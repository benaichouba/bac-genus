from pydantic import BaseModel, Field
from typing import Optional, List


class LessonBase(BaseModel):
    title: str
    summary: Optional[str] = None
    content: str
    source: Optional[str] = "uploaded"


class LessonCreate(LessonBase):
    pass


class LessonOut(LessonBase):
    id: int


class ExerciseBase(BaseModel):
    lesson_id: int
    level: str = Field(default="beginner")
    question: str
    answer: Optional[str] = None


class ExerciseOut(ExerciseBase):
    id: int


class TopicOut(BaseModel):
    id: int
    name: str
    score: int
    source: Optional[str] = None


class UploadItem(BaseModel):
    id: int
    file_name: str
    original_name: str
    file_path: str
