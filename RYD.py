import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


client.run('MTAwNDU0NjI3MTU4OTE3NTM2OA.G4vmQL.XNO4DrHD1NeW8UKBT2z4cSg1FWzG9JuD-01zWM')
