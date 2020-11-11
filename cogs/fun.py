import discord
from discord.ext import commands
import random

class fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    # command: bonK!!!11
    @commands.command(name='bonk', help='BONK')
    async def ping(self, ctx):
        await ctx.send(file=discord.File('bonk/mike.PNG'))

def setup(client):
    client.add_cog(fun(client))
