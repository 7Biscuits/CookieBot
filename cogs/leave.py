import discord 
from discord.ext import commands
import datetime

class Leave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def leave(self, ctx, *, reason='No reason provided'):
        member = ctx.author
        embed = discord.Embed(
            title="Member left ",
            description=f"{member.name} has left the server, Reason: {reason}",
            colour=discord.Colour.red(),
            )
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.timestamp = datetime.datetime.utcnow()
        await member.kick(reason=reason)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Leave(bot))
