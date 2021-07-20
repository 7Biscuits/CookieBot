import discord
from discord.ext import commands
import datetime

class ModCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['createtextchannel', 'createtxtch', 'ctextch', 'addtextch])
    @commands.has_permissions(manage_channels=True)
    async def addtextchannel(self, ctx, channel=None):
        if channel is not None:
            await ctx.guild.create_text_channel(name='{}'.format(channel))
            embed = discord.Embed(
                title="New text channel created",
                description=f'{channel} has been created',
                colour=discord.Colour.green()
            )
            embed.add_field(name="Channel: ", value=f'{channel}')
            embed.add_field(name='Moderator: ', value=f'{ctx.author.name}')
            embed.set_thumbnail(url=f"{ctx.author.avatar_url}")
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(ModCommands(bot))
