import discord
from discord.ext import commands
import datetime

class ModCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def textch(self, ctx, channel: discord.TextChannel=None):
        if channel is not None:
            await ctx.guild.create_text_channel(channel=channel)
            embed = discord.Embed(
                title="New channel created",
                description=f'{channel} has been created',
                colour=discord.Colour.green()
            )
            embed.add_field(name="Channel: ", value=f'{channel.mention}')
            embed.add_field(name='Moderator: ', value=f'{ctx.author.name}')
            embed.set_thumbnail(url=f"{ctx.author.avatar_url}")

def setup(bot):
    bot.add_cog(ModCommands(bot))
