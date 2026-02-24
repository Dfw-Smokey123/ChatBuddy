"""Main Streamlit Application - ChatBuddy"""
import streamlit as st
from src.llm import GroqClient
from src.prompts import PERSONAS, get_persona_prompt, get_persona_names
from config.settings import STREAMLIT_THEME

# Page Configuration
st.set_page_config(
    page_title="ChatBuddy - Mental Health Companion",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS
st.markdown(
    """
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .chat-message {
        padding: 12px;
        border-radius: 8px;
        margin: 8px 0;
    }
    .user-message {
        background-color: #e3f2fd;
        text-align: right;
    }
    .assistant-message {
        background-color: #f3e5f5;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def initialize_session_state():
    """Initialize session state variables"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "current_persona" not in st.session_state:
        st.session_state.current_persona = "therapist"
    if "llm_client" not in st.session_state:
        st.session_state.llm_client = GroqClient()


def display_chat_history():
    """Display chat history"""
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f'<div class="chat-message user-message">👤 {message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(
                f'<div class="chat-message assistant-message">🤖 {message["content"]}</div>', unsafe_allow_html=True
            )


def get_ai_response(user_message):
    """Get response from Groq AI"""
    # Build message history with system prompt
    system_prompt = get_persona_prompt(st.session_state.current_persona)
    messages = [{"role": "system", "content": system_prompt}]

    # Add conversation history
    for msg in st.session_state.messages:
        messages.append({"role": msg["role"], "content": msg["content"]})

    # Add current user message
    messages.append({"role": "user", "content": user_message})

    # Get AI response
    response = st.session_state.llm_client.chat(messages)
    return response


def main():
    """Main Streamlit application"""
    initialize_session_state()

    # Sidebar - Persona Selection
    with st.sidebar:
        st.title("⚙️ ChatBuddy Settings")
        st.divider()

        st.subheader("Select Your Companion")
        persona_names = get_persona_names()
        personas_list = [(key, info["name"], info["description"]) for key, info in persona_names.items()]

        for key, name, description in personas_list:
            if st.button(f"**{name}**\n_{description}_", key=key, use_container_width=True):
                st.session_state.current_persona = key
                st.session_state.messages = []  # Reset chat when changing persona
                st.rerun()

        st.divider()

        # Current Persona Info
        current_persona = st.session_state.current_persona
        persona_info = PERSONAS[current_persona]
        st.info(f"**Currently chatting with:**\n\n{persona_info['name']}\n\n_{persona_info['description']}_")

        st.divider()

        # Clear Chat Button
        if st.button("🗑️ Clear Chat History", use_container_width=True):
            st.session_state.messages = []
            st.rerun()

        st.divider()
        st.markdown(
            """
        **About ChatBuddy**
        
        ChatBuddy is your 24/7 AI-powered mental health companion. Choose a persona above and start chatting!
        
        ⚠️ **Disclaimer**: ChatBuddy is not a substitute for professional mental health treatment.
        """
        )

    # Main Chat Interface
    st.title("💬 ChatBuddy")
    st.markdown(f"**Connected to: {PERSONAS[st.session_state.current_persona]['name']}**")
    st.divider()

    # Display chat history
    display_chat_history()

    # User Input
    user_input = st.chat_input("Type your message here...", key="user_input")

    if user_input:
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Display user message
        st.markdown(f'<div class="chat-message user-message">👤 {user_input}</div>', unsafe_allow_html=True)

        # Get and display AI response
        with st.spinner("Thinking..."):
            ai_response = get_ai_response(user_input)
            st.session_state.messages.append({"role": "assistant", "content": ai_response})

            st.markdown(f'<div class="chat-message assistant-message">🤖 {ai_response}</div>', unsafe_allow_html=True)

        st.rerun()


if __name__ == "__main__":
    main()
