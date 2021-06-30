import discord
from discord.ext import commands


class ModCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['clean','cls','sweep'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount+1)


def setup(client):
    client.add_cog(ModCommands(client))