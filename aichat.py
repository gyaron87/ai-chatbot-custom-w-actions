from google import genai
from google.genai import types
import subprocess

client = genai.Client(api_key="YOUR_API_KEY")

conversation = [
    "HERE_WHAT_PERSONALITY_YOU_WOULD_LIKE_TO_ADD"
    "FIRST_THING_TO_SAY",
]

# A teljes beszélgetés egy stringként megy
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="\n".join(conversation),
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0),
        max_output_tokens=50,
    )
)

bot_reply = response.text
print("Bot:", bot_reply)

while True:
    user_input = input("Te: ")
    if not user_input:
        print("Chatbot leállítva.")
        break

    conversation.append(f"User: {user_input}")

    # A teljes beszélgetés egy stringként megy
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="\n".join(conversation),
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0)
        )
    )

    bot_reply = response.text
    print("Bot:", bot_reply)

    conversation.append(f"Bot: {bot_reply}")
    #subprocess.run(["espeak", "-v", "hu", bot_reply])

