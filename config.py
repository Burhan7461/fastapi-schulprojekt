from dotenv import load_dotenv
import os

load_dotenv()  # Lädt die .env-Datei automatisch

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./dummy.db")
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG", "False") == "True"
