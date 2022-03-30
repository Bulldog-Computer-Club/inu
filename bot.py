import os
import sys

import discord
import dotenv

dotenv.load_dotenv()
client = discord.Client()
token = os.getenv("DISCORD_TOKEN")

@client.event
async def on_ready():
    print(f"Successfully logged in as {client.user}")

if __name__ == "__main__":
    if not token:
        print("required environmental variable DISCORD_TOKEN not set")
        sys.exit(1)

    client.run(token)
