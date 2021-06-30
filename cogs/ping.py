import discord
from discord.ext import commands
import datetime
import random

class HelpfulCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx, *, member: discord.Member=None):
      member = ctx.author
      embed = discord.Embed(title="**Ping**", description=f":ping_pong: Pong! {round(self.client.latency*1000)}ms")
      embed.set_thumbnail(url=f"{member.avatar_url}")
      embed.timestamp = datetime.datetime.utcnow()
      await ctx.send(embed=embed)

def setup(client):
    client.add_cog(HelpfulCommands(client))