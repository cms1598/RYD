import os
from dotenv import load_dotenv, find_dotenv
import discord
from discord.ext import commands, tasks

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


@bot.command(name='hello', aliases=['hi', 'hola'], help='Saludo de RYD')
async def on_message(message):
    await message.channel.send('Hola Elisa y Cristobal! Soy RYD, el nuevo secretario de Cristobal. Por ahora solo '
                               'existo, espero pronto tener todas mis funciones.')


TOKEN = os.getenv("DISCORD_TOKEN")

bot.run(TOKEN)
