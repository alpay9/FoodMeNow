from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FoodMeNow backend is running!"}

class ScrapeRequest(BaseModel):
    location: str
    filters: dict

@app.post("/scrape-restaurants")
def scrape_restaurants(request: ScrapeRequest):
    
    # Scraping logic would go here

    return {"success": True, "message": "Scraping started"}
