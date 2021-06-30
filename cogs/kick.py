import discord
from discord.ext import commands


class ModCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"{member} has been kicked.")

    @kick.error
    async def ban_error(self, ctx, error):
      if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.auhtor.mention} You don't Have permission to use this command")

def setup(client):
    client.add_cog(ModCommands(client))