import discord
from discord.ext import commands

class Demo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        print("HERE")
        await ctx.send('Pong!')