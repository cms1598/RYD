from datetime import datetime

"""
#####################################################################
######################### TESTING FUNCTIONS #########################
#####################################################################
"""


async def test_command(ctx):
    print("\n\n")
    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    print(now, " --> Test command begins...")

    member = ctx.author
    print("command author: ", member)

    guild = ctx.guild
    channel = ctx.channel
    print("command guild: ", guild, ", channel: ", channel)

    await channel.send("Please, check your terminal. The info should be there.")

    print("\n")
    return None
