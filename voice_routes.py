from fastapi import APIRouter, UploadFile, Form
import os

from speech_to_text import speech_to_text
from text_to_speech import text_to_speech
from app import answer_user_query, collection   

router = APIRouter()

@router.post("/voice-chat")
async def voice_chat(file: UploadFile, language: str = Form("english")):
    # 1) Save uploaded audio temporarily
    os.makedirs("static/voice", exist_ok=True)
    temp_path = f"static/voice/{file.filename}"
    with open(temp_path, "wb") as f:
        f.write(await file.read())

    # 2) Convert speech → text
    user_msg = speech_to_text(temp_path)
    if not user_msg:
        os.remove(temp_path)
        return {"audio_url": None, "reply": None, "error": "Unable to understand voice message"}

    # 3) Get RAG answer (same pipeline as text chat)
    bot_reply = answer_user_query(user_msg, collection, language)

    # 4) Convert answer text → speech
    audio_file = text_to_speech(bot_reply, language)

    # 5) Clean up temp input file
    os.remove(temp_path)

    return {"audio_url": audio_file, "reply": bot_reply}
