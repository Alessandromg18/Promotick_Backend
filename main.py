from fastapi import FastAPI

from routes.upload import router as upload_router
from routes.metrics import router as metrics_router

from routes.auth import router as auth_router
from services.storage_service import init_db

app = FastAPI()

init_db()

app.include_router(upload_router)
app.include_router(metrics_router)
app.include_router(auth_router)