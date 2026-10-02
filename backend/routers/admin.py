from fastapi import APIRouter

router = APIRouter()


@router.get("/predictions")
def get_predictions():
    return {
        "predictions": [
            {"topic": "المعرفة", "probability": 0.83, "reason": "تكرار واسع في الدروس والاختبارات"},
            {"topic": "الوجود", "probability": 0.76, "reason": "مكرر في المحاور الفلسفية الأساسية"},
            {"topic": "الأخلاق", "probability": 0.71, "reason": "مواضيع قابلة للتكرار في الامتحان"},
            {"topic": "الحرية", "probability": 0.65, "reason": "تظهر في معظم النقاشات الفلسفية"},
        ]
    }

