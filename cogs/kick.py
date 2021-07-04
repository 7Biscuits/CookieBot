import discord
from discord.ext import commands
import datetime

class ModCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member = None, *, reason='No reason provided'):
        if member != None:
            embed = discord.Embed(
                colour=discord.Colour.red(),
                title='Member has been successfully kicked',
                description=f'{member.name} has been successfully kicked by {ctx.author.name}, Reason: {reason}'
                )
            embed.set_thumbnail(url=f"{member.avatar_url}")
            embed.timestamp = datetime.datetime.utcnow()
            #await member.message.send(f'you have been kicked from {ctx.guild.name}, Reason: {reason}')
            await member.kick(reason=reason)
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"{ctx.author.mention} you didn't provide a member to be kicked")

    @kick.error
    async def ban_error(self, ctx, error):
      if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.auhtor.mention} You don't Have permission to use this command")

def setup(bot):
    bot.add_cog(ModCommands(bot))