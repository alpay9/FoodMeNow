from fastapi import APIRouter
from app.models.schemas import ScrapeRequest, ScrapeResponse
from app.services.scraping import scrape_restaurants_service

router = APIRouter()

@router.post("/scrape")
def scrape_restaurants(request: ScrapeRequest):
    result = scrape_restaurants_service(request)
    return ScrapeResponse(success=True, message=result)
