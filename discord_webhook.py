import requests
import os

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def send_discord_message(message):
    if not DISCORD_WEBHOOK_URL:
        raise Exception("Webhook URL nicht gesetzt!")

    payload = {"content": message}
    response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
    if response.status_code != 204:
        raise Exception(f"Fehler beim Senden: {response.status_code}, {response.text}")
