import os
import json
import subprocess
from dotenv import load_dotenv

load_dotenv()

from discord_webhook import send_discord_message
from deepseek_prompt import load_prompt, erklaere_cve, client
from trivy_parser import extract_vulnerabilities

def run_trivy_scan():
    try:
        print("🚀 Starte Trivy-Scan des Docker-Images...")
        subprocess.run(
            [
                "trivy", "image", "--severity", "HIGH,CRITICAL",
                "--format", "json", 
                "--output", "trivy_output.json",
                "ghcr.io/enesaslnts/matchdaybot:latest"
            ],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print("✅ Trivy-Image-Scan abgeschlossen.")
    except subprocess.CalledProcessError as e:
        send_discord_message(f"❌ Fehler beim Trivy-Scan:\n```\n{e.stderr.strip()}\n```")
        raise


def build_prompt(template, vulnerabilities):
    return f"""
{template}

Analysiere die folgenden Sicherheitslücken (Top 5) und liefere:
1. Einen kurzen Fußball-Analysten-Kommentar (1–2 Sätze, humorvoll).
2. Eine Markdown-Tabelle mit: Package | Severity | CVE | Fixed Version | How to Fix
3. Technische Key Notes (z. B. CVE-Typ, betroffene Komponenten)
4. Klare Handlungsempfehlungen ("Auswechseln", "Taktik umstellen", "Sofort patchen")

Hier sind die Daten:
{json.dumps(vulnerabilities[:5], indent=2)}
"""

def analyse_and_send(discord_output: bool = True) -> str:
    try:
        run_trivy_scan()

        vulnerabilities = extract_vulnerabilities()

        if not vulnerabilities:
            msg = "✅ Kein Foulspiel entdeckt. Die Abwehr steht – saubere Leistung! 🧤⚽"
            print(msg)
            if discord_output:
                send_discord_message(msg)
            return msg

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

        print("📝 Analyse erfolgreich abgeschlossen.")
        if discord_output:
            send_discord_message(result)
        return result

    except Exception as e:
        msg = f"❌ Fehler bei der Spielanalyse: {str(e)}"
        print(msg)
        if discord_output:
            send_discord_message(msg)
        return msg

def handle_custom_command(message_content: str):
    if message_content.startswith("/erkläre"):
        try:
            cve_id = message_content.split(" ")[1].strip()
            antwort = erklaere_cve(cve_id)
            send_discord_message(f"🛡️ Erklärung für **{cve_id}**:\n\n{antwort}")
        except Exception as e:
            send_discord_message(f"⚠️ Fehler: {str(e)}")

if __name__ == "__main__":
    analyse_and_send()
    
