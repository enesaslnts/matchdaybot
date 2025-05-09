import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Funktioniert für DeepSeek (kompatibel mit openai>=1.2.0)
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com/v1"  # ⚠️ /v1 NICHT vergessen!
)

def load_prompt():
    path = os.getenv("MODEL_HUMOR_PATH1", "model_prompt.md")
    try:
        with open(path, "r") as file:
            return file.read().strip()
    except Exception:
        return """You are a tactical football analyst, uncovering security vulnerabilities like defensive weaknesses.
- Use football metaphors ("like a red card in the final minute")
- Always end with a football-themed kicker ("Abpfiff!" or "Tor für die Sicherheit!")
- Use emojis ⚽🟥📉📊
Example: "This CVE is like leaving the goal open during a penalty shootout. 🥅⚠️ Abpfiff!"
"""

def erklaere_cve(cve_id: str) -> str:
    messages = [
        {
            "role": "system",
            "content": (
                "Du bist ein Cybersicherheitsanalyst mit Fußball-Metaphern. "
                "Erkläre CVEs einfach, mit Bewertung und Handlungsempfehlung. "
                "Verwende Fußballbilder („rote Karte“, „Abwehrlücke“ etc.) und Emojis ⚽🚨."
            )
        },
        {
            "role": "user",
            "content": f"Erkläre CVE {cve_id} für Laien – mit Risikobewertung und kurzer Handlungsempfehlung."
        }
    ]

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Fehler beim Abrufen der CVE-Erklärung: {str(e)}"
