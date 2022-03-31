#!/usr/bin/env python3

import argparse
import logging
import os
import sys
from typing import Optional

import discord
import dotenv

dotenv.load_dotenv()
client = discord.Client()

logging.basicConfig(
    format="%(asctime)s [%(levelname)s]: %(message)s", level=logging.INFO
)


@client.event
async def on_ready():
    logging.info(f"successfully logged in as {client.user}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--token", help="specify a Discord bot token")
    args = parser.parse_args()
    token: Optional[str] = args.token or os.getenv("DISCORD_TOKEN")
    if not token:
        logging.error("no token specified, use --token or set DISCORD_TOKEN")
        sys.exit(1)

    client.run(token)
