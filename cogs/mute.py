import discord
from discord.ext import commands
import datetime

class ModCommands(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(aliases=['m'])
  @commands.has_permissions(kick_members=True)
  async def mute(self, ctx, *, member: discord.Member=None, reason="No Reason Provided"):
    if member == None:
      await ctx.send(f'{ctx.auhtor.mention} Provide a member to mute')
    elif member != None:
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.add_roles(muted_role)
        embed = discord.Embed(
            colour=discord.Colour.red(),
            title='Member has been successfully muted',
            description=f'{member.name} has been successfully muted by {ctx.author.name}, Reason: {reason}'
            )
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
        await member.send(f"You have been muted in: {ctx.guild.name}, Reason: {reason}")

  @mute.error
  async def mute_error(self, ctx, error):
    if isinstance(error, commands.MissingPermissions):
      await ctx.send(f"{ctx.auhtor.mention} You don't Have permission to use this command")

def setup(bot):
  bot.add_cog(ModCommands(bot))