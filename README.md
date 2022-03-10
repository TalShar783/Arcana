# Arcana
 
The Saen'Dal Arcana is an in-world tarot deck for a friend's D&D campaign. This bot simulates a single deck of cards (across all instances; multi-server compatibility isn't implemented), and allows any number of players to draw any number of cards and view their hands and have the cards explained to them. It will respond to any messages in any channel it can see, including DMs.

## Commands

The command prefix is defined as the “prefix” variable near the top of arcana-bot.py. It can be changed to anything you want. I was never able to get Discord’s default slash-commands to work with it.

**@-mentioning** the bot will cause it to introduce itself in the channel and give a brief rundown of how to use it.

```draw``` draws a given number of cards from the deck (default 1) and adds it to the player’s hand. By default it _shows_ the card drawn, which only displays the card’s title. If the player isn’t already part of the game, drawing or picking a card will add them to it. It takes two parameters (in this order): The name of the player, and the number of  cards to draw.

**Example:** ```/draw Lenore 3``` or ```/draw Trish``` (this will draw Trish one card).

```pick``` takes two parameters: a player and the name of a card (as it is displayed when it’s sent by the bot). It adds the named card to the named player’s hand. Careful, the bot might get a little testy if you get a card name wrong.

```explain``` takes a single parameter, the name of a card, and, without drawing it, gives the explanation of the named card.

**Example:** ```/pick Lenore King of Darkness```

```showHand``` takes a single parameter, a player, and returns the titles of each card in the player’s hand.  

**Example:** ```/showHand Lenore```

```explainHand``` does what showHand does, but returns the description of each card inside of its embed.

```players``` takes no parameters and returns a list of players in the current game.

```reset``` takes no parameters, clears the list of players, and builds a new deck.

The bot, by default, reacts to each of its messages that **show** a card with a ❓. If anyone clicks that emoji, the bot will edit the **show** message and turn it into an **explain** message.

