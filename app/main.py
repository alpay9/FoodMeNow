from fastapi import FastAPI
from app.api.endpoints import restaurants, recommendations, feedback

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to FoodMeNow API!"}

app.include_router(restaurants.router, prefix="/restaurants", tags=["restaurants"])
app.include_router(recommendations.router, prefix="/recommendations", tags=["recommendations"])
app.include_router(feedback.router, prefix="/feedback", tags=["feedback"])
