import os
from pathlib import Path

from dotenv import load_dotenv


# Project root directory
BASE_DIR = Path(__file__).resolve().parent

# Load variables from .env
load_dotenv(BASE_DIR / ".env")


# Application settings
APP_NAME = os.getenv(
    "APP_NAME",
    "LegalEase - AI Legal Document Generator"
)

BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://127.0.0.1:8000"
)


# Gemini settings
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()

GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-3.8-flash"
)


# Image directory
IMAGE_DIR = BASE_DIR / "Image"

LOGO_PATH = IMAGE_DIR / "Logo.png"

INVERSE_LOGO_PATH = IMAGE_DIR / "inverseLogo.png"


def validate_settings():
    """
    Check whether the required Gemini API key is available.
    """

    if not GEMINI_API_KEY:
        raise RuntimeError(
            "GEMINI_API_KEY is missing. "
            "Please add your Gemini API key to the .env file."
        )

    return True