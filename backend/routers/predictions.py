from fastapi import APIRouter

from schemas import get_topics

router = APIRouter()


@router.get("/analysis")
def get_analysis():
    topics = get_topics()
    return {"topics": topics}

