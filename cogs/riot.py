import discord
from discord.ext import commands
from riotwatcher import LolWatcher

class riot(commands.Cog):

    def __init__(self, client):
        self.client = client

    # ranked league of legends info
    @commands.command(name='league', help='Display LoL ranked summoner information.')
    async def league(self, ctx, arg):
        api_key = "RGAPI-f8134b51-7fab-4544-975e-545e2f28c046"  # pulled directly from the riot api developer website
        watcher = LolWatcher(api_key)

        embed = discord.Embed(title='League of Legends', description=f"Ranked Summoner Information for {arg}")

        # retrieves player info
        playerinfo = watcher.summoner.by_name('na1', arg)
        rankinfo = watcher.league.by_summoner('na1', playerinfo['id'])

        rank = (rankinfo[0]).get('tier') + " " + (rankinfo[0]).get('rank')
        lp = (rankinfo[0]).get('lp')
        wins = (rankinfo[0]).get('wins')
        losses = (rankinfo[0]).get('losses')

        embed.add_field(name='Current Rank', value=rank)
        embed.add_field(name='LP', value=lp)
        embed.add_field(name='Wins', value=wins)
        embed.add_field(name='Losses', value=losses)

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(riot(client))
