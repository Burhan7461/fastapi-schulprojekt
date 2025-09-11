from fastapi import FastAPI
from starlette.routing import Router
from config import DATABASE_URL, SECRET_KEY, DEBUG
from app.api.routes import router

app = FastAPI(debug=DEBUG)
app.include_router(router)
