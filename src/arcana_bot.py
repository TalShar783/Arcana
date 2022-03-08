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

explainEmoji = bot.get_emoji(950860713138737202)


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
        "Light": discord.Colour.yellow(),
        "Fire": discord.Colour.red(),
        "Ice": discord.Colour.blue(),
        "Unaligned": discord.Colour.dark_gray()
    }
    return switcher.get(house)

@bot.event
async def on_raw_reaction_add(payload):
    if payload.user_id != 943668329871200258:
        if str(payload.emoji) == "❓":
            # print(payload)
            messageId = payload.message_id
            msg = await bot.get_channel(payload.channel_id).fetch_message(messageId)
            await msg.clear_reaction("❓")
            msgCard = (msg.embeds[0].title).replace("*","")
            print(msgCard)
            for c in thisGame.deck.originalCards:
                if c.n.casefold() == msgCard.casefold():
                    await msg.edit(embed=sendCardEmbed(c))
            # await msg.channel.send(msg.embed)
            # await msg.edit()


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
    for p in thisGame.players:
        if name.casefold() == p.name.casefold():
            await ctx.send(f"**{p.name}** draws: ")
    for i in range(number):
        print(f"Drawing a card for {name}...")
        thisGame.addPlayer(name)
        for p in thisGame.players:
            if name.casefold() == p.name.casefold():
                drawnCard = p.draw(thisGame.deck)
                print(drawnCard.n)
                if drawnCard.n == "Error" or not isinstance(drawnCard, cards.CardClass):
                    p.hand.remove(cards.errored_card)
                    await ctx.send("Error: No card found!")
                else:
                    await embedCardShow(ctx, drawnCard)
    return


@bot.command()
async def pick(ctx, name: str, *args: str):
    card = " ".join(args)
    print(f"{name} has requested to draw the card {card}.")
    thisGame.addPlayer(name)
    for p in thisGame.players:
        if name.casefold() == p.name.casefold():
         await ctx.send(f"**{p.name}** has picked the card...")
         pickedCard = p.pick(thisGame.deck, card)
        if pickedCard.n == "Error" or not isinstance(pickedCard, cards.CardClass):
            p.hand.remove(cards.errored_card)
            await ctx.send("Error: No card found!")
        else:
            await embedCardShow(ctx, pickedCard)


@bot.command()
async def showHand(ctx, player: str):
    print(f"{ctx.author} has requested to see {player}'s hand.")
    output: str = ""
    output += f"{player}: "
    for p in thisGame.players:
        if player.casefold() in p.name.casefold():
            await ctx.send(f"**{p.name}**'s hand is:")
    for p in thisGame.players:
        if player.casefold() in p.name.casefold():
            for c in p.hand:
                output += f"\n**{c.show()}**"
                await embedCardShow(ctx, c)
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
                await embedCardExplain(ctx, c)


@bot.command()
async def explain(ctx, *args: str):
    card = " ".join(args)
    print(f"{ctx.author} has requested an explanation of the card {card}.")
    for c in thisGame.deck.originalCards:
        if card.casefold() in c.n.casefold():
            try:
                await embedCardExplain(ctx, c)
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
