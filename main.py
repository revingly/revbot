import discord
from discord.ext import commands
import sys
import logging

""" main code """

formatter = commands.HelpFormatter(show_check_failure=False)

bot = commands.Bot(command_prefix="&", formatter=formatter,pm_help=False)


@bot.event
async def on_ready():
    """
    return message when the bot is deployed and start working
    """
    print('bot is working')


@bot.event
async def on_command():
    """
    :return:
    """
    pass


@bot.event
async def on_message(command, ctx):
    if user_allowed(message):
        await bot.process_commands(message)


    """ commands error handling function"""
@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.MissingRequiredArgument):
        await send_cmd_help(ctx)
    elif isinstance(error, commands.BadArgument):
        await send_cmd_help
    elif isinstance(error, commands.DisabledCommand):
        await bot.send_message(ctx.channel, "command is disabled")
    elif isinstance(eror, commands.CommandInvokeError):
        logger.exception("Exception in command '{}'".format(
            ctx.command.qualified_name), exc_info=error.original)
        oneliner = "Error in command '{}' - {}: {}".format(
            ctx.command.qualified_name, type(error.original).__name__,
            str(error.original))
        await ctx.bot.send_message(ctx.message.channel, inline(oneliner))
    elif isinstance(error, commands.CommandNotFound):
        pass
    elif isinstance(error, commands.CheckFailure):
        pass
    else
        logger.exception(type(error).__name__, exc_info=error)

        """ commande for sending help text for a commande """
async def send_cmd_help(ctx):
    if ctx.invoked_subcommand:
        pages = bot.formatter.format_help_for(ctx, ctx.invoked_subcommand)
        for page in pages:
            await bot.send_message(ctx.message.channel, page)
    else:
        pages = bot.formatter.format_help_for(ctx, ctx.command)
        for page in pages:
            await bot.send_message(ctx.message.channel, page)

    """ check if the user is allowed to use commandes"""
def user_allowed(message):

    author = message.author

    mod = bot.get_cog('Mod')

    if mod is not None:
        if settings.owner == author.id:
            return True
        if not message.channel.is_private:
            server = message.server
            names = (settings.get_server_admin(
                server), settings.get_server_mod(server))
            results = map(
                lambda name: discord.utils.get(author.roles, name=name), names)
            for r in results:
                if r is not None:
                    return True

        if author.id in mod.blacklist_list:
            return False

        if mod.whitelist_list:
            if author.id not in mod.whitelist_list:
                return False

        if not message.channel.is_private:
            if message.server.id in mod.ignore_list["SERVERS"]:
                return False

            if message.channel.id in mod.ignore_list["CHANNELS"]:
                return False
        return True
    else:
        return True


def set_logger():
    global logger
    logger = logging.getLogger("discord")
    logger.setLevel(logging.WARNING)
    handler = logging.FileHandler(
        filename='data/red/discord.log', encoding='utf-8', mode='a')
    handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s %(module)s %(funcName)s %(lineno)d: '
        '%(message)s',
        datefmt="[%d/%m/%Y %H:%M]"))
    logger.addHandler(handler)

    logger = logging.getLogger("red")
    logger.setLevel(logging.INFO)

    red_format = logging.Formatter(
        '%(asctime)s %(levelname)s %(module)s %(funcName)s %(lineno)d: '
        '%(message)s',
        datefmt="[%d/%m/%Y %H:%M]")

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(red_format)
    stdout_handler.setLevel(logging.INFO)

    fhandler = logging.handlers.RotatingFileHandler(
        filename='data/red/red.log', encoding='utf-8', mode='a',
        maxBytes=10**7, backupCount=5)
    fhandler.setFormatter(red_format)

    logger.addHandler(fhandler)
    logger.addHandler(stdout_handler)



def main():
    global settings
    global checks

    set_logger()






