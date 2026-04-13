from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="AI Intelligence Platform",
    version="2.0.0"
)

app.include_router(router)

@app.get("/")
def health():
    return {"status": "running", "system": "AI Intelligence Platform"}
