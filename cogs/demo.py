from discord.ext import commands
import discord
import asyncio


class DemoCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send("Pong!")

    @commands.command()
    async def embed(self, ctx: commands.Context, title: str, desc: str):
        # if the title or desc is empty, send a message saying its empty
        if not title or not desc:
            await ctx.send("Title or description is empty!")
            return

        # create a discord embed with the first arg being its title, and the rest concatenated for its content
        embed = discord.Embed(title=title, description=desc)

        # send the embed
        await ctx.send(embed=embed)

    @commands.command()
    async def reaction(self, ctx: commands.Context, emoji: str):

        try:
            await ctx.message.add_reaction(emoji);
        except discord.HTTPException as e:
            await ctx.send(e)

    @commands.command()
    async def clear(self, ctx: commands.Context, amount: int):
        await ctx.channel.purge(limit=amount + 1)
        msg = await ctx.send("Purged {} messages!".format(amount))

        await asyncio.sleep(1)
        await msg.delete()

    @commands.command()
    async def assign(self, ctx: commands.Context, role: discord.Role):
        await ctx.author.add_roles(role)
        await ctx.send("You have been assigned the role {}!".format(role.name))

    


async def setup(bot: commands.Bot):
    await bot.add_cog(DemoCog(bot))
