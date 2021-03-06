import random

# TODO: Merge cards and hunterCards into a single file, make a new attribute describing what deck the card belongs to.
#  This will require a good bit of refactoring.
# TODO: Add documentation.


class CardClass:
    registry = []

    def __init__(self, name, description, house):
        self.n = name
        self.d = description
        self.h = house
        self.registry.append(self)
        if self.n == "The Chalice":
            self.d += f" {self.rollChalice()}"

    def show(self):
        try:
            return self.n
        except Exception:
            return errored_card.n

    def explain(self):
        try:
            return self.d
        except Exception:
            return errored_card.d

    def getHouse(self):
        try:
            return self.h
        except Exception:
            return errored_card.h

    def rollChalice(self):
        switcher = {
            1: "This Chalice is filled with glistening red blood.",
            2: "This Chalice is filled with nauseating green poison.",
            3: "This Chalice is filled with rich purple wine."
        }
        roll = switcher.get(random.randint(1, 3), "Invalid")
        return roll


lord_of_ice = CardClass("Lord of Ice",
                        "A reflection of the Saen’dal‘s greatest leaders, the Lord of Ice represents wisdom, "
                        "leadership, and right action. As a card in a fortune, it foretells guidance and good advice. "
                        "The recipient would also be wise to look back on recent conversations and attempt to glean "
                        "kernels of wisdom that may have escaped their initial understanding. ",
                        "Ice")
lady_of_ice = CardClass("Lady of Ice",
                        "As the Lord is a figure of leadership, the Lady is a guardian. She recalls the mythic figure "
                        "of Silanah, who delivered her people from their greatest foes and preserved their way of "
                        "life for millennia. Her appearance foretells the arrival of a protector, whether in the form "
                        "of a parent, teacher, friend, or colleague. In other cases, it might guide the recipient to "
                        "renew relationships with such figures, in order to better prepare for the inevitable arrival "
                        "of the proverbial Winter.",
                        "Ice")
sage_of_ice = CardClass("Sage of Ice",
                        "The Sage of Ice is straightforward. His appearance in the Arcana represents learning and "
                        "discovery, the acquisition of valuable knowledge that will be of benefit to the recipient "
                        "and those close to them. As before, this could foretell a future revelation, or guide the "
                        "recipient to re-examine the knowledge they already possess. ",
                        "Ice")
servant_of_ice = CardClass("Servant of Ice",
                           "The Servant recalls the righteous knights who fought not only for the safety of the "
                           "Saen’dal, but for the preservation of their very souls. It symbolizes duty, devotion, "
                           "and service to a righteous cause. As an omen, it is often understood as a call to devote "
                           "oneself to such a cause, or to seek a cause worthy of such devotion if one seems absent. "
                           "It can also be taken as a confirmation of the righteousness of one’s path.",
                           "Ice")
preservation = CardClass("Preservation",
                         "Along with their association between Winter and community, the authors of the Arcana also "
                         "believed in the role of collective memory in the preservation of their people. As such, "
                         "the card Preservation recalls not only physical safety, but remembrance. When drawn, "
                         "it calls on the recipient to remember the past: its people, events, and lessons. It is less "
                         "an omen and more a demand: keep your past close, or be lost in the future. ",
                         "Ice")
winter = CardClass("Winter",
                   "Winters in the ancient lands of the Saen’dal were harsh. They demanded concerted, communal "
                   "efforts to ensure their people would survive to see the spring. As such, they developed a "
                   "powerful association between the winter and community. In the Arcana, this card represents a "
                   "convergence: the coming together of friends, family, and allies for the achievement of a "
                   "collective goal. It foretells difficulty, yes, but difficulty that can be overcome with the "
                   "aid of one’s people. ",
                   "Ice")

lord_of_fire = CardClass("Lord of Fire",
                         "Distinct from the King of Darkness in several ways, but an ill omen regardless. The Lord of "
                         "Fire reveals a force of destruction, rather than evil, blind to causes and allegiances and "
                         "driven by the need to ruin, rather than selfish desire. As a window into the future, "
                         "the Lord of Fire’s appearance indicates an active and persistent threat to the recipient’s "
                         "physical safety: an invading army, an oncoming storm, a rumbling volcano—something that "
                         "cannot be reasoned with, and seeks only to destroy.",
                         "Fire")
lady_of_fire = CardClass("Lady of Fire",
                         "The Lady of Fire represents danger, just as the Lord does. However, her flavor of threat is "
                         "very different: she represents a threat from within, most usually in the form of some "
                         "temptation or personal weakness. She is an omen of seduction, but not necessarily by some "
                         "scarlet-haired temptress—whether the allure of power, the promise of pleasure, or simply the "
                         "siren call of greed and gluttony, the Lady of Fire is a warning against ruin wrought by "
                         "one’s own hands.",
                         "Fire")
demon_of_fire = CardClass("Demon of Fire",
                          "As with the whole of the House of Fire, the Demon warns of danger to come. However, "
                          "as the Lord represents danger on a grand scale, the Demon represents it on a personal "
                          "level, though this makes it no less threatening to the recipient. Often conflated with "
                          "Knight of Darkness, the two are actually quite distinct: the Knight represents a figure of "
                          "personal animosity, a long-held grudge, a rivalry. The Demon, on the other hand, "
                          "represents a threat with no history, no targeted malice. A blind robbery, a random act of "
                          "violence, a target of opportunity—these are manifestations of the Demon. As an omen, "
                          "it calls for vigilance against such threats, and avoidance of the circumstances in which "
                          "they are likely to arrive.",
                          "Fire")
slave_of_fire = CardClass("Slave of Fire",
                          "Just as effects are slaves to their causes, so it is with the Slave of Fire. A very "
                          "straightforward omen, the Slave of Fire warns of danger that follows from one’s own "
                          "choices. The appearance of the Slave does not necessarily condemn the recipient’s "
                          "actions—even the most noble actions can still bring about danger—but it warns that they may "
                          "have had unintended side effects. Drawing this card may prompt an inspection of recent "
                          "actions or a reconsideration of plans, with the goal of unmasking the potentially harmful "
                          "consequences. ",
                          "Fire")
destruction = CardClass("Destruction",
                        "A brighter omen than Chaos, but not by much. The Saen’dal separated the two along an "
                        "important axis: pain versus suffering. Chaos entails the latter: sorrow and emotional pain "
                        "that will scar the very soul. Destruction foretells the former: physical pain, the loss of "
                        "property, and scars for the flesh. The Saen’dal viewed these things as secondary, "
                        "to the point where some considered Destruction a positive omen: such losses could be "
                        "recouped, and even a maimed body could house a joyful soul.",
                        "Fire")
inferno = CardClass("Inferno",
                    "Like Sea and Desert, the Inferno is a reference to the Saen’dal homeworld of Arion. "
                    "However, unlike the lands of Light and Darkness, Inferno reflects another realm: the Four "
                    "Hells, wherein the original Archdaemons made their abode. Regardless of its historical "
                    "allusions, the modern card has a very simple meaning: the recipient is currently in danger, "
                    "whether they know it or not. Be it an abusive relationship, a dangerous job, or an unsafe "
                    "dwelling, to draw the Inferno means that one is there, and should immediately re-examine "
                    "his life to locate and elude danger.",
                    "Fire")

king_of_darkness = CardClass("King of Darkness",
                             "Where the King is distant, the Knight is intimate. A personal rival, a bitter foe, "
                             "a cruel tormentor who knows the recipient, and whom the recipient knows in return. The "
                             "appearance of the Knight often foretells direct conflict with this adversary. It means "
                             "that one’s steps forward will be contested, not by fickle chance, but by an active, "
                             "hostile will.",
                             "Darkness")
knight_of_darkness = CardClass("Knight of Darkness",
                               "Where the King is distant, the Knight is intimate. A personal rival, a bitter foe, "
                               "a cruel tormentor who knows the recipient, and whom the recipient knows in return. "
                               "The appearance of the Knight often foretells direct conflict with this adversary. It "
                               "means that one’s steps forward will be contested, not by fickle chance, "
                               "but by an active, hostile will.",
                               "Darkness")
soldier_of_darkness = CardClass("Soldier of Darkness",
                                "Where the King is distant, and the Knight is intimate, the Soldiers are faceless but "
                                "immediate. They are pawns, for whom the recipient is but one face among many. The "
                                "appearance of the Soldier indicates coming hardship and conflict. Most often, "
                                "this will be a battle in which the recipient will be outnumbered.",
                                "Darkness")
child_of_darkness = CardClass("Child of Darkness",
                              "Where the other servants of Darkness act with intent, a Child is merely the product of "
                              "its circumstances. This card represents the unintended consequences of evil; the "
                              "aftershocks left in evil’s wake that do its work unbeknownst to it. The appearance of "
                              "the Child foretells the fallout from the King’s schemes, a twist of fate or betrayal "
                              "as a result of evil deeds. ",
                              "Darkness")
chaos = CardClass("Chaos",
                  "Another historical reference to the Saen’dal’s past, Chaos refers to the collapse of their "
                  "civilization as a result of their creators’ tragic deaths. Though this context is largely "
                  "forgotten, the card’s presence in the Arcana represents the chaos and bereavement that are the "
                  "fulfillment of the King of Darkness’ plans. A dark omen, it foretells a time of uncertainty, fear, "
                  "or loss; a reshuffling of circumstances that will bring sorrow and suffering.",
                  "Darkness")
the_desert = CardClass("The Desert",
                       "A historical reference to the lifeless deserts of the continent Kaladyn, on the Saen’dal "
                       "homeworld of Arion, wherein dwelt the ancient enemies of their people. The Desert represents "
                       "the abode of evil, the place in which Darkness makes its home. In the Arcana, it is most "
                       "often interpreted as a warning against a particular place, or a sign that one should relocate "
                       "to a new home. In a more metaphorical light, it can mean the exhaustion of possibilities; in "
                       "this way, the Desert may act as an admonition against becoming stuck in one’s ways.",
                       "Darkness")

queen_of_light = CardClass("Queen of Light",
                           "One of the brightest omens the Saen’dal Arcana can bestow, the Queen of Light is the "
                           "equal and opposite of the King of Darkness. Her appearance indicates the presence in "
                           "one’s life of a benefactor or provider who wishes to see the recipient succeed. She is an "
                           "omen of hope: no matter how dark one’s circumstances may seem, the Queen reaches out with "
                           "support and charity, even if she is unseen.",
                           "Light")
hero_of_light = CardClass("Hero of Light",
                          "The Queen’s presence is often distant or subtle, yet the Hero’s is visible and immediate. "
                          "His appearance indicates an ally, a friend, a comrade-in-arms, one who will bear the "
                          "struggles and trials of life alongside the recipient. Drawing the Hero may foretell the "
                          "arrival of a champion, or it may simply indicate that one is not so alone as he or she "
                          "believes.",
                          "Light")
painter_of_light = CardClass("Painter of Light",
                             "The Painter does not wield the power or influence of the Queen, nor the shining sword "
                             "of the Hero, but she is a foe of the Darkness all the same. Her appearance indicates "
                             "something of beauty and worth in the recipient’s life: a bastion to which one can "
                             "retreat in the face of suffering and loss, whether she takes the form of a person, "
                             "a work of art, or a simple pleasure from which the recipient might draw strength. If "
                             "the Painter appears, one should devote himself to the search for beauty in his life; "
                             "often, it will be lurking nearby, unseen.",
                             "Light")
sword_of_light = CardClass("Sword of Light",
                           "A weapon against the Darkness, but without a will of its own. The appearance of the Sword "
                           "indicates a tool, a weapon, a gift, a boon—something that will aid in the recipient’s "
                           "struggles, but something that must be actively wielded, rather than providing assistance "
                           "itself. The Sword of Light can foretell the arrival or finding of such a tool, "
                           "but it is often thought of as a reminder of assets forgotten; the tools the recipient "
                           "already possesses, but has overlooked. ",
                           "Light")
order = CardClass("Order",
                  "While many modern audiences might find the concept of “Order” stifling or restrictive, "
                  "the Saen’dal culture that birthed the Arcana held it as their highest aspiration: a return to the "
                  "orderly state of the world in which their gods, the Phaen, held dominion over creation. As such, "
                  "Order is one of the brightest omens the cards can offer: a promise of clarity, of calm, "
                  "of peace. It promises that Darkness is not indomitable, and that a resolution to one’s struggles "
                  "is on the horizon.",
                  "Light")
the_sea = CardClass("The Sea",
                    "Like The Desert, The Sea is a reference to the world from whence the Saen’dal came: the Sea of "
                    "Light, the grave of their creators and a place of tranquility and peace. The Sea represents a "
                    "place of safety, and in the modern, fortune-telling context of the Arcana, it may be interpreted "
                    "as a call to action: to seek out peace and harmony, whether physical or spiritual.",
                    "Light")

the_tower = CardClass("The Tower",
                      "Among the most ambiguous of the Unaligned, the Tower has many different interpretations. In "
                      "some traditions, it is an omen of a mighty obstacle; a fortress tower that will need to be "
                      "scaled or besieged, usually through great effort. To others, it represents a need for a "
                      "broader perspective: to gain a higher vantage by which to examine one’s circumstances. Still "
                      "others believe that it is a beacon tower: a call to arms, a warning to gather one’s strength "
                      "for coming conflict.",
                      "Unaligned")
the_fist = CardClass("The Fist",
                     "The Fist represents the mailed gauntlet of a knight, and is associated with martial skill, "
                     "physical might, and decisive action. It is generally understood to mean that one of these three "
                     "qualities will soon be urgently needed, and is a warning to prepare for that eventuality. In "
                     "other cases, it is seen as a sign that the recipient will soon gain one of the aforementioned "
                     "qualities.",
                     "Unaligned")
the_sceptre = CardClass("The Sceptre",
                        "The Scepter represents the office of the king’s vizier and advisor, and is associated with "
                        "knowledge, arcane power, and foresight. As an omen, it foretells a need for one of the "
                        "three, generally to sway another’s belief or change another’s actions (as an advisor might "
                        "warn his leader). Others interpret the Scepter, like the Fist, as an indication that such "
                        "power or knowledge will be granted to the recipient.",
                        "Unaligned")
the_chalice = CardClass("The Chalice",
                        f"Complex in execution and simple in meaning, Chalice is the omen of the unexpected. Unique "
                        f"among all the cards in the deck, there are actually three Chalices. If one is drawn, "
                        f"the others should be removed afterward. One Chalice is filled with deep purple wine: this "
                        f"represents an unexpected windfall. Another is filled with green poison: this represents an "
                        f"unexpected loss. The last is filled with thick red blood, and is an omen of unexpected "
                        f"violence. ",
                        "Unaligned")
the_crown = CardClass("The Crown",
                      "The Crown represents the burdens and privileges of leadership. As with most of the Unaligned, "
                      "this can have a number of interpretations, but the most frequent is generally understood to "
                      "mean that the recipient will be called upon to lead in some fashion. Sometimes, "
                      "this is a bright omen of a promotion or advancement, but it can also imply that one will need "
                      "to step up and lead in a time of crisis.",
                      "Unaligned")
the_beast = CardClass("The Beast",
                      "That which cannot be controlled. As an omen, the Beast represents a warning against attempting "
                      "to command uncontrollable forces. It may be seen as a call  to re-evaluate priorities and "
                      "redirect one’s energies… or a command to break free of someone else’s control. ",
                      "Unaligned")
the_consort = CardClass("The Consort",
                        "Distinct from the Maiden, the Consort does not necessarily imply marriage, though it may. It "
                        "is a symbol of alliance or partnership, whether romantic or otherwise. It foretells the "
                        "founding of a mutually beneficial relationship, or the importance of an existing one.",
                        "Unaligned")
the_maiden = CardClass("The Maiden",
                       "One of the more pleasant omens of the Unaligned, the Maiden symbolizes nothing more or less "
                       "than love. Drawing this card implies that love will take a major role in the recipient’s "
                       "fate. Most hope that this means they will fall in love, but it can also imply that they "
                       "should look to existing love for comfort and strength, or to focus on restoring and renewing "
                       "that love. ",
                       "Unaligned")
the_man_in_chains = CardClass("The Man In Chains",
                              "Recalling images of the Saen’dal’s eternal foes, the soul-stealing Three Sisters, "
                              "the Man in Chains represents slavery, of the body and soul. It is among the worst "
                              "cards one can draw, and proclaims that the subject (whether the recipient or someone "
                              "close to them) is nearly damned, and must devote him- or herself to breaking their "
                              "chains. ",
                              "Unaligned")
the_ghost = CardClass("The Ghost",
                      "In ancient Saen’dal cosmology, Ghost signified the souls that had not been saved by their "
                      "Warden, and were doomed to wander the dusty wastes of the afterlife. As a symbol, "
                      "the Ghost means simply “that which cannot be saved.” Drawing it means that something in the "
                      "recipient’s life is futile: a friend’s struggle with addiction may be doomed, "
                      "or one’s marriage gone beyond hope of repair. It is an admonition against breaking oneself to "
                      "achieve the impossible. ",
                      "Unaligned")
death = CardClass("Death",
                  "The darkest omen of the Deck, Death is simple: the recipient will die, whether physically or "
                  "spiritually. A physical death’s implications are obvious, but a spiritual one has more interesting "
                  "consequences: usually, the death of a belief, the loss of faith, or that the end of one’s path in "
                  "life will come far sooner than expected.",
                  "Unaligned")
rebirth = CardClass("Rebirth",
                    "The brightest of the Deck’s omens, Rebirth foretells a renewal of life. A restoration of hope, "
                    "the opening of closed doors, the birth of a new generation, or simply a new day dawning over the "
                    "darkness of one’s life. In the rare occasion that Rebirth and Death are found in the same hand, "
                    "their meanings are married to one another: the recipient will suffer, even to the point of "
                    "emotional or spiritual death… but their suffering will not be in vain, and they will be reborn "
                    "stronger, wiser, and more complete than before.",
                    "Unaligned")

errored_card = CardClass("Error", "This card doesn't actually exist; it was given in error!", "Unaligned")

# for p in CardClass.registry:
#     print(p.n)

# for p in CardClass.registry:
#     p.show()
#     print(p.explain())
