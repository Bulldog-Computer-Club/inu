import os
import sys

import discord

client = discord.Client()


@client.event
async def on_ready():
    print(f"Successfully logged in as {client.user}")


token = os.getenv("DISCORD_TOKEN")
if not token:
    print("required environmental variable DISCORD_TOKEN not set")
    sys.exit(1)

client.run(token)
