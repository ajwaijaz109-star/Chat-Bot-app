from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message")

    if not user_message:
        return JSONResponse({"error": "No message provided"}, status_code=400)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful chatbot."},
                {"role": "user", "content": user_message},
            ]
        )
        bot_reply = response["choices"][0]["message"]["content"]
        return {"reply": bot_reply}
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
