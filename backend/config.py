import os
from dotenv import load_dotenv

load_dotenv(override=True)


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret")
    JWT_EXP_MINUTES = int(os.getenv("JWT_EXP_MINUTES", "120"))
    MONGO_URI = os.getenv("MONGO_URI")
    MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "career_guidance_db")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    CORS_ORIGINS = [o.strip() for o in os.getenv("CORS_ORIGINS", "*").split(",")]
