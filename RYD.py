import os

import discord
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
# TOKEN = os.getenv('DISCORD_TOKEN')[1:-1]
TOKEN = "MTAwNDU0NjI3MTU4OTE3NTM2OA.GdNQ4G.-4juxLTTu9esTO0oPdg9g5HyyCnYcrmFTc33Tk"

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

print(TOKEN)
# ssh -i C:\Users\crist\Desktop\RYD\RYD-keypair.pem ubuntu@ec2-3-95-207-0.compute-1.amazonaws.com

client.run(TOKEN)
