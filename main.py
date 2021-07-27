import discord
from discord.ext import commands
import os
import datetime
import random
import asyncio
import requests
from keep_alive import keep_alive

bot = commands.Bot(command_prefix = 'c-')
#bot.remove_command('help')

@bot.event
async def on_ready():
  print("--------------------")
  print("Logged in as user")
  print(bot.user.name)
  print(bot.user.id)
  print("Ready To Eat Cookies")
  print("--------------------")
  await bot.change_presence(activity=discord.Streaming(name="Cookies Recipe", url="https://www.twitch.tv/rick_astley"))

snipe_message_author = {}
snipe_message_content = {}

@bot.event
async def on_message_delete(message):
    snipe_message_author[message.channel.id] = message.author
    snipe_message_content[message.channel.id] = message.content
    await asyncio.sleep(60)
    del snipe_message_author[message.channel.id]
    del snipe_message_content[message.channel.id]

@bot.command()
async def snipe(ctx):
    channel = ctx.channel
    try:
        em = discord.Embed(title=f"Sniped message #{channel.name}",
                           description=snipe_message_content[channel.id],
                           color=ctx.author.color)
        em.set_footer(text=f"Message sniped by {ctx.author.name}")
        await ctx.send(embed=em)
        del snipe_message_content[channel.id]
        del snipe_message_author[channel.id]

    except:
        await ctx.send(f"**There is nothing to snipe!**")

@bot.event
async def on_message(message):
  if message.content.startswith('c-guess'):
    answer = random.randint(1, 10)
    await message.channel.send(f'{message.author.mention} Guess a number between 1 and 10')

    def is_correct(m):
        return m.author == message.author and m.content.isdigit()

    try:
       guess = await bot.wait_for('message', check=is_correct, timeout=5.0)

    except asyncio.TimeoutError:
      await message.channel.send(f'{message.author.mention} You took too long too respond. The answer was {answer}')

    if int(guess.content) == answer:
      await message.channel.send(f'{message.author.mention} you guessed it right. the answer was {answer}')
    else:
      await message.channel.send(f'{message.author.mention} your answer is wrong. The correct answer is {answer}')
  await bot.process_commands(message)

@bot.command()
async def pressf(ctx, *, member: discord.Member=None, reason=None):
    if member != None:
      msg_ = await ctx.send(f"Everyone!! Let's pay our respects to {member.mention},Reason: {reason}, React on the message to pay your respect")
      #await msg_.add_reaction('<:F_:713427539313557594>')
      await msg_.add_reaction('<:red_cross:817435952943071302>')

      def check(reaction, user):
        #return msg.id == ctx.message.id and msg.reaction == "<:red_cross:817435952943071302>"
        return str(reaction.emoji) == '<:red_cross:817435952943071302>' and user != bot.user

      reaction, user = await bot.wait_for("reaction_add",check=check)
      await ctx.send(f'{user.mention} has paid their respect')
      return

    elif member == None:
      await ctx.send(f'{ctx.author.mention} Hey idiot, Mention the member you want to pay respect')


for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f"cogs.{filename[:-3]}")

keep_alive()
bot.run(os.environ['DISCORD_TOKEN'])
