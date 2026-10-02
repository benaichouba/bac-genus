from fastapi import APIRouter, Query

from schemas import get_exercises_by_lesson, add_exercise
from services.content_service import generate_exercise_set

router = APIRouter()


@router.get("/exercises")
def get_exercises(lesson_id: int = Query(...), level: str = "beginner"):
    exercises = get_exercises_by_lesson(lesson_id, level)
    if not exercises:
        custom_exercises = generate_exercise_set(lesson_id, level)
        return {"lesson_id": lesson_id, "level": level, "exercises": custom_exercises}
    return {"lesson_id": lesson_id, "level": level, "exercises": exercises}


@router.post("/exercises/generate")
def generate_exercises(lesson_id: int, level: str = "beginner"):
    return {"lesson_id": lesson_id, "level": level, "exercises": generate_exercise_set(lesson_id, level)}

