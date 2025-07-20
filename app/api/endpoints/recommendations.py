from fastapi import APIRouter
from app.models.schemas import RecommendationRequest, RecommendationResponse
from app.services.recommendation import get_recommendation_service

router = APIRouter()

@router.post("/")
def get_recommendation(request: RecommendationRequest):
    result = get_recommendation_service(request)
    return RecommendationResponse(**result)
