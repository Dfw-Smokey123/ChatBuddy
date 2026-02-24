# ChatBuddy – AI-Powered Mental Health Companion

An AI-powered mental health companion built with LangChain, Groq, and Streamlit.

## Features

- 24/7 AI emotional support
- Multiple predefined personas (Therapist, Wellness Coach, etc.)
- Custom prompt system
- Session-based conversations

## Tech Stack

- **Frontend**: Streamlit
- **LLM Framework**: LangChain
- **LLM Provider**: Groq
- **Language**: Python 3.9+

## Project Structure

```
ChatBuddy/
├── src/
│   ├── llm/              # LLM integration (Groq/LangChain)
│   ├── prompts/          # Custom prompt system & personas
│   ├── utils/            # Utility functions
│   └── __init__.py
├── config/               # Configuration files
├── assets/               # Images, icons, etc.
├── streamlit_app.py      # Main Streamlit entry point
├── requirements.txt      # Python dependencies
├── .env.example          # Environment variables template
└── README.md
```

## Setup

1. Clone the repository
2. Copy `.env.example` to `.env` and add your Groq API key
3. Install dependencies: `pip install -r requirements.txt`
4. Run the app: `streamlit run streamlit_app.py`

## Development

- `src/llm/groq_client.py` - Groq LLM client integration
- `src/prompts/personas.py` - Persona definitions and prompt templates
- `config/settings.py` - Application configuration
- `src/utils/` - Helper functions for chat management

## License

MIT
