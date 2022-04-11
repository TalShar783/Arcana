import discord
from discord.ext import commands
import hunterCards
import game
import mytoken
import sys

TOKEN = mytoken.token
debugEnabled = False

description = '''A more lightweight bot that just runs the forecast script. Meant to be used with a Task Scheduler.'''

intents = discord.Intents.all()

dummyGame = game.GameClass("dummyGame", hunterCards)

prefix = '/'

bot = commands.Bot(command_prefix=prefix, description=description, intents=intents)

explainEmoji = "❓"
subscribedChannels = [950437219859071067, 951182029242900530]


# casting-fate: 950437219859071067
# beta_testing: 951182029242900530
# bot-testing: 950459698870628372


def debug(message):
    if debugEnabled:
        print(message)


async def embedCardExplain(ctx, card: hunterCards.CardClass):
    color = houseColor(card.getHouse())
    await ctx.send(embed=sendEmbed(f"**{card.show()}**", "", card.explain(), color))


async def embedCardShow(ctx, card: hunterCards.CardClass):
    color = houseColor(card.getHouse())
    msg = await ctx.send(embed=sendEmbed(f"**{card.show()}**", "", "", color))
    await msg.add_reaction("❓")


def sendCardEmbed(card: hunterCards.CardClass):
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
    await c.send("Good morning! I bear tidings from the Silent Chorus concerning your fate today. \n The card that "
                 "governs your fate today is...")
    debug(f"Drawing forecast...")
    drawnCard = dummyGame.deck.drawCard()
    if drawnCard.n == "Error" or not isinstance(drawnCard, cards.CardClass):
        await c.send("Error: No card found!")
    else:
        await embedCardShow(c, drawnCard)
    dummyGame.reset()


bot.run(TOKEN)
