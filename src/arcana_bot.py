import discord
import os
from discord.ext import commands
import cards
import deck
import player
import game

TOKEN = os.environ.get('BOT_TOKEN')

client = discord.Client()
intents = discord.Intents.default()
intents.members = True
description = "The Abyss speaks to you through the Saen'dal Arcana."

bot = commands.Bot(command_prefix='/', description=description, intents=intents)
# @bot.command()
# async def newgame(ctx):
#     thisGame = game.GameClass()
#     thisGame.reset()
#     thisGame.addPlayer(ctx.author)
#     await ctx.send(thisGame.getPlayers())

@client.event
async def on_ready():
    print("{0.user} is online!".format(client))

@client.event
async def on_message(message):
    # if message.author == client.user:
    #     return
    if message.content.startswith("!hello") or message.content.startswith("/hello"):
        await message.channel.send("Hello from the other side!")

bot.run(TOKEN)