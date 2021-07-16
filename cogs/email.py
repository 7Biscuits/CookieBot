import discord
from discord.ext import commands
import datetime
import random
import smtplib, ssl 
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.multipart import MIMEMultipart
import os

class HelpfulCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def email(self, ctx, email, *,message):
      sender = 'cookiebotofficial@gmail.com'
      receiver = email
      bodySend = message
      msg = MIMEText(bodySend, 'html')
      msg['Subject'] = 'Hi! I am Cookie'
      msg['From'] = sender
      msg['To'] = receiver
      s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
      s.login(user = sender, password = os.environ('GMAILPASS'))
      s.sendmail(sender, receiver, msg.as_string())
      s.quit()


def setup(client):
    client.add_cog(HelpfulCommands(client))
