import asyncio
import discord
from config import config
bot = discord.Client()

@bot.async_event
async def on_ready():
     print('connected!')


async def say_hi(author, message):
    print('saying hi')
    await bot.send_message(message.channel, "Hi!")

@bot.async_event
async def on_message(message):
    author = message.author
    if message.author == bot.user:
              return
    if message.content.startswith('!hello'):
        #   func = message.content.lstrip('!')
        await say_hi(author, message)
    else:
      return
    #
    # if func == 'hello':
    #      await bot.send_message(message.channel, 'hoe gaat het?')
    # return



try:
    bot.run(config.token)
except:
    print('invalid token')
