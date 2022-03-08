import discord
import os
from discord.ext import commands
import random
import cards
import deck
import player
import game

TOKEN = os.environ.get('BOT_TOKEN')

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

intents = discord.Intents.all()

thisGame = game.GameClass()

bot = commands.Bot(command_prefix='/', description=description, intents=intents)

def sendEmbed(title: str, url: str, description: str, color):
    embed = discord.Embed(title=title, url=url, description=description, color=color)
    return embed

def houseColor(house):
    switcher = {
        # "Darkness": "#9c0399",
        # "Light": "#fdff8f",
        # "Fire": "#ff2f00",
        # "Ice": "#00f7ff",
        # "Unaligned": "#a1a1a1"
        "Darkness": discord.Colour.purple(),
        "Light": discord.Colour.yellow(),
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

@bot.command()
async def reset(ctx):
    thisGame.reset()
    print("The game has been reset!")
    print(f"Players: {thisGame.players}")
    print(f"Cards remaining in deck: {thisGame.deck.cardsRemaining()}")
    await ctx.send("The game has been reset.")


@bot.command()
async def draw(ctx, name: str, number: int = 1):
    for i in range(number):
        print(f"Drawing a card for {name}...")
        thisGame.addPlayer(name)
        for p in thisGame.players:
            if name == p.name:
                drawnCard = p.draw(thisGame.deck)
                color = houseColor(drawnCard.getHouse())
                await ctx.send(embed=sendEmbed(f"**{p.name}\n\n {drawnCard.show()}**", "", drawnCard.explain(), color))
    return

@bot.command()
async def showHand(ctx, player: str):
    print(f"{ctx.author} has requested to see {player}'s hand.")
    output: str = ""
    output += f"{player}: "
    for p in thisGame.players:
        if player in p.name:
            for c in p.hand:
                output += f"\n**{c.show()}**"
                color = houseColor(c.getHouse())
                await ctx.send(embed=sendEmbed(f"**{p.name}\n\n {c.show()}**", "", "", color))
            print(output)


@bot.command()
async def explainHand(ctx, player: str):
    print(f"{ctx.author} has requested to see {player}'s cards and their meaning.")
    output: str = ""
    output += f"**{player}:** "
    for p in thisGame.players:
        if player in p.name:
            for c in p.hand:
                color = houseColor(c.getHouse())
                output += f"\n\n**{c.show()}:** {c.explain()}"
                await ctx.send(embed=sendEmbed(f"**{p.name}\n\n {c.show()}**", "", c.explain(), color))
            print(output)

@bot.command()
async def explain(ctx, *args: str):
    card = " ".join(args)
    print(f"{ctx.author} has requested an explanation of the card {card}.")
    output: str = ""
    for c in thisGame.deck.cards:
        if card in c.n:
            color = houseColor(c.getHouse())
            try:
                await ctx.send(embed=sendEmbed(f"**{c.show()}**", "", c.explain(), color))
            except discord.errors.HTTPException:
                number = random.randint(1,10)
                match number:
                    case 10: await ctx.send("How about go fuck yourself.")
                    case _: await ctx.send("Oops, that's not the proper name of a card. Try again!")



@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

bot.run(TOKEN)
