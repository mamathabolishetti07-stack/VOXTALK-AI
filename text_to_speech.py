from gtts import gTTS
import io


language_codes = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "Tamil": "ta",
    "Kannada": "kn"
}


def text_to_speech(
    text,
    language
):

    tts = gTTS(
        text=text,
        lang=language_codes[language]
    )

    audio = io.BytesIO()

    tts.write_to_fp(audio)

    return audio.getvalue()