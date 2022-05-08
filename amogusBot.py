import discord
from discord.ext import commands

# Credentials

TOKEN = "OTcyOTUzODkwNzQ2MTQ2ODc2.GwXdcC.7CsNQtPt3bBhK6e6eje30CH2f6oqLIm7_8ryoY"

# Create Bot

client = commands.Bot(commands_prefix = "!")

@client.command()
async def sussybaka(ctx):
    ctx.send("sus")
