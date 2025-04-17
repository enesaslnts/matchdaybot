import os
import json
from app.discord_webhook import send_discord_message
from app.deepseek_prompt import load_prompt
from app.trivy_parser import extract_vulnerabilities
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

def build_prompt(template, vulnerabilities):
    return f"""
{template}

Analysiere die folgenden Sicherheitslücken (Top 5) und liefere:
1. Einen kurzen Fußball-Analysten-Kommentar (1-2 Sätze, humorvoll).
2. Eine Markdown-Tabelle mit: Package | Severity | CVE | Fixed Version | How to Fix
3. Technische Key Notes (z. B. CVE-Typ, betroffene Komponenten)
4. Klare Handlungsempfehlungen ("Auswechseln", "Taktik umstellen", "Sofort patchen")

Hier sind die Daten:
{json.dumps(vulnerabilities[:5], indent=2)}
"""

def analyse_and_send():
    try:
        vulnerabilities = extract_vulnerabilities()

        if not vulnerabilities:
            send_discord_message("✅ Kein Foulspiel entdeckt. Die Abwehr steht – saubere Leistung! 🧤⚽")
            return

        humor_template = load_prompt()
        prompt = build_prompt(humor_template, vulnerabilities)

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        result = response.choices[0].message.content.strip()
        if not result:
            result = "⚠️ Analyse leer – vielleicht war das nur ein Freundschaftsspiel."

        send_discord_message(result)

    except Exception as e:
        send_discord_message(f"❌ Fehler bei der Spielanalyse: {str(e)}")

if __name__ == "__main__":
    analyse_and_send()
