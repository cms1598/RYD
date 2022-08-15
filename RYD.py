import os
from dotenv import load_dotenv, find_dotenv
import discord
from discord.ext import commands, tasks

import commands.test as t
import commands.elisa as e

# -------------- Env variables --------------
load_dotenv(find_dotenv())

TOKEN = os.getenv("DISCORD_TOKEN")

# ---------------- Bot setup ----------------
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, (commands.CommandNotFound, commands.CheckFailure)):
        return


@bot.command(name='hello', aliases=['hi', 'hola'], help='RYD\'s greeting.')
async def on_message(ctx):
    await ctx.channel.send('Hi Elisa y Cristobal! I\'m RYD, Cristobal\'s new personal assistant. For a while '
                           'I\'m just living, hopefully I\'ll be with all my functions equipped soon.')


"""
#####################################################################
######################### TESTING FUNCTIONS #########################
#####################################################################
"""


@bot.command(name='test', aliases=['t'], help='Testing command. Looks for info and help to understand'
                                              'some behaviour')
async def test(ctx):
    await t.test_command(ctx)


"""
#####################################################################
######################### ELISA'S FUNCTIONS #########################
#####################################################################
"""


@bot.command(name='status', help='Status command. Tell Elisa what is my current status.')
@commands.has_any_role("Elisa")
async def status(ctx):
    await e.status_command(ctx)



bot.run(TOKEN)
