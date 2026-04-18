# backend.py - Clean Final Version

import os
from groq import Groq

class MultilingualChatbot:
    def __init__(self):
        # ✅ Proper API key usage
        self.client = Groq(
            api_key="groq_api_key"
        )

    def chat(self, message, language="English", history=None):

        # ✅ Fix mutable default bug
        if history is None:
            history = []

        # ---------------- SYSTEM MESSAGE ----------------
         messages = [
            {
                "role": "system",
                "content": f"You are a helpful AI assistant. Reply in {language}."
            }
        ]
        
        # ---------------- ADD HISTORY ----------------
        # History already contains user + assistant messages
        for msg in history:
            if msg["role"] in ["user", "assistant"]:
                messages.append({
                    "role": msg["role"],
                    "content": msg["content"]
                })

        # ❌ DO NOT append message again (already included from UI)

        # ---------------- API CALL ----------------
        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.7,
            max_tokens=1024
        )

        # ---------------- RETURN RESPONSE ----------------
        return response.choices[0].message.content