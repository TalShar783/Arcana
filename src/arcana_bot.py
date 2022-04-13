import discord
import os
from discord.ext import commands
import random
import cards
import deck
import player
import game
import mytoken
import hunterCards

TOKEN = mytoken.token
debugEnabled = True

description = '''A bot to run a tarot-type deck of cards to predict your future.'''

intents = discord.Intents.all()

dummyHunterGame = game.GameClass("dummyHunterGame", hunterCards)
dummyGame = game.GameClass("dummyGame", cards)

prefix = '/'

bot = commands.Bot(command_prefix=prefix, description=description, intents=intents)

explainEmoji = "❓"
gamesList = []


def debug(message):
    if debugEnabled:
        print(message)


def checkGamesList(gameId):
    debug(f"Checking games list for existing game with gameID {gameId}...")
    debug(f"Type passed for gameId is {type(gameId)}.")
    if not gamesList:
        debug("Games List is empty.")
        return False
    for g in gamesList:
        if g.getId() == gameId:
            debug(f"Game found: {g.getId()}. Variable type is {type(g.getId())}.")
            return g
    return False


def initializeGame(channelRaw):
    if type(channelRaw) == discord.channel.TextChannel:
        channel = f"{channelRaw.id}"
        debug(f"Recasting channel name {channelRaw} to channel ID {channel}.")
    else:
        channel = f"{channelRaw.id}"
        debug(f"Channel {channel} did not need recasting.")
    if not checkGamesList(channel):
        newGame = game.GameClass(channel)
        debug(f"newGame object is {newGame}")
        gamesList.append(newGame)
        debug(f"New game added at object: {newGame}. Id is {newGame.getId()}.")
        debug(f"gamesList is now the following: {gamesList}")
        if debug:
            for g in gamesList:
                debug(f"Game Object: {g}. Game ID: {g.getId()}")
                debug(g)
        return newGame
    else:
        debug(f"Existing game found with object {channel} as its id.")
        debug(f"gamesList is now the following: {gamesList}")
        if debug:
            for g in gamesList:
                debug(f"Game Object: {g}. Game ID: {g.getId()}")
        return checkGamesList(channel)


async def embedCardExplain(ctx, card: cards.CardClass):
    color = houseColor(card.getHouse())
    await ctx.send(embed=sendEmbed(f"**{card.show()}**", "", card.explain(), color))


async def embedCardShow(ctx, card: cards.CardClass):
    color = houseColor(card.getHouse())
    house = ""
    if isinstance(card, cards.CardClass):
        house = f"House of {card.getHouse()}"
        if card.getHouse() == "Unaligned":
            house = "Unaligned"
    if isinstance(card, hunterCards.CardClass):
        house = f"Court of the {card.getHouse()}"
        if card.getHouse() == "Unaligned":
            house = "Neutral"
        if card.getHouse() == "Myths":
            house = "Court of Myths"
        if card.getHouse() == "Beasts":
            house = "Court of Beasts"
    msg = await ctx.send(embed=sendEmbed(f"**{card.show()}**", "", house, color))
    await msg.add_reaction("❓")


def sendCardEmbed(card: cards.CardClass):
    house = ""
    if isinstance(card, cards.CardClass):
        if card.getHouse() == "Unaligned":
            house = f"Unaligned\n\n"
        else:
            house = f"House of {card.getHouse()}"
    if isinstance(card, hunterCards.CardClass):
        house = f"Court of the {card.getHouse()}"
        if card.getHouse() == "Unaligned":
            house = "Neutral"
        if card.getHouse() == "Myths":
            house = "Court of Myths"
        if card.getHouse() == "Beasts":
            house = "Court of Beasts"
    color = houseColor(card.getHouse())
    explanation = house+card.explain()
    embed = discord.Embed(title=card.show(), url="", description=explanation, color=color)
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
        "Dead": discord.Colour.darker_gray(),
        "Fae": discord.Colour.dark_green(),
        "Damned": discord.Colour.dark_red(),
        "Divine": discord.Colour.gold(),
        "Eldritch": discord.Colour.dark_purple(),
        "Beasts": discord.Colour.dark_orange(),
        "Myths": discord.Colour.dark_blue(),
        "Hunters": discord.Colour.teal(),
        "Unaligned": discord.Colour.dark_gray()
    }
    return switcher.get(house)


botInstructions = "I am the Voice of the Abyss.\n" \
                  "I am your window into the past, present and future.\n" \
                  "To speak to me, use the following:\n\n" \
                  f"My command prefix is {prefix}. Prepend all below commands with that.\n\n" \
                  "**reset** resets the deck and players, starting a new game. If you use **reset hunter**, " \
                  "it will instead switch the deck to using the original Hunter's Fate deck.\n\n" \
                  "**players** lists the names of the current players.\n\n" \
                  "**draw** draws at least one card and adds a new player to the game if they're not already playing. " \
                  "It then adds those cards to the player's hand.\n" \
                  "**draw** accepts up to two parameters, the first of which is required: the player's name, " \
                  "and the number of cards to draw.\n" \
                  "Example: **draw Lenore 5** will draw 5 cards for the player Lenore.\n\n" \
                  "**pick** takes a card name and draws that card from the deck, and adds it to the player's hand. " \
                  "Example: **pick Lenore King of Darkness**\n\n" \
                  "**showHand** takes a player parameter and shows all the titles of the cards in their hand. " \
                  "Example: **showHand Lenore**\n\n" \
                  "**forecast** draws you one card, unassociated with any game or player, to predict your day.\n\n" \
                  "Lastly, any time you see me react to a message with ❓, you may click that to request that I " \
                  "explain the card in question." \


@bot.event
async def on_raw_reaction_add(payload):
    messageId = payload.message_id
    msg = await bot.get_channel(payload.channel_id).fetch_message(messageId)
    if msg.author == bot.get_user(943668329871200258):
        debug("Bot author recognized")
        if payload.user_id != 943668329871200258:
            debug("Reacting user is not self.")
            if str(payload.emoji) == "❓":
                debug("Emoji recognized.")
                if isinstance(msg.embeds[0], discord.embeds.Embed):
                    debug("Message recognized as an embed")
                    await msg.clear_reaction("❓")
                    msgCard = msg.embeds[0].title.replace("*", "")
                    if "Court of" in msg.embeds[0].description or "Neutral" in msg.embeds[0].description:
                        debug("Card recognized as a Hunter card.")
                        for c in dummyHunterGame.deck.originalCards:
                            if c.n.casefold() == msgCard.casefold():
                                await msg.edit(embed=sendCardEmbed(c))
                                return
                    else:
                        if "House of" in msg.embeds[0].description or "Unaligned" in msg.embeds[0].description:
                            debug("Card recognized as an Arcana card.")
                            for c in dummyGame.deck.originalCards:
                                if c.n.casefold() == msgCard.casefold():
                                    await msg.edit(embed=sendCardEmbed(c))
                                    return
                        return


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.listen('on_message')
async def userMention(msg):
    if bot.user.mentioned_in(msg):
        await msg.channel.send(
            embed=sendEmbed("Voice of the Abyss: Instructions", "", botInstructions, discord.Colour.purple()))


@bot.command()
async def reset(ctx, card_set="cards"):
    debug(f"Reset function called. Passed channel = {ctx.channel}")
    if card_set == "cards":
        thisGame = initializeGame(ctx.channel)
        thisGame.reset()
        print("The game has been reset!")
        print(f"Players: {thisGame.players}")
        print(f"Cards remaining in deck: {thisGame.deck.cardsRemaining()}")
        await ctx.send("The game has been reset. Card set: Saen'dal Arcana")
    if card_set == "hunter":
        thisGame = initializeGame(ctx.channel)
        thisGame.reset(hunterCards)
        print("The game has been reset!")
        print(f"Players: {thisGame.players}")
        print(f"Cards remaining in deck: {thisGame.deck.cardsRemaining()}")
        await ctx.send("The game has been reset. Card set: Fate of the Hunter")


@bot.command()
async def debugSwitch(ctx):
    global debugEnabled
    if debugEnabled:
        debugEnabled = False
        print("Debug disabled.")
    else:
        debugEnabled = True
        print("Debug enabled.")


@bot.command()
async def forecast(ctx):
    await ctx.send("I bear tidings from the starry abyss concerning your fate today. \n The card that "
                   "governs your fate today is...")
    debug(f"Drawing forecast...")
    drawnCard = dummyGame.deck.drawCard()
    if drawnCard.n == "Error" or not isinstance(drawnCard, cards.CardClass):
        await ctx.send("Error: No card found!")
    else:
        await embedCardShow(ctx, drawnCard)
    dummyGame.reset()


@bot.command()
async def forecastHunter(ctx):
    await ctx.send("I bear tidings from the Silent Chorus concerning your fate today. \n The card that "
                   "governs your fate today is...")
    debug(f"Drawing forecast...")
    drawnCard = dummyHunterGame.deck.drawCard()
    if drawnCard.n == "Error" or not isinstance(drawnCard, hunterCards.CardClass):
        await ctx.send("Error: No card found!")
    else:
        await embedCardShow(ctx, drawnCard)
    dummyHunterGame.reset(hunterCards)


@bot.command()
async def players(ctx):
    thisGame = initializeGame(ctx.channel)
    print(f"{ctx.author} has requested to see a list of current players.")
    output = ""
    for p in thisGame.players:
        output += f"{p.name}\n"
    await ctx.send(output)


@bot.command()
async def draw(ctx, name: str, number: int = 1):
    thisGame = initializeGame(ctx.channel)
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
                if drawnCard.n == "Error" or (not isinstance(drawnCard, cards.CardClass) and not isinstance(drawnCard,
                                                                                                            hunterCards.CardClass)):
                    p.hand.remove(cards.errored_card)
                    await ctx.send("Error: No card found!")
                else:
                    await embedCardShow(ctx, drawnCard)
    return


@bot.command()
async def pick(ctx, name: str, *args: str):
    thisGame = initializeGame(ctx.channel)
    card = " ".join(args)
    print(f"{name} has requested to draw the card {card}.")
    thisGame.addPlayer(name)
    pickedCard = False
    for p in thisGame.players:
        if name.casefold() == p.name.casefold():
            await ctx.send(f"**{p.name}** has picked the card...")
            pickedCard = p.pick(thisGame.deck, card)
        if pickedCard == "Error" or (
                not isinstance(pickedCard, cards.CardClass) and not isinstance(pickedCard, hunterCards.CardClass)):
            p.hand.remove(cards.errored_card)
            await ctx.send("Error: No card found!")
        else:
            await embedCardShow(ctx, pickedCard)
    return


@bot.command()
async def showHand(ctx, player: str):
    thisGame = initializeGame(ctx.channel)
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


bot.run(TOKEN)
