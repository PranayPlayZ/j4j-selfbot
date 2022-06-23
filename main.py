import os
os.system("pip install -U git+https://github.com/dropout1337/Discord-iOS/")
import discord_ios
import discord
import random
import json
import sys
import asyncio
from discord.ext import commands
from flask import Flask
import threading

def clear():
  if sys.platform in ["linux", "linux2", "darwin"] or os.name == "posix":
    os.system("clear")
  else:
    os.system("cls")

clear()

with open('config.json') as config_file:
  config = json.load(config_file)

guild = config['Server_ID']
cs = config['Channel_Names']
cmsgs = config['Channel_Messages']
dmsgs = config['Dm_Messages']
tym = config['Delay']
emoji = config['Status_Emoji']
tex = config['Status_Type']
seggs = config['Success_Message']
ok_ = config['247_Hosting']
lowertext = tex.lower()

app = Flask(__name__)


@app.route('/')
def main():
    return "KaramveerPlayZ#1337 | J4J Bot 24/7 Hosting Api Link"

def start():
    app.run(host='0.0.0.0',port=8080)

if ok_ == True:
  threading.Thread(target=start, args=()).start()

bot = discord.Client(loop=asyncio.AbstractEventLoop)
bot = commands.Bot(command_prefix="karamveerplayz-j4j-bot", intents=discord.Intents.all(), help_command=None, self_bot=True)

@bot.event
async def on_ready():
  os.system("title J4J Bot - [KaramveerPlayZ#1337]")
  print(f"Connected to: {bot.user}\nCreated By KaramveerPlayZ!\n")
  if lowertext == "idle":
    await bot.change_presence(activity=discord.CustomActivity(name=None, emoji=emoji), status=discord.Status.idle)
  elif lowertext == "dnd":
    await bot.change_presence(activity=discord.CustomActivity(name=None, emoji=emoji), status=discord.Status.dnd)
  elif lowertext == "online":
    await bot.change_presence(activity=discord.CustomActivity(name=None, emoji=emoji), status=discord.Status.online)

@bot.listen("on_ready")
async def ready_even():
  os.remove("database.json")
  with open('database.json', 'a+') as f:
    f.write("""{
  "alog": []
}""")

@bot.event
async def on_connect():
  g = bot.get_guild(int(guild))
  while True:
    try:
      for channel in g.channels:
        for chh in cs:
          if chh in channel.name:
            async with channel.typing():
              await asyncio.sleep(5)
              msg = random.choice(cmsgs)
              await channel.send(msg)
              print(f"[$] Successfully Sent {msg} To {channel.name}")
              await asyncio.sleep(tym)
    except:
      await asyncio.sleep(6)
      continue

@bot.event
async def on_message(message):
  if message.author.id != bot.user.id:
    if message.guild == None:
      with open('database.json') as f:
        alogg = json.load(f)
      if str(message.author.id) in alogg['alog']:
        return
      if message.author.bot:
        return
      else:
        with open('database.json', 'r') as f:
          jsonn = json.load(f)
        jsonn['alog'].append(str(message.author.id))
        with open('database.json', 'w') as f:
          json.dump(jsonn, f, indent=4)
        async with message.channel.typing():
          await asyncio.sleep(5)
          msgg = random.choice(dmsgs)
          await message.channel.send(msgg)
          await asyncio.sleep(8)
          await message.channel.send(random.choice(seggs))
          print(f"[$] Successfully Sent {msgg} To {message.author}")
  await bot.process_commands(message)

bot.run(config["Token"], bot=False, reconnect=True)