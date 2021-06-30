import discord
from discord.ext import commands
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.client = bot

    @commands.command()
    async def pp(self, ctx, *, member: discord.Member=None):
        pps = ['8=D', '8==D', '8===D', '8====D', '8=====D', '8======D', '8=======D', '8========D', '8============D', "You don't have pp"]
        res = random.choice(pps)
        if member == None:
            member = ctx.author

        embed = discord.Embed(title=f"{member.name}'s pp size:")
        embed.set_footer(text=f"{res}")

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Fun(bot))