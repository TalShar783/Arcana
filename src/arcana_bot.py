import discord
import os
from discord.ext import commands
import random
import cards
import deck
import player
import game
import token

TOKEN = token.token

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

intents = discord.Intents.all()

thisGame = game.GameClass()

prefix = '/'

bot = commands.Bot(command_prefix=prefix, description=description, intents=intents)

explainEmoji = "❓"


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


botInstructions = "I am the Voice of the Abyss.\n" \
                  "I am your window into the past, present and future.\n" \
                  "To speak to me, use the following:\n\n" \
                  f"My command prefix is {prefix}. Prepend all below commands with that.\n\n" \
                  "**reset** resets the deck and players, starting a new game.\n\n" \
                  "**players** lists the names of the current players.\n\n" \
                  "**draw** draws at least one card and adds a new player to the game if they're not already playing. It then adds those cards to the player's hand.\n" \
                  "**draw** accepts up to two parameters, the first of which is required: the player's name, and the number of cards to draw.\n" \
                  "Example: **draw Lenore 5** will draw 5 cards for the player Lenore.\n\n" \
                  "**pick** takes a card name and draws that card from the deck, and adds it to the player's hand. Example: **pick Lenore King of Darkness**\n\n" \
                  "**showHand** takes a player parameter and shows all the titles of the cards in their hand. Example: **showHand Lenore**\n\n" \
                  "**explainHand** is like showHand, but also returns the descriptions of each card.\n\n" \
                  "**explain** takes the name of a card and returns its explanation. Example: **explain King of Darkness**\n\n" \
                  "Lastly, any time you see me react to a message with ❓, you may click that to request that I explain the card in question." \

@bot.event
async def on_raw_reaction_add(payload):
    if payload.user_id != 943668329871200258:
        if str(payload.emoji) == "❓":
            messageId = payload.message_id
            msg = await bot.get_channel(payload.channel_id).fetch_message(messageId)
            if isinstance(msg.embeds[0].description, discord.embeds._EmptyEmbed):
                await msg.clear_reaction("❓")
                msgCard = msg.embeds[0].title.replace("*", "")
                for c in thisGame.deck.originalCards:
                    if c.n.casefold() == msgCard.casefold():
                        await msg.edit(embed=sendCardEmbed(c))


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.listen('on_message')
async def userMention(msg):
    if bot.user.mentioned_in(msg):
        await msg.channel.send(embed=sendEmbed("Voice of the Abyss: Instructions", "", botInstructions, discord.Colour.purple()))


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
    thisGame.addPlayer(name)
    for p in thisGame.players:
        if name.casefold() == p.name.casefold():
            await ctx.send(f"**{p.name}** draws: ")
    for i in range(number):
        print(f"Drawing a card for {name}...")
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
