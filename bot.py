#!/usr/bin/env python3

import argparse
import asyncio
import logging
import os
import sys
from typing import Optional

import discord
import dotenv
from discord.ext import commands

dotenv.load_dotenv()

logging.basicConfig(
    format="%(asctime)s [%(levelname)s]: %(message)s", level=logging.INFO
)

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready():
    logging.info(f"successfully logged in as {bot.user}")


@bot.event
async def on_message(msg: discord.Message):
    await bot.process_commands(msg)


initial_exts = ["cogs.demo"]


async def main():
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

    async with bot:
        for ext in initial_exts:
            await bot.load_extension(ext)
        await bot.start(token)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
