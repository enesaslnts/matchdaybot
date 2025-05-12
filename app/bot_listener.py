import os
import discord
from dotenv import load_dotenv
import asyncio
from app.deepseek_prompt import erklaere_cve
from app.main import analyse_and_send

load_dotenv()

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
        await handle_explain_command(message)
    elif message.content.startswith("/scan"):
        await handle_scan_command(message)

async def handle_explain_command(message):
    try:
        cve_id = message.content.split(" ")[1].strip()
        print(f"📥 Anfrage für: {cve_id}")
        print("🔐 API-Key (gekürzt):", os.getenv("DEEPSEEK_API_KEY")[:8] + "..." if os.getenv("DEEPSEEK_API_KEY") else "Nicht gesetzt")

        antwort = erklaere_cve(cve_id)
        await message.channel.send(f"🛡️ Erklärung für **{cve_id}**:\n\n{antwort}")
    except Exception as e:
        await message.channel.send(f"⚠️ Fehler: {str(e)}")

async def handle_scan_command(message):
    try:
        await message.channel.send("🔎 Starte lokalen Trivy-Scan...")

        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, analyse_and_send)

        await message.channel.send(result)
    except Exception as e:
        await message.channel.send(f"❌ Fehler bei der Sicherheitsanalyse: {str(e)}")

# Bot starten
client.run(os.getenv("DISCORD_BOT_TOKEN"))
