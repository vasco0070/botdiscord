import discord
import a2s
import asyncio

# Token-ul botului tău de la Discord Developer Portal
TOKEN = "MTI4MDIyOTk3ODU0MTEzMzg5Ng.G4GlCe.ra-liD_sXMPl48vX89aW_z5sol-o02llOlqjWw"

# IP-ul și portul serverului tău de CS2
SERVER_IP = "5.183.171.78"
SERVER_PORT = 27015  # Modifică dacă ai alt port

intents = discord.Intents.default()
client = discord.Client(intents=intents)

# Funcție pentru actualizarea statusului botului
async def update_status():
    await client.wait_until_ready()
    while not client.is_closed():
        try:
            address = (SERVER_IP, SERVER_PORT)
            info = a2s.info(address)
            status = f"🎮 {info.player_count}/{info.max_players} jucători online"
        except:
            status = "❌ Server offline"

        await client.change_presence(activity=discord.Game(status))
        await asyncio.sleep(30)  # Update la fiecare 30 secunde

@client.event
async def on_ready():
    print(f"✅ Botul {client.user} este online!")
    client.loop.create_task(update_status())

client.run(TOKEN)
