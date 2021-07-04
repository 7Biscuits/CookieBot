import discord
from discord.ext import commands


class ModCommands(commands.Cog):
    def __init__(self, bot):
        bot.client = bot

    @commands.command(aliases=['nick','nickname','cnick'], pass_context=True)
    @commands.has_permissions(administrator=True)
    async def changenickname(self, ctx, member: discord.Member = None, *, nick=None):
        if member != None and nick != None:
            await member.edit(nick=nick)
            await ctx.send(f'Nickname was changed for {member.name} ')

        elif member == None:
            await ctx.send(
                f'{ctx.author.mention} you forgot to provide a member')

        elif nick == None:
            await ctx.send(
                f'{ctx.author.mention} you forgot to provide a nick name')

        elif member == None and nick == None:
            await ctx.send(
                f'{ctx.author.mention} you forgot to provide a member and a nick name'
            )


def setup(bot):
  bot.add_cog(ModCommands(bot))
