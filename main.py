import sys
import discord
from discord.ext import commands
import logging
import logging.handlers
from config.checks import *
from config.bot_globals import *

"""set up logger """
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

""" initilize bot """
bot = commands.Bot(command_prefix="&", pm_help=False)

""" events """

@bot.event
async def on_ready():
    log_print("[RESUME] Bot resumed connection.")
    log_print("------------------------STATUS------------------------")
    log_print("Ispyra {0} by Ispira using discord.py by Rapptz"
    .format(version))

    log_print("Contributors: {0}"
    .format(' '.join(contributors)))

    log_print("Logged in as: {0}"
    .format(bot.user.name))

    log_print("With ID: {0}"
    .format(bot.user.id))

    log_print("Botmasters: {0}"
    .format(', '.join(bot_masters)))

    log_print("Connected to:")
    for serv in bot.servers:
        log_print("{0},".format(serv.name))
        server_list.append(serv)

    log_print("------------------------STATUS------------------------")

@bot.event
async def on_message():
    pass

@bot.event
async def on_command():
    pass

@bot.event
async def on_server_join(server):
    pass

@bot.event
async def on_server_remove(server):
    pass

@bot.event
async def on_server_update(server):
    pass

@bot.command()
@allowed()
@is_owner()
async def shutdown():
    await bot.say('goodbye')
    await bot.logout()
    bot.close()


def main():
    bot.connect()
    bot.login(bot_token)
