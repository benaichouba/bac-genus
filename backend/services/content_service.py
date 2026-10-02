from fastapi import APIRouter, File, UploadFile, Form, HTTPException
from pathlib import Path
import os

from services.content_service import parse_uploaded_text, generate_exercise_set, update_topic_scores
from schemas import save_upload, add_lesson

router = APIRouter()
UPLOAD_DIR = Path(__file__).resolve().parents[1] / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True, parents=True)


@router.post("/upload")
async def upload_file(file: UploadFile = File(...), title: str = Form(default="درس جديد")):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file uploaded")

    file_ext = file.filename.lower().split(".")[-1]
    allowed = {"pdf", "txt", "md"}
    if file_ext not in allowed:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    safe_name = file.filename.replace(" ", "_")
    target_path = UPLOAD_DIR / safe_name

    with target_path.open("wb") as f:
        content = await file.read()
        f.write(content)

    upload_id = save_upload(safe_name, file.filename, str(target_path))
    text = parse_uploaded_text(target_path)

    if not text.strip():
        raise HTTPException(status_code=400, detail="Could not read content from uploaded file")

    lesson_id = add_lesson(title=title, summary=text[:220], content=text, source=file.filename)
    update_topic_scores(text)

    return {
        "status": "success",
        "upload_id": upload_id,
        "lesson_id": lesson_id,
        "file_name": file.filename,
        "generated_exercises": generate_exercise_set(lesson_id, "beginner")
    }


@router.get("/uploads")
def list_uploads():
    from schemas import get_uploads
    return {"uploads": get_uploads()}

