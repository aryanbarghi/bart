import discord
from discord.ext import commands
import requests


class weather(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='weather', help='Displays current weather information of 5-digit zip code.')
    async def weather(self, ctx, arg):

        embed = discord.Embed(title='Weather', description=f"{ctx.author.mention}")

        if not (arg.isnumeric() and len(arg) == 5):
            embed.add_field(name=f'stop living in your fantasy world, this is real life',
                            value=f"This is not a valid zip code!")
        else:
            zipCode = arg
            API = "908b6bab23b7dc66f92948681f48692f"
            response = requests.get(
                f"http://api.openweathermap.org/data/2.5/weather?zip={zipCode},us&units=imperial&appid={API}")
            data = response.json()

            cityName = data.get('name')
            weatherConditionId = ((data["weather"])[0])["id"]

            def weatherDescription(argument):
                switcher = {
                    200: f"There is currently a thunderstorm with light rain happening in {cityName}.",
                    201: f"There is currently a thunderstorm with moderate rain happening in {cityName}.",
                    202: f"There is currently a thunderstorm with heavy rain happening in {cityName}.",
                    210: f"There is currently a light thunderstorm happening in {cityName}.",
                    211: f"There is currently a thunderstorm happening in {cityName}.",
                    212: f"There is currently a heavy thunderstorm happening in {cityName}.",
                    221: f"There is currently a ragged thunderstorm happening in {cityName}.",
                    230: f"There is currently a thunderstorm with light drizzle happening in {cityName}.",
                    231: f"There is currently a thunderstorm with moderate drizzle happening in {cityName}.",
                    232: f"There is currently a thunderstorm with heavy drizzle happening in {cityName}.",

                    300: f"There is currently a light drizzle in {cityName}.",
                    301: f"There is currently a moderate drizzle in {cityName}.",
                    302: f"There is currently a heavy drizzle in {cityName}.",
                    310: f"There is currently a light drizzle in {cityName}.",
                    311: f"There is currently a moderate drizzle in {cityName}.",
                    312: f"There is currently a heavy drizzle in {cityName}.",
                    313: f"There is currently a light drizzle in {cityName}.",
                    314: f"There is currently a moderate drizzle in {cityName}.",
                    321: f"There is currently a heavy drizzle in {cityName}.",

                    500: f"It's currently raining lightly in {cityName}.",
                    501: f"It's currently raining in {cityName}.",
                    502: f"It's currently raining heavily in {cityName}.",
                    503: f"It's currently raining very heavily in {cityName}.",
                    504: f"It's currently raining extremely heavily in {cityName}.",
                    511: f"There is currently freezing rain in {cityName}.",
                    520: f"There are currently light showers in {cityName}.",
                    521: f"There are currently showers in {cityName}.",
                    522: f"There are currently heavy showers in {cityName}.",
                    531: f"There are currently ragged showers in {cityName}.",

                    600: f"It's currently snowing lightly in {cityName}.",
                    601: f"It's currently snowing in {cityName}.",
                    602: f"It's currently snowing heavily in {cityName}.",
                    611: f"It's currently sleeting in {cityName}.",
                    612: f"There is currently a light shower sleet in {cityName}.",
                    613: f"There is currently a shower sleet in {cityName}.",
                    615: f"There is currently light rain and snow in {cityName}.",
                    616: f"There is currently rain and snow in {cityName}.",
                    620: f"There is currently a light shower of snow in {cityName}.",
                    621: f"There is currently a shower of snow in {cityName}.",
                    622: f"There is currently a heavy shower of snow in {cityName}.",

                    701: f"It's currently misting in {cityName}.",
                    711: f"There is currently smoke in {cityName}.",
                    721: f"There is currently haze in {cityName}.",
                    731: f"There is currently dust in {cityName}.",
                    741: f"It's currently foggy in {cityName}.",
                    751: f"It's currently sandy in {cityName}.",
                    761: f"It's currently dusty in {cityName}.",
                    762: f"There is currently ash in {cityName}.",
                    771: f"There is currently a squall in {cityName}.",
                    781: f"A tornado has been reported in {cityName}. Seek shelter immediately.",

                    800: f"It's currently clear in {cityName}.",

                    801: f"It's currently cloudy in {cityName}.",
                    802: f"It's currently cloudy in {cityName}.",
                    803: f"It's currently cloudy in {cityName}.",
                    804: f"There is currently an overcast in {cityName}.",
                }
                return switcher.get(weatherConditionId, "Invalid data.")

            await ctx.send("Welcome back! " + weatherDescription(weatherConditionId) + f" Expect temperatures between {(data.get('main')).get('temp_min')}°F and {(data.get('main')).get('temp_max')}°F.")

            embed = discord.Embed(title=f"{cityName} Weather Data", description=f"{ctx.author.mention}")

            temperature = (data.get('main')).get('temp')
            pressure = (data.get('main')).get('pressure')
            humidity = (data.get('main')).get('humidity')
            wind = f"{(data.get('wind')).get('speed')} mph @ {(data.get('wind')).get('deg')}°"
            clouds = (data.get('clouds')).get('all')

            embed.add_field(name='Current Temperature', value=f"{temperature} °F")
            embed.add_field(name='Atmospheric Pressure', value=f"{pressure} hPa")
            embed.add_field(name='Humidity', value=f"{humidity} %")
            embed.add_field(name='Wind', value=f"{wind}")
            embed.add_field(name='Cloudiness', value=f"{clouds} %")

            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(weather(client))