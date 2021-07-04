import discord
from discord.ext import commands

class Text(commands.Cog):
  def __init__(self, bot):
    self.bot= bot
  
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def echo(self, ctx, *, message):
    await ctx.message.delete()
    await ctx.send(message)

  @echo.error
  async def echo_error(self, ctx, error):
    if isinstance(error, commands.MissingPermissions):
      await ctx.send(f"{ctx.author.mention} You don't Have permission to use this command")

def setup(bot):
  bot.add_cog(Text(bot))