import os

import discord
from dotenv import load_dotenv, find_dotenv


client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('your token here')
# ssh -i C:\Users\crist\Desktop\RYD\RYD-keypair.pem ubuntu@ec2-3-95-207-0.compute-1.amazonaws.com
