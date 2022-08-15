from datetime import datetime
import pytz

"""
#####################################################################
######################### ELISA'S FUNCTIONS #########################
#####################################################################
"""


async def status_command(ctx):
    print("\n\n")
    now = datetime.now(pytz.timezone("Chile/Continental")).strftime("%d-%m-%Y %H:%M:%S")
    print(now, " --> Status command begins...")
    print("\n")

    await ctx.channel.send("Elisa, Cristobal is developing all the back-end of my functionalities. That means he's "
                           "working on my database and also coding some functions. \n\nIf you want to learn more about"
                           "how I'll being working, please ask him. It's difficult to explain in a message.")

    return None

