import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


client.run('MTAwNDU0NjI3MTU4OTE3NTM2OA.Go3Ebo.Jp90AwpUPCTPwMXoTPBHE29YonirY71xqoXvg0')
