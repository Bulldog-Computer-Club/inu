#!/usr/bin/env python3

import os
import sys
import argparse
import logging

import discord
import dotenv

dotenv.load_dotenv()
client = discord.Client()
token = os.getenv("DISCORD_TOKEN")

logging.basicConfig(format="%(asctime)s [%(levelname)s]: %(message)s")

@client.event
async def on_ready():
    print(f"Successfully logged in as {client.user}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--token", help="specify a Discord bot token")
    args = parser.parse_args()
    token = args.token
    if not token:
        logging.error("no token specified, use --token or set DISCORD_TOKEN")
        sys.exit(1)

    client.run(token)
