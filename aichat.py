from google import genai
from google.genai import types
import subprocess

client = genai.Client(api_key="YOUR_API_KEY")

# System instruction: Orbán Viktor személyisége
system_instruction = (
            "CHATBOT_CHARACHTERISTICS"
)

# Első bemutatkozás
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="FIRST_THING_TO_START_SAYING",
    config=types.GenerateContentConfig(
        system_instruction=system_instruction,
        thinking_config=types.ThinkingConfig(thinking_budget=0)
    )
)

bot_reply = response.text
print("Bot:", bot_reply)

# Beszélgetés lista
conversation = [f"Bot: {bot_reply}"]

# Végtelen chat loop
while True:
    user_input = input("Te: ")
    if not user_input:
        print("Chatbot leállítva.")
        break

    conversation.append(f"User: {user_input}")

    prompt = "\n".join(conversation)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            thinking_config=types.ThinkingConfig(thinking_budget=0)
        )
    )

    bot_reply = response.text
    print("Bot:", bot_reply)

    conversation.append(f"Bot: {bot_reply}")
    # subprocess.run(["espeak", "-v", "hu", bot_reply])
