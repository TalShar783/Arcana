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


async def embedCard(ctx, card: cards.CardClass):
    color = houseColor(card.getHouse)
    ctx.send(embed=sendEmbed(f"**{card.show()}**", "", card.explain(), color))


async def sendEmbed(title: str, url: str, description: str, color):
    embed = discord.Embed(title=title, url=url, description=description, color=color)
    return embed


async def houseColor(house):
    switcher = {
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
async def players(ctx):
    print(f"{ctx.author} has requested to see a list of current players.")
    output = ""
    for p in thisGame.players:
        output += f"{p.name}\n"
    await ctx.send(output)


@bot.command()
async def draw(ctx, name: str, number: int = 1):
    await ctx.send(f"**{name}** draws: ")
    for i in range(number):
        print(f"Drawing a card for {name}...")
        thisGame.addPlayer(name)
        for p in thisGame.players:
            if name == p.name:
                drawnCard = p.draw(thisGame.deck)
                # color = houseColor(drawnCard.getHouse())
                if drawnCard.n == "Error" or not isinstance(drawnCard, cards.CardClass):
                    p.hand.remove(cards.errored_card)
                    await ctx.send("Error: No card found!")
                else:
                    await embedCard(ctx, drawnCard)
    return


@bot.command()
async def pick(ctx, name: str, *args: str):
    card = " ".join(args)
    print(f"{name} has requested to draw the card {card}.")
    await ctx.send(f"**{name}** has picked the card...")
    thisGame.addPlayer(name)
    for p in thisGame.players:
        if name == p.name:
            pickedCard = p.pick(thisGame.deck, card)
            color = houseColor(pickedCard.getHouse())
            if pickedCard.n == "Error" or not isinstance(pickedCard, cards.CardClass):
                p.hand.remove(cards.errored_card)
                await ctx.send("Error: No card found!")
            else:
                await ctx.send(embed=sendEmbed(f"**{p.name}\n\n {pickedCard.show()}**", "", pickedCard.explain(), color))


@bot.command()
async def showHand(ctx, player: str):
    print(f"{ctx.author} has requested to see {player}'s hand.")
    await ctx.send(f"**{player}**'s hand is:")
    output: str = ""
    output += f"{player}: "
    for p in thisGame.players:
        if player in p.name:
            for c in p.hand:
                output += f"\n**{c.show()}**"
                color = houseColor(c.getHouse())
                await ctx.send(embed=sendEmbed(f"**{c.show()}**", "", "", color))
            print(output)


@bot.command()
async def explainHand(ctx, player: str):
    print(f"{ctx.author} has requested to see {player}'s cards and their meaning.")
    await ctx.send(f"I shall now explain **{player}**'s hand...")
    output: str = ""
    output += f"**{player}:** "
    for p in thisGame.players:
        if player in p.name:
            for c in p.hand:
                color = houseColor(c.getHouse())
                output += f"\n\n**{c.show()}:** {c.explain()}"
                await ctx.send(embed=sendEmbed(f"**{c.show()}**", "", c.explain(), color))
            print(output)


@bot.command()
async def explain(ctx, *args: str):
    card = " ".join(args)
    print(f"{ctx.author} has requested an explanation of the card {card}.")
    for c in thisGame.deck.originalCards:
        if card in c.n:
            color = houseColor(c.getHouse())
            try:
                await ctx.send(embed=sendEmbed(f"**{c.show()}**", "", c.explain(), color))
                return
            except discord.errors.HTTPException:
                number = random.randint(1, 10)
                match number:
                    case 10:
                        await ctx.send("How about go fuck yourself.")
                    case _:
                        await ctx.send("Oops, that's not the proper name of a card. Try again!")
                return

    number = random.randint(1, 10)
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
