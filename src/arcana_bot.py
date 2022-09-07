from typing import Literal

import discord
from discord import app_commands
from discord.app_commands import Choice
from discord.ext import commands
from discord.ext.commands import Greedy
import asyncio

import cards
import game
import mytoken
import hunterCards
import WildMagicEnums

# TOKEN needs to be your Discord client's private token. mytoken.py is not included in the repository. To use it, just make
# a mytoken.py file and assign your token to the "token" variable.
TOKEN = mytoken.token
# Enabling debugEnabled will allow more verbose reporting in the console.
debugEnabled = True
MY_GUILD = discord.Object(id=476818108896772109)


# TODO: Add an embed function for the client so that it's expandable when the client is mentioned, rather than blowing up the
#  text channel.
# TODO: Add a list for channel IDs or guild IDs that will determine which deck the client will default to using.
class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default(), )
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)


client = MyClient()

# These two dummy games allow us to use our forecast and explain functions without drawing from existing decks.
dummyHunterGame = game.GameClass("dummyHunterGame", hunterCards)
dummyGame = game.GameClass("dummyGame", cards)
# Determines what emoji will be used in the Explain methods.
explainEmoji = "❓"
# Initializes a list of active games. The game IDs will be equivalent to the channel IDs where they're being played.
gamesList = []

# This is the command prefix of the client. Discord.py isn't properly handling slash-commands, so it won't display
# a command autocomplete, but it works regardless.
prefix = '/'


# Makes our debug methods only apply if we've got debugEnabled as True
def debug(message):
    if debugEnabled:
        print(message)


# Default on_ready event, just shows us that we're online.
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


## Events and Async Functions ##

# This method checks against our gamesList to see if there's an existing game in the channel where it's called.
# It takes a gameId as an argument, which usually is just the channel ID as a string.
# If a game is not found, it will return False; if one is found, it'll return the game object itself.
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


# This calls the checkGamesList method, and if a game isn't found, starts a new one with the channel ID.
# It returns a game ID every time, unless there's a very strange error.
# This is called basically any time anyone does anything dealing with a game.
# It takes a channel object as an argument.
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


# Sends a message containing a single embed, containing the "show" function of a card; just the title and house,
# with a color corresponding to the cards' House.
# TODO: Change all card houses to fully include 'house of' or 'court of' descriptions, so I can just use those directly.
async def embedCardShow(interaction: discord.Interaction, card: cards.CardClass):
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
    msg = await interaction.channel.send(embed=sendEmbed(f"**{card.show()}**", "", house, color))
    await msg.add_reaction("❓")


# Constructs and returns an embed. Takes a card object, which can be a CardClass from cards or hunterCards.
def sendCardEmbed(card: cards.CardClass):
    house = ""
    if isinstance(card, cards.CardClass):
        if card.getHouse() == "Unaligned":
            house = f"Unaligned"
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
    explanation = house + "\n\n" + card.explain()
    embed = discord.Embed(title=card.show(), url="", description=explanation, color=color)
    return embed


# Simply sends an embed, given a title, URL, description, and color.
def sendEmbed(title: str, url: str, description: str, color):
    embed = discord.Embed(title=title, url=url, description=description, color=color)
    return embed


# A list of houses and their corresponding colors.
# TODO: When I've renamed the houses, I'm going to need to update these strings.
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


# A long, multi-line string containing markdown formatting, describing how to use the client.
clientInstructions = "I am the Voice of the Abyss.\n" \
                     "I am your window into the past, present and future.\n" \
                     "To speak to me, use the following:\n\n" \
                     f"My command prefix is {prefix}. Prepend all below commands with that.\n\n" \
                     "**reset** resets the deck and players, starting a new game. If you use **reset hunter**, " \
                     "it will instead switch the deck to using the original Hunter's Fate deck.\n\n" \
                     "If you use it without arguments, it will use the Arcana deck.\n\n" \
                     "**players** lists the names of the current players.\n\n" \
                     "**draw** draws at least one card and adds a new player to the game if they're not already playing." \
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
 \
 \


    ##Commands and Events##


@client.tree.command()
@app_commands.describe(first='The first number to add', second='The second number to add')
async def add(
        interaction: discord.Interaction,
        first: app_commands.Range[int, 0, 100],
        second: app_commands.Range[int, 0, None],
):
    """Adds two numbers together"""
    await interaction.response.send_message(f'{first} + {second} = {first + second}', ephemeral=False)


# Uses the on_raw_reaction_add event, given the payload object (another way of accessing the message object). Tries to
# narrow messages down as quickly as possible, since this will be reading every message that's reacted-to.
# Checks to see whether the original message was sent by the client itself, then whether the reaction was sent by anyone
# other than the client, then checks to see if the emoji was the question-mark.
# TODO: Tokenize the question-mark so it can be changed more easily.
# Once the message is recognized as an embed, it reads the description object of the embed. Right now, the only way to
# differentiate between decks is to see whether the house is "Court of" and "Neutral"; or "House of" and "Unaligned."
# TODO: Add deck name to the original embed description and use that to differentiate decks.
# Once recognized, the client searches the appropriate deck and edits the embed to be an Explain embed rather than a Show.

@client.event
async def on_raw_reaction_add(payload):
    messageId = payload.message_id
    msg = await client.get_channel(payload.channel_id).fetch_message(messageId)
    if msg.author == client.get_user(943668329871200258):
        debug("client author recognized")
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


# Reads to see whether the client has been @-mentioned. If so, sends its instructions.
# TODO: Try to make this work with on-mention; I tried it earlier, and it didn't work. Should reduce load slightly.
@client.tree.command()
async def help(interaction: discord.Interaction):
    await interaction.response.send_message(
        embed=sendEmbed("Voice of the Abyss: Instructions", "", clientInstructions, discord.Colour.purple()), ephemeral= True)


# Takes an optional argument that defaults to using the regular Arcana deck. If the argument is "hunter", uses the
# Hunter deck instead.
# TODO: Add error reporting in case an improper argument is given.
@client.tree.command()
@app_commands.describe(card_set="The deck to use in the new game")
async def reset(
        interaction: discord.Interaction,
        card_set: Literal["The Hunter's Fate", "Saen'dal Arcana"]
):
    debug(f"Reset function called. Passed channel = {interaction.channel}")
    if card_set == "Saen'dal Arcana":
        thisGame = initializeGame(interaction.channel)
        thisGame.reset()
        print("The game has been reset!")
        print(f"Players: {thisGame.players}")
        print(f"Cards remaining in deck: {thisGame.deck.cardsRemaining()}")
        await interaction.response.send_message("The game has been reset. Card set: Saen'dal Arcana")
    if card_set == "The Hunter's Fate":
        thisGame = initializeGame(interaction.channel)
        thisGame.reset(hunterCards)
        print("The game has been reset!")
        print(f"Players: {thisGame.players}")
        print(f"Cards remaining in deck: {thisGame.deck.cardsRemaining()}")
        await interaction.response.send_message("The game has been reset. Card set: The Hunter's Fate")


# Switches debug mode on or off, allowing us to debug without restarting the client.
@client.tree.command()
async def debug_switch(interaction: discord.Interaction):
    global debugEnabled
    if debugEnabled:
        debugEnabled = False
        print("Debug disabled.")
    else:
        debugEnabled = True
        print("Debug enabled.")


# Gives a "daily forecast" from the client. This one uses the Arcana deck. Draws from the dummy deck, so that existing
# decks won't be used or altered.
@client.tree.command()
async def forecast(interaction: discord.Interaction):
    await interaction.response.send_message(
        "I bear tidings from the starry abyss concerning your fate today. \n The card that "
        "governs your fate today is...")
    debug(f"Drawing forecast...")
    drawnCard = dummyGame.deck.drawCard()
    if drawnCard.n == "Error" or not isinstance(drawnCard, cards.CardClass):
        await interaction.response.send_message("Error: No card found!")
    else:
        await embedCardShow(interaction, drawnCard)
    dummyGame.reset()


# Same as forecast, but uses the Hunter deck instead.
@client.tree.command()
async def forecast_hunter(interaction: discord.Interaction):
    await interaction.response.send_message(
        "I bear tidings from the Silent Chorus concerning your fate today. \n The card that "
        "governs your fate today is...")
    debug(f"Drawing forecast...")
    drawnCard = dummyHunterGame.deck.drawCard()
    if drawnCard.n == "Error" or not isinstance(drawnCard, hunterCards.CardClass):
        await interaction.response.send_message("Error: No card found!")
    else:
        await embedCardShow(interaction, drawnCard)
    dummyHunterGame.reset(hunterCards)


# Sends a list of players in this channel's game to the channel.
@client.tree.command()
async def players(interaction: discord.Interaction):
    thisGame = initializeGame(interaction.channel)
    print(f"{interaction.user} has requested to see a list of current players.")
    output = ""
    for p in thisGame.players:
        output += f"{p.name}\n"
    await interaction.response.send_message(output)


# Draws a card for the given player. Player must specify the player name to draw the card; after the player exists,
# The command is case-insensitive. If the player provides a number after the playername, it will draw that many cards.
# If no number is specified, it will draw one.
# TODO: Add more robust error handling.
@client.tree.command()
async def draw(interaction: discord.Interaction, name: str, number: int):
    thisGame = initializeGame(interaction.channel)
    thisGame.addPlayer(name)
    for p in thisGame.players:
        if name.casefold() == p.name.casefold():
            await interaction.response.send_message(f"**{p.name}** draws: ")
    for i in range(number):
        print(f"Drawing a card for {name}...")
        for p in thisGame.players:
            if name.casefold() == p.name.casefold():
                drawnCard = p.draw(thisGame.deck)
                print(drawnCard.n)
                if drawnCard.n == "Error" or (not isinstance(drawnCard, cards.CardClass) and not isinstance(drawnCard,
                                                                                                            hunterCards.CardClass)):
                    p.hand.remove(cards.errored_card)
                    await interaction.response.send_message("Error: No card found!")
                else:
                    await embedCardShow(interaction, drawnCard)
    return


# Picks a card out of the active deck, removing it from the deck and adding it to the specified player's hand. Requires
# a case-insensitive player name and a case-insensitive card name.
# TODO: Add more robust error handling.
@client.tree.command()
async def pick(interaction: discord.Interaction, name: str, card: str):
    thisGame = initializeGame(interaction.channel)
    print(f"{name} has requested to draw the card {card}.")
    thisGame.addPlayer(name)
    pickedCard = False
    for p in thisGame.players:
        if name.casefold() == p.name.casefold():
            await interaction.response.send_message(f"**{p.name}** has picked the card...")
            pickedCard = p.pick(thisGame.deck, card)
        if pickedCard == "Error" or (
                not isinstance(pickedCard, cards.CardClass) and not isinstance(pickedCard, hunterCards.CardClass)):
            p.hand.remove(cards.errored_card)
            await interaction.response.send_message("Error: No card found!")
        else:
            await embedCardShow(interaction, pickedCard)
    return


# Sends a "Show" embed for each card in a player's hand.
@client.tree.command()
async def show_hand(interaction: discord.Interaction, player: str):
    thisGame = initializeGame(interaction.channel)
    print(f"{interaction.user} has requested to see {player}'s hand.")
    output: str = ""
    output += f"{player}: "
    for p in thisGame.players:
        if player.casefold() in p.name.casefold():
            await interaction.response.send_message(f"**{p.name}**'s hand is:")
    for p in thisGame.players:
        if player.casefold() in p.name.casefold():
            for c in p.hand:
                output += f"\n**{c.show()}**"
                await embedCardShow(interaction, c)
            print(output)


# Triggers a Wild Magic Surge
@client.tree.command()
async def wild_magic(interaction: discord.Interaction):
    await interaction.response.send_message(f"WILD MAGIC SURGE! \n {WildMagicEnums.WildMagicSurge()}")


client.run(TOKEN)
