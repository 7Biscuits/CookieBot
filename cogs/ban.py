import discord
from discord.ext import commands
import datetime

class ModCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, *, member: discord.Member, reason=None):
        embed = discord.Embed(
            colour=discord.Colour.red(),
            title='Member has been successfully banned',
            description=f'{member.name} has been successfully banned by {ctx.author.name}, Reason: {reason}'
            )
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.timestamp = datetime.datetime.utcnow()
        await member.ban(reason=reason)
        await ctx.send(embed=embed)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
          await ctx.send(f"{ctx.auhtor.mention} You don't Have permission to use this command")

def setup(bot):
    bot.add_cog(ModCommands(bot))