from fastapi import FastAPI
from config import DATABASE_URL, SECRET_KEY, DEBUG

app = FastAPI(debug=DEBUG)

@app.get("/config-check")
def config_check():
    return {
        "database": DATABASE_URL,
        "secret_key": SECRET_KEY,
        "debug": DEBUG
    }
