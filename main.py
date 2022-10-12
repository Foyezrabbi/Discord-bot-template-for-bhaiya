import discord
from discord.ext import commands
import asyncio
from datetime import datetime, timezone, timedelta

token = "123"
prefix = ['A!', "a!", "a/", "A/"]
intents = intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, intents=intents, help_command=None, case_insensitive=True)
bot.remove_command("help")


@bot.event
async def on_ready():
    print()
    print(f"""logged in as {bot.user}""")


@bot.event
async def on_member_join(member):
    print('working')
    await member.send("welcome")
    await asyncio.sleep(1)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Couldn't find that command you're looking for.", delete_after=5.0)
        await ctx.message.delete(delay=5)
        print(f"\nCommandNotFound\n{datetime.now(timezone(timedelta(hours=+3))).time()}")
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Command is on interserveral cooldown. Try again in {error.retry_after:0.1f} seconds.",
                       delete_after=5.0)
        await ctx.message.delete(delay=5)
        print(f"\nCommandOnCooldown\n{datetime.now(timezone(timedelta(hours=+3))).time()}")


bot.run(token, bot=True)
