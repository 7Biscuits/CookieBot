import discord
from discord.ext import commands


class ModCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, *, member: discord.Member, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"{member} has been banned.")

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
          await ctx.send(f"{ctx.auhtor.mention} You don't Have permission to use this command")

def setup(bot):
    bot.add_cog(ModCommands(bot))