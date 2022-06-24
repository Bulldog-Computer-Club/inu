#!/usr/bin/env python3

import argparse
import logging
import os
from pydoc import cli
import sys
from typing import Optional
from cogs.demo import Demo

import discord
import dotenv
from discord.ext import commands

dotenv.load_dotenv()
client = commands.Bot(command_prefix='!')

logging.basicConfig(
    format="%(asctime)s [%(levelname)s]: %(message)s", level=logging.INFO
)


@client.event
async def on_ready():
    logging.info(f"successfully logged in as {client.user}")

    # Add demo cog
    await client.add_cog(Demo(client))
    print("Added demo cog")

@client.event
async def on_message(message):
    print(message.content)
    print('HERE')
    # Execute command
    await client.process_commands(message)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--token", help="specify a Discord bot token")
    parser.add_argument("--debug", help="set the debug loglevel", action="store_true")
    parser.add_argument(
        "--quiet", help="silence everything except errors", action="store_true"
    )
    args = parser.parse_args()
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)
    elif args.quiet:
        logging.getLogger().setLevel(logging.ERROR)

    token: Optional[str] = args.token or os.getenv("DISCORD_TOKEN")
    if not token:
        logging.error("no token specified, use --token or set DISCORD_TOKEN")
        sys.exit(1)

    client.run(token)


