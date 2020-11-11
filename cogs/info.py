import discord
from discord.ext import commands
import random

class info(commands.Cog):

    def __init__(self, client):
        self.client = client

    # event: upon connecting with discord server
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged into Discord as {self.client.user.name} (ID: {self.client.user.id})!')

    # event: upon member connection establish
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} has joined the server!')

    #event - a member has left
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left the server.')

    # command: check latency
    @commands.command(name='ping', help='Returns the current latency in ms.')
    async def ping(self, ctx):
        await ctx.send(f'Pong! Latency is {self.client.latency*1000}ms.')

    # command: clear chat history
    @commands.command(name='clear', help='Clears x amount of previous messages.')
    async def clear(self, ctx, arg):
        if not arg.isnumeric():
            await ctx.send("Incorrect input! Please enter a valid [positive] integer to specify the number of previous messages you would like to remove.")

        await ctx.channel.purge(limit=int(arg))

    # command: kick player
    @commands.command(name='kick', help='Kicks specified player.')
    async def kick(self, ctx, member : discord.Member, *, reason = None):
        await member.kick(reason = reason)

def setup(client):
    client.add_cog(info(client))