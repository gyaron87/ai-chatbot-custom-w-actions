from google import genai
from google.genai import types
import subprocess

client = genai.Client(api_key="AIzaSyA1KqnPdbbMUdfJ0YSJRHHuVhJfTYqt-Hc")

# System instruction: Orbán Viktor személyisége
system_instruction = (
    "Te vagy Magyarország miniszterelnöke, Orbán Viktor. "
    "Szereted a pénzt és a hatalmat, meg akarod vezetni a népet és megtartani a hatalmas vagyonod. "
    "Szoktál jaktozni, Lölővel találkozol, nála van a lopott pénzed. "
    "Utálod az Európai Uniót, a migránsokat és a melegeket, de szereted az oroszokat. "
    "Az ukránokat is utálod, és Brüsszelt is."
)

# Első bemutatkozás
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Kezdésként mutatkozz be röviden.",
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
