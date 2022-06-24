from discord.ext import commands
import discord
import random


class DemoCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        """Check if the bot is online."""
        await ctx.send("Pong!")

    @commands.command()
    async def embed(self, ctx: commands.Context, title: str, desc: str):
        """Create a simple embed with a title and description."""
        embed = discord.Embed(title=title, description=desc)
        await ctx.send(embed=embed)

    @commands.command()
    async def react(self, ctx: commands.Context, emoji: str):
        """React with an emoji."""
        try:
            await ctx.message.add_reaction(emoji)
        except discord.HTTPException:
            await ctx.send("Not a valid emoji.")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx: commands.Context, amount: int):
        """Delete messages from the channel in bulk."""
        limit = amount + 1  # also delete triggering message
        if limit > 100:
            await ctx.send("The amount of messages to delete must be less than 100.")
        elif amount <= 0:
            await ctx.send("The amount of messages to delete must be greater than 0.")

        await ctx.channel.purge(limit=limit)
        msg = await ctx.send(f"Purged {amount} messages!")
        await msg.delete(delay=1)

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def assign(self, ctx: commands.Context, role: discord.Role):
        """Assign a role to yourself."""
        await ctx.author.add_roles(role)
        await ctx.send(f"You have been assigned the role {role.name}!")

    @commands.command()
    async def rps(self, ctx: commands.Context, choice: str):
        """Play rock-paper-scissors with the bot."""
        CHOICES = ("rock", "paper", "scissors")
        WINNING_PAIRS = (("rock", "scissors"), ("scissors", "paper"), ("paper", "rock"))

        user_choice = choice.lower()
        if user_choice in CHOICES:
            bot_choice = random.choice(CHOICES)
            if bot_choice == user_choice:
                await ctx.send(f"I chose {user_choice} too, so it appears we're tied!")
            elif (user_choice, bot_choice) in WINNING_PAIRS:
                await ctx.send(
                    f"You chose {user_choice}, which beats my choice of {bot_choice}, so it appears you win."
                )
            else:
                await ctx.send(
                    f"I chose {bot_choice}, and that beats your choice of {user_choice}. Good game!"
                )
        else:
            await ctx.send("Choose one of rock, paper, or scissors.")


async def setup(bot: commands.Bot):
    await bot.add_cog(DemoCog(bot))
