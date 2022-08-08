import os

import discord
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

# print(TOKEN)
# ssh -i C:\Users\crist\Desktop\RYD\RYD-keypair.pem ubuntu@ec2-3-95-207-0.compute-1.amazonaws.com

client.run(TOKEN)
