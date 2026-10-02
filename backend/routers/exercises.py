from fastapi import APIRouter, HTTPException

from schemas import get_lessons, get_lesson_by_id

router = APIRouter()


@router.get("/lessons")
def list_lessons():
    return {"lessons": get_lessons()}


@router.get("/lessons/{lesson_id}")
def lesson_detail(lesson_id: int):
    lesson = get_lesson_by_id(lesson_id)
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return lesson

