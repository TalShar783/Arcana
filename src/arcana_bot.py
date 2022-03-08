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
intents.members = True

thisGame = game.GameClass()

bot = commands.Bot(command_prefix='/', description=description, intents=intents)

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


@bot.command()
async def draw(ctx, name: str, number: int):
    for i in range(number):
        print(f"Drawing a card for {name}...")
        if thisGame == None:
            thisGame.reset()
        thisGame.addPlayer(name)
        for p in thisGame.players:
            if name == p.name:
                p.draw(thisGame.deck)
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
            print(output)
            await ctx.send(output)

@bot.command()
async def explainHand(ctx, player: str):
    print(f"{ctx.author} has requested to see {player}'s cards and their meaning.")
    output: str = ""
    output += f"**{player}:** "
    for p in thisGame.players:
        if player in p.name:
            for c in p.hand:
                output += f"\n\n**{c.show()}:** {c.explain()}"
            print(output)
            await ctx.send(output)

@bot.command()
async def explain(ctx, *args: str):
    card = " ".join(args)
    print(f"{ctx.author} has requested an explanation of the card {card}.")
    output: str = ""
    for c in thisGame.deck.cards:
        if card in c.n:
            output += f"**{c.show()}:** {c.explain()}"
    print(output)
    try:
        await ctx.send(output)
    except discord.errors.HTTPException:
        number = random.randint(1,10)
        match number:
            case 10:
                await ctx.send("How about go fuck yourself.")
            case _:
                await ctx.send("Oops, that's not the proper name of a card. Try again!")

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
