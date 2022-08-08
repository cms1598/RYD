import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


client.run('MTAwNDU0NjI3MTU4OTE3NTM2OA.GT7dcd.LVHaG0llpXhpVPjfhsQdydl79aQI-6vNZfsWRs')
