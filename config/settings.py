"""Application Settings and Configuration"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Application Settings
DEBUG_MODE = os.getenv("DEBUG_MODE", "false").lower() == "true"
STREAMLIT_THEME = os.getenv("STREAMLIT_THEME", "dark")

# LLM Configuration
LLM_MODEL = "openai/gpt-oss-120b"  # Default Groq model
LLM_TEMPERATURE = 0.7
LLM_MAX_TOKENS = 1024

# Validation
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in environment variables. Please set it in .env file.")
