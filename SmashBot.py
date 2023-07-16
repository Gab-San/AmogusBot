import discord
import logging
from discord.ext import commands

<<<<<<< HEAD:SmashBot.py
import Games.Tris as tris
=======
>>>>>>> b27e6619cdb8bcf8b1f62343763b36b7c1e499b4:SmashBot

# Setting up log handler. This will save log entries on discord.log file

handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode='w')

intents = discord.Intents.default()
intents.message_content=True

# Gets the bot object from discord.py

bot = commands.Bot(command_prefix='?', intents=intents, status=discord.Status.idle)


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!'
          f'\n\nClient Name: {bot.user.name}'
          f'\nClient ID: {bot.user.id} and Discriminator: {bot.user.discriminator}'
          f'\n\nVerified: {bot.user.verified}'
          f'\nCreated: {bot.user.created_at}\n')


@bot.command()
async def test(ctx):
    await ctx.send("Test")

@bot.command()
async def sus(ctx, arg):
    await ctx.send(f'{arg} is sus')


# Executing the bot

bot.run(DISCORD_TOKEN, log_handler=handler)