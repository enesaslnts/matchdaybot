import os
import discord
import asyncio
from dotenv import load_dotenv
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
        antwort = erklaere_cve(cve_id)
        await message.channel.send(f"🛡️ Erklärung für **{cve_id}**:\n\n{antwort}")
    except Exception as e:
        await message.channel.send(f"⚠️ Fehler: {str(e)}")

async def handle_scan_command(message):
    try:
        await message.channel.send("🔎 Starte lokalen Trivy-Scan...")

        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, lambda: analyse_and_send(discord_output=False))

        await message.channel.send(result)
    except Exception as e:
        await message.channel.send(f"❌ Fehler bei der Sicherheitsanalyse: {str(e)}")

client.run(os.getenv("DISCORD_BOT_TOKEN"))
