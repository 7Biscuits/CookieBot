import discord
from discord.ext import commands
import json
import aiohttp

class NumFact(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['number'])
    async def numberfact(self, ctx, number: int):

        if not number:
            await ctx.send(f'{ctx.author.mention} Listen idiot, You have to type the number to get the fact about it -_-')
            return
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'http://numbersapi.com/{number}?json') as resp:
                    file = json.loads(await resp.read())
                    fact = file['text']
                    await ctx.send(f"**Did you know?**\n*{fact}*")
        except KeyError:
            await ctx.send("No facts are available for that number.")

def setup(bot):
  bot.add_cog(NumFact(bot))