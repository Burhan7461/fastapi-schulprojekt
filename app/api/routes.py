from fastapi import APIRouter

router = APIRouter()

@router.get("/testen")
def hello():
    return {"message": "Backend laeuft!"}
