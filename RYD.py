import os
from dotenv import load_dotenv, find_dotenv
import discord
from discord.ext import commands, tasks

from commands.test import test_command

load_dotenv(find_dotenv())

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


@bot.command(name='test', aliases=['t'], help='Saludo de RYD')
async def on_message(ctx):
    await test_command(ctx)


TOKEN = os.getenv("DISCORD_TOKEN")

bot.run(TOKEN)
