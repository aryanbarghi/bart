import os
import discord
from discord.ext import commands
# from dotenv import load_dotenv

# in a real life scenario i'd use an environmental variable but for simplicity we're using a literal
TOKEN = 'NzEwNTc1MjM2OTA2NDgzNzk1.Xr2cwg.8HkeYWe9vCJgStcbpa2eeIzms1c'

# use $ as the prefix for bot commands
bot = commands.Bot(command_prefix="$")

@bot.command
async def load(ctx, extension):
    print(f'**********\nLoading\n**********')
    bot.load_extension(f'cogs.{extension}')

@bot.command
async def unload(ctx, extension):
    print(f'**********\nUnloading\n**********')
    bot.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(TOKEN)
