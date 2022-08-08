import os

import discord
from dotenv import load_dotenv
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
TOKEN = os.environ.get("DISCORD_TOKEN")

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

print(TOKEN)

#client.run(TOKEN)
