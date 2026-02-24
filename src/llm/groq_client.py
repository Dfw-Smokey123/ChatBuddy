"""Groq LLM Client Integration with LangChain"""
from langchain_groq import ChatGroq
from config.settings import GROQ_API_KEY, LLM_MODEL, LLM_TEMPERATURE, LLM_MAX_TOKENS


class GroqClient:
    """Wrapper for Groq LLM via LangChain"""

    def __init__(self, model=LLM_MODEL, temperature=LLM_TEMPERATURE, max_tokens=LLM_MAX_TOKENS):
        """
        Initialize Groq client

        Args:
            model: Model name (default: openai/gpt-oss-120b)
            temperature: Sampling temperature (0-1)
            max_tokens: Maximum tokens in response
        """
        self.client = ChatGroq(
            api_key=GROQ_API_KEY,
            model_name=model,
            temperature=temperature,
            max_tokens=max_tokens,
        )

    def chat(self, messages):
        """
        Send messages to Groq and get response

        Args:
            messages: List of message dicts with 'role' and 'content'

        Returns:
            Response text from the model
        """
        try:
            response = self.client.invoke(messages)
            return response.content
        except Exception as e:
            raise RuntimeError(f"Error communicating with Groq: {str(e)}")

    def stream_chat(self, messages):
        """
        Stream chat response from Groq

        Args:
            messages: List of message dicts

        Yields:
            Streamed response chunks
        """
        try:
            for chunk in self.client.stream(messages):
                if chunk.content:
                    yield chunk.content
        except Exception as e:
            raise RuntimeError(f"Error streaming from Groq: {str(e)}")
