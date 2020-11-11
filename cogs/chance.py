import discord
from discord.ext import commands
import random

class chance(commands.Cog):

    def __init__(self, client):
        self.client = client

    # rolls xdy dice where x is number of dice to be rolled with y sides
    @commands.command(name='rolldice', help='Rolls x dice with y amount of sides. Use format xdy')
    async def rolldice(self, ctx, arg):

        embed = discord.Embed(title='Dice Roll(s)', description=f"{ctx.author.mention}")

        # error checking
        if not (arg[:1]).isnumeric() or (arg[1:2]) != 'd' or not (arg[2:]).isnumeric():
            embed.add_field(name=f'noOOope', value=f"This is not a valid input! Use the format xdy where x is the number of dice to be rolled and y is the number of sides per die.")
            return
        else:
            numofdice, numofsides = arg.split('d')  # ignore the d and split into two variables
            total = 0

            # output the die numbers
            for x in range(0, int(numofdice)):
                rolled = random.randint(1, int(numofsides))
                # await ctx.send('Die ' + str(x+1) + ' = ' + str(rolled))
                embed.add_field(name = f'Die {str(x+1)}:', value = f'{str(rolled)}')
                total += rolled

            # await ctx.send('Total = ' + str(total))
            await ctx.send(embed = embed)

    # heads or tails?
    @commands.command(name='cointoss', help='Flip a coin.')
    async def cointoss(self, ctx):
        embed = discord.Embed(title='Coin Tosssssss', description=f"{ctx.author.mention}")
        tossed = random.randint(0, 1)
        if tossed == 0:
            embed.add_field(name = 'bing!', value = 'Heads!')
        elif tossed == 1:
            embed.add_field(name = 'ding!', value = 'Tails!')
        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(chance(client))
