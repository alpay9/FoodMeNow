from pydantic import BaseModel
from typing import Optional, Dict

class ScrapeRequest(BaseModel):
    location: str
    filters: Optional[Dict] = None

class ScrapeResponse(BaseModel):
    success: bool
    message: str

class RecommendationRequest(BaseModel):
    user_id: int
    filters: Optional[Dict] = None

class RecommendationResponse(BaseModel):
    food_id: str
    name: str
    restaurant_name: str
    price: float
    description: Optional[str] = None

class FeedbackRequest(BaseModel):
    user_id: int
    food_id: str
    grade_by_user: int

class FeedbackResponse(BaseModel):
    success: bool
