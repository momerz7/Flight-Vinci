from fastapi import FastAPI
from dotenv import load_dotenv
from app.routers import health

app = FastAPI()
app.include_router(health.router)

@app.get("/")
def root():
    return {"message": "FlightVinci backend is running"}

load_dotenv()
