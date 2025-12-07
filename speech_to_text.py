import speech_recognition as sr

def speech_to_text(audio_path: str) -> str:
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)

    try:
        # hi-IN handles Hindi + a lot of Hinglish reasonably well
        return recognizer.recognize_google(audio, language="hi-IN")
    except:
        return ""
