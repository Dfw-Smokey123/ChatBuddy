"""Application Settings and Configuration"""
import os
from dotenv import load_dotenv
import streamlit as st

# Load environment variables from .env file (local development only)
load_dotenv()

# API Configuration - Try Streamlit secrets first (cloud), then environment variables (local)
def get_groq_api_key():
    """Get GROQ_API_KEY from Streamlit secrets or environment variables."""
    try:
        # Streamlit Cloud secrets
        return st.secrets.get("GROQ_API_KEY")
    except Exception:
        # Local development from .env or environment
        return os.getenv("GROQ_API_KEY")

GROQ_API_KEY = get_groq_api_key()

# Application Settings
DEBUG_MODE = os.getenv("DEBUG_MODE", "false").lower() == "true"
STREAMLIT_THEME = os.getenv("STREAMLIT_THEME", "dark")

# LLM Configuration
LLM_MODEL = "mixtral-8x7b-32768"  # Default Groq model (updated for compatibility)
LLM_TEMPERATURE = 0.7
LLM_MAX_TOKENS = 1024

# Validation
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in Streamlit secrets or environment variables.")
