import os
import discord
from dotenv import load_dotenv
from app.deepseek_prompt import erklaere_cve

load_dotenv()

# Discord Intents konfigurieren
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Bot ist online als {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("/erkläre"):
        cve_id = message.content.split(" ")[1].strip()
        print(f"📥 Anfrage für: {cve_id}")
        print("🔐 API-Key (gekürzt):", os.getenv("DEEPSEEK_API_KEY")[:8] + "..." if os.getenv("DEEPSEEK_API_KEY") else "Nicht gesetzt")

        try:
            antwort = erklaere_cve(cve_id)
            await message.channel.send(f"🛡️ Erklärung für **{cve_id}**:\n\n{antwort}")
        except Exception as e:
            await message.channel.send(f"⚠️ Fehler: {str(e)}")

# Bot starten
client.run(os.getenv("DISCORD_BOT_TOKEN"))
