import discord
from discord.ext import commands

# Credentials

TOKEN = "OTcyOTUzODkwNzQ2MTQ2ODc2.GtqFHT.Bn0RHuR--MkUCBa2-XrSTvy4w1KJYu8kE1fp98"

# Create Bot

client = commands.Bot(command_prefix = "!")

# On Start

@client.event
async def on_ready():
    print(" Connected to bot: {}".format(client.user.name))
    print(" Bot ID: {}".format(client.user.id)) 


@client.command()
async def sus(ctx):
    await ctx.send("sus")

@client.command()
async def whosesus(ctx):
    await ctx.send("You're SUS")


# Run the Bot

client.run(TOKEN)