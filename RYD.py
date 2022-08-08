from discord.ext import commands


client = commands.Bot(
    command_prefix='!',
    help_command=None
)


@client.command()
async def hello(ctx):
    await ctx.send('Hello!')


client.run(
    'MTAwNDU0NjI3MTU4OTE3NTM2OA.G4vmQL.XNO4DrHD1NeW8UKBT2z4cSg1FWzG9JuD-01zWM'
)
