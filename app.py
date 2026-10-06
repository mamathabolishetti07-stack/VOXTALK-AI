import streamlit as st

from chatbot import get_ai_response
from rag import build_database, retrieve_context
from text_to_speech import text_to_speech
from voice import speech_to_text


st.set_page_config(
    page_title="VoxTalk AI",
    page_icon="🎙️"
)

st.title("🎙️ VoxTalk AI")
st.write("Your multilingual conversational AI assistant")


# -----------------------------
# Language Selection
# -----------------------------

language = st.selectbox(
    "Choose language",
    [
        "English",
        "Telugu",
        "Hindi",
        "Tamil",
        "Kannada"
    ]
)

language_codes = {
    "English": "en-IN",
    "Telugu": "te-IN",
    "Hindi": "hi-IN",
    "Tamil": "ta-IN",
    "Kannada": "kn-IN"
}


# -----------------------------
# Microphone
# -----------------------------

audio = st.audio_input(
    "🎤 Speak to VoxTalk AI"
)

if audio:

    spoken_text = speech_to_text(
        audio,
        language_codes[language]
    )

    if spoken_text:
        st.write(
            f"You said: {spoken_text}"
        )


# -----------------------------
# Build RAG database
# -----------------------------

build_database()


# -----------------------------
# Chat History
# -----------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:

    if message["role"] != "system":

        with st.chat_message(message["role"]):
            st.write(message["content"])


# -----------------------------
# Text Input
# -----------------------------

prompt = st.chat_input(
    "Ask VoxTalk AI something..."
)


if prompt:

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.write(prompt)


    # Retrieve relevant information
    context = retrieve_context(prompt)


    # Get AI answer
    answer = get_ai_response(
        st.session_state.messages,
        context
    )


    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })


    with st.chat_message("assistant"):
        st.write(answer)


    # Convert answer to speech
    audio_response = text_to_speech(
        answer,
        language
    )

    st.audio(
        audio_response,
        format="audio/mp3"
    )