from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import init_db
from routers import admin, lessons, exercises, analysis, predictions

app = FastAPI(title="BAC GENUS", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(admin.router, prefix="/api/admin", tags=["admin"])
app.include_router(lessons.router, prefix="/api", tags=["lessons"])
app.include_router(exercises.router, prefix="/api", tags=["exercises"])
app.include_router(analysis.router, prefix="/api", tags=["analysis"])
app.include_router(predictions.router, prefix="/api", tags=["predictions"])


@app.on_event("startup")
def startup_event():
    init_db()


@app.get("/api/health")
def health():
    return {"status": "ok", "app": "BAC GENUS"}


@app.get("/")
def root():
    return {"message": "BAC GENUS backend is running."}

