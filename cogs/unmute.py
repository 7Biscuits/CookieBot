import discord
from discord.ext import commands
import datetime

class ModCommands(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(aliases=['um'])
  @commands.has_permissions(kick_members=True)
  async def unmute(self, ctx, *, member: discord.Member=None):
    if member == None:
      await ctx.send(f'{ctx.author.mention} Provide a member to unmute')
      
    elif member != None:
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(mutedRole)
        embed = discord.Embed(
            colour=discord.Colour.red(),
            title='Member has been successfully unmuted',
            description=f'{member.name} has been successfully unmuted by {ctx.author.name}'
            )
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
        await member.send(f'you have been unmuted from {ctx.guild.name}')

  @unmute.error
  async def unmute_error(self, ctx, error):
    if isinstance(error, commands.MissingPermissions):
      await ctx.send(f"{ctx.auhtor.mention} You don't Have permission to use this command")

def setup(bot):
  bot.add_cog(ModCommands(bot))