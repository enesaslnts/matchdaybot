import requests
import os

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def send_discord_message(message):
    if not DISCORD_WEBHOOK_URL:
        raise Exception("Webhook URL nicht gesetzt!")

    chunks = split_message(message)
    for chunk in chunks:
        payload = {"content": chunk}
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        if response.status_code != 204:
            raise Exception(f"Fehler beim Senden: {response.status_code}, {response.text}")

def split_message(text, limit=1900):
    """Teilt die Nachricht in Blöcke von max. 1900 Zeichen (für Sicherheit)"""
    lines = text.split('\n')
    blocks = []
    current = ""

    for line in lines:
        if len(current) + len(line) + 1 > limit:
            blocks.append(current)
            current = ""
        current += line + "\n"

    if current:
        blocks.append(current)

    return blocks
