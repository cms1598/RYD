from datetime import datetime
import pytz
import psycopg2

"""
#####################################################################
######################### TESTING FUNCTIONS #########################
#####################################################################
"""


async def test_command(ctx):
    print("\n\n")
    now = datetime.now(pytz.timezone("Chile/Continental")).strftime("%d-%m-%Y %H:%M:%S")
    print(now, " --> Test command begins...")

    member = ctx.author
    print("command author: ", member)

    guild = ctx.guild
    channel = ctx.channel
    print("command guild: ", guild, ", channel: ", channel)

    await channel.send("Please, check your terminal. The info should be there.")

    print("\n")
    return None


async def test_db(ctx, password):
    print("\n\n")
    now = datetime.now(pytz.timezone("Chile/Continental")).strftime("%d-%m-%Y %H:%M:%S")
    print(now, " --> Database test command begins...")

    conn = psycopg2.connect(database='ryd', user='ryd', password=password, host='3.95.207.0', port='5432')
    cursor = conn.cursor()
    cursor.execute("select version()")
    data = cursor.fetchone()

    await ctx.send(data)

    conn.close()
    print("\n")
    return None

