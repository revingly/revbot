import asyncio
import discord
from config.config import config

bot = discord.Client()

first_time = True

@bot.async_event
async def on_ready():
    data = []
    user_token = input()
    print(user_token)
    data.append(user_token)
    user_id = input()
    print(user_id)
    data.append(user_id)
    print(data)
    config.writeCredentials(data)
    print(first_time)
    print('connected!')


async def say_hi(author, message):
    print('saying hi')
    await bot.send_message(message.channel, "Hi! %s" % author)

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
