import discord
from discord.ext import commands
import datetime

class ModCommands(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(aliases=['ub'])
  @commands.has_permissions(ban_members=True)
  async def unban(self, ctx, *, member=None):
    if member == None:
      await ctx.send(f'{ctx.author.mention} Provide a member to unban')
    elif member != None:
      banned_users = await ctx.guild.bans()
      member_name, member_discriminator = member.split('#')

      for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
          await ctx.guild.unban(user)
          embed = discord.Embed(
              colour=discord.Colour.green(),
              title='Member has been successfully unbanned',
              description=f'{member.name} has been successfully unbanned by {ctx.author.name}'
              )
          embed.timestamp = datetime.datetime.utcnow()
          await ctx.send(embed=embed)
          return
          
        else:
          await ctx.send(f'{ctx.author.mention} Member not found')

  @unban.error
  async def unban_error(self, ctx , error):
    if isinstance(error, commands.MissingPermissions):
      await ctx.send(f"{ctx.auhtor.mention} You don't Have permission to use this command")
          
def setup(bot):
  bot.add_cog(ModCommands(bot))

