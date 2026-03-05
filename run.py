from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.routing import Router
from config import DATABASE_URL, SECRET_KEY, DEBUG
from app.api.routes import router

app = FastAPI(debug=DEBUG)

# Erlaubte Origins (für Entwicklung ggf. ["*"] verwenden)
origins = [
    "http://localhost:51513",
    "http://127.0.0.1:51513",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:56603",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # in Entwicklung: ["*"], in Produktion konkrete Domains
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
