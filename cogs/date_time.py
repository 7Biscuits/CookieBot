import discord
from discord.ext import commands
import datetime

class TimeCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def time(self, ctx):
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        embed = discord.Embed(title='Time', description=f'current time a greenwich meridian: {current_time}', colour=discord.Colour.purple())
        await ctx.send(embed=embed)

    @commands.command()
    async def date(self, ctx):
        now = datetime.datetime.now()
        date = now.strftime('%d')
        month = now.strftime('%m')
        year = now.strftime('%Y')

        embed = discord.Embed(
            title="Today's date",
            colour=discord.Colour.blue()
            )
        embed.add_field(name="Date: ", value=f'{date}')
        embed.add_field(name="Month: ", value=f"{month}")
        embed.add_field(name="Year: ", value=f'{year}')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(TimeCommands(bot))
        
