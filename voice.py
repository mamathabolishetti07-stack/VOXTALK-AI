import tempfile
import speech_recognition as sr


def speech_to_text(audio_file, language_code="en-IN"):

    recognizer = sr.Recognizer()

    with tempfile.NamedTemporaryFile(
        suffix=".wav",
        delete=False
    ) as temp_file:

        temp_file.write(
            audio_file.getvalue()
        )

        temp_path = temp_file.name

    try:

        with sr.AudioFile(temp_path) as source:

            audio = recognizer.record(source)

        text = recognizer.recognize_google(
            audio,
            language=language_code
        )

        return text

    except Exception:
        return None