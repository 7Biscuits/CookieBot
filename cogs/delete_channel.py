import discord
from discord.ext import commands

class ModCommands(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  @commands.has_permissions(manage_channels=True)
  async def deletechannel(self, ctx, *, channel: discord.TextChannel=None):
    if channel is not None:
      await channel.delete()
      embed = discord.Embed(
                title="Text Channel deleted",
                description=f'{channel} has been deleted',
                colour=discord.Colour.red()
            )
      embed.add_field(name="Channel: ", value=f'{channel}')
      embed.add_field(name='Moderator: ', value=f'{ctx.author.name}')
      embed.set_thumbnail(url=f"{ctx.author.avatar_url}")
      await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(ModCommands(bot))
