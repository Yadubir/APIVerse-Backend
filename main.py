from fastapi import FastAPI
from routes import search, integration, health, review, categories
import uvicorn
import os

app = FastAPI()

# CORS setup
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(search.router)
app.include_router(integration.router)
app.include_router(health.router)
app.include_router(review.router)
app.include_router(categories.router)

@app.get("/")
def read_root():
    return {"message": "Hello from APIVerse backend"}

# === Entry point ===
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # default to 8000 if not found
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)