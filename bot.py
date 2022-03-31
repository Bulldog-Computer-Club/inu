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

logging.basicConfig(format="%(asctime)s [%(levelname)s]: %(message)s", level=logging.INFO)

@client.event
async def on_ready():
    logging.info(f"successfully logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(message)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--token", help="specify a Discord bot token")
    args = parser.parse_args()
    if not token:
        token = args.token
        if not token:
            logging.error("no token specified, use --token or set DISCORD_TOKEN")
            sys.exit(1)

    client.run(token)
