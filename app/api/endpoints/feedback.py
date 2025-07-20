from fastapi import APIRouter
from app.models.schemas import FeedbackRequest, FeedbackResponse
from app.services.feedback import save_feedback_service

router = APIRouter()

@router.post("/")
def feedback(request: FeedbackRequest):
    result = save_feedback_service(request)
    return FeedbackResponse(success=result)
