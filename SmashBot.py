import discord
import logging
import json
from discord.ext import commands


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
async def sus(ctx, arg):
    await ctx.send(f'{arg} is sus')

@bot.command()
async def play(ctx, cmd):
    await bot.load_extension(cmd)

@bot.command()
async def chkcmd(ctx, cmd):
    command = discord.utils.find(lambda comm: str(comm) == cmd, bot.commands) 
    if command:
        await ctx.send("Command Found")
    else:
        await ctx.send("Command Not Found")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    print(message)
    await bot.process_commands(message)

# Executing the bot

def main():
    TOKENFILE = "token-config.json"

    with open(TOKENFILE, 'r') as infile:
        config = json.load(infile)

    bot.run(config['token'], log_handler=handler)

if __name__ == '__main__':
    main()
