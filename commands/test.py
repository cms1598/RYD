import discord

"""
#####################################################################
######################### TESTING FUNCTIONS #########################
#####################################################################
"""


async def test_command(ctx):
    print("Test command begins...")

    member = ctx.author
    print("command author: ", member)

    guild = ctx.guild
    channel = ctx.channel
    print("command guild: ", guild, ", channel: ", channel)

    await channel.send("Please, check your terminal. The info should be there.")

    return None

