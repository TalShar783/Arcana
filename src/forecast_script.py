import discord
import os
from discord.ext import commands
import random
import cards
import deck
import player
import game
import mytoken
import sys

TOKEN = mytoken.token
debugEnabled = True

description = '''A more lightweight bot that just runs the forecast script. Meant to be used with a Task Scheduler.'''

intents = discord.Intents.all()

dummyGame = game.GameClass("dummyGame")

prefix = '/'

bot = commands.Bot(command_prefix=prefix, description=description, intents=intents)

explainEmoji = "❓"
subscribedChannels =[950437219859071067, 951182029242900530]

# casting-fate: 950437219859071067
# beta_testing: 951182029242900530
# bot-testing: 950459698870628372



def debug(message):
    if debugEnabled == True:
        print(message)

async def embedCardExplain(ctx, card: cards.CardClass):
    color = houseColor(card.getHouse())
    await ctx.send(embed=sendEmbed(f"**{card.show()}**", "", card.explain(), color))


async def embedCardShow(ctx, card: cards.CardClass):
    color = houseColor(card.getHouse())
    msg = await ctx.send(embed=sendEmbed(f"**{card.show()}**", "", "", color))
    await msg.add_reaction("❓")


def sendCardEmbed(card: cards.CardClass):
    color = houseColor(card.getHouse())
    embed = discord.Embed(title=card.show(), url="", description=card.explain(), color=color)
    return embed


def sendEmbed(title: str, url: str, description: str, color):
    embed = discord.Embed(title=title, url=url, description=description, color=color)
    return embed


def houseColor(house):
    switcher = {
        "Darkness": discord.Colour.purple(),
        "Light": discord.Colour.gold(),
        "Fire": discord.Colour.red(),
        "Ice": discord.Colour.blue(),
        "Unaligned": discord.Colour.dark_gray()
    }
    return switcher.get(house)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    for c in subscribedChannels:
        await forecast(bot.get_channel(c))
    sys.exit()



async def forecast(c):
    await c.send("Good morning! I bear tidings from the starry abyss concerning your fate today.")
    await c.send(f"Your forecast for the morning: ")
    debug(f"Drawing morning forecast...")
    drawnCard = dummyGame.deck.drawCard()
    if drawnCard.n == "Error" or not isinstance(drawnCard, cards.CardClass):
        await c.send("Error: No card found!")
    else:
        await embedCardShow(c, drawnCard)
    await c.send(f"Your forecast for the afternoon: ")
    debug(f"Drawing afternoon forecast...")
    drawnCard = dummyGame.deck.drawCard()
    if drawnCard.n == "Error" or not isinstance(drawnCard, cards.CardClass):
        await c.send("Error: No card found!")
    else:
        await embedCardShow(c, drawnCard)
    await c.send(f"Your forecast for the evening: ")
    debug(f"Drawing evening forecast...")
    drawnCard = dummyGame.deck.drawCard()
    if drawnCard.n == "Error" or not isinstance(drawnCard, cards.CardClass):
        await c.send("Error: No card found!")
    else:
        await embedCardShow(c, drawnCard)
    dummyGame.reset()

bot.run(TOKEN)
