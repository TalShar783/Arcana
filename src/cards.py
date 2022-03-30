import random

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
            return(self.n)
        except AttributeError | IndexError:
            return errored_card.n

    def explain(self):
        try:
            return self.d
        except AttributeError | IndexError:
            return errored_card.d

    def getHouse(self):
        try:
            return self.h
        except AttributeError | IndexError:
            return errored_card.h

    def rollChalice(self):
        switcher = {
            1: "It is filled with glistening red blood.",
            2: "It is filled with nauseating green poison.",
            3: "It is filled with rich purple wine."
        }
        roll = switcher.get(random.randint(1, 3), "Invalid")
        return roll




lord_of_ice = CardClass("Lord of Ice",
                        "Originally representative of Archon Asrahmat, the Warden of Souls, creator of the Amaraen’dal, the Society of Light. Now associated equally with Illeonai Raivan, the High King of Livania.",
                        "Ice")
lady_of_ice = CardClass("Lady of Ice",
                        "Originally representative of Silanah, the favored daughter of Asrahmat and spiritual guide of the Amaraen’dal. Now represents her as the Warden of Souls.",
                        "Ice")
sage_of_ice = CardClass("Sage of Ice",
                        "Represents the Four Pillars, the Archangels,  of the Angels of Death, the elite leadership of the Warden’s holy warriors and priests.",
                        "Ice")
servant_of_ice = CardClass("Sage of Ice",
                        "Represents the Angels of Death as an organization, the servants of justice and salvation in the Society of Light, and later, in the Livanian Empire.",
                        "Ice")
protection = CardClass("Protection",
                       "Represents guardianship and safekeeping, specifically the Warden and her servants’ salvation of the souls of the dead.",
                       "Ice")
winter = CardClass("Winter",
                       "Historically represented Tharyd, specifically the Society of Light and the domains of the north, beneath the Tower of Ice. Now associated with the Livanian Empire.",
                       "Ice")

lord_of_fire = CardClass("Lord of Fire",
                       "Historically associated with the Four Archdemons, the highest powers of Hell.",
                       "Fire")
lady_of_fire = CardClass("Lady of Fire",
                        "Historically associated with temptresses and deceivers, usually of the demonic variety.",
                        "Fire")
demon_of_fire = CardClass("Demon of Fire",
                         "Historically representative of Demons, the soldiers in the armies of Hell.",
                         "Fire")
slave_of_fire = CardClass("Slave of Fire",
                         "Represents souls entangled and controlled by the plots and powers of Hell, willing or not.",
                         "Fire")
destruction = CardClass("Destruction",
                         "Represents active destruction and devastation, unleashed by the Four Archdemons upon the souls and lives of the world.",
                         "Fire")
inferno = CardClass("Inferno",
                         "Represents, quite simply, Hell, and in some cases, the continent of Kansayd, domain of volcanic hellscapes and terrible monsters.",
                         "Fire")

king_of_darkness = CardClass("King of Darkness",
                    "The appearance of the King of Darkness reveals a force of malice, working to cause harm or suffering within the recipient’s life. The King of Darkness is often an impersonal force: the leader of a faction that is the source of the recipient’s woes, or the author of a tide of metaphorical darkness whose rippling effects bring misery and loss. Above all, it is a warning: one’s suffering is not random. It is the work of a malicious enemy.",
                    "Darkness")
knight_of_darkness = CardClass("Knight of Darkness",
                     "Where the King is distant, the Knight is intimate. A personal rival, a bitter foe, a cruel tormentor who knows the recipient, and whom the recipient knows in return. The appearance of the Knight often foretells direct conflict with this adversary. It means that one’s steps forward will be contested, not by fickle chance, but by an active, hostile will.",
                     "Darkness")
soldier_of_darkness = CardClass("Soldier of Darkness",
                     "Where the King is distant, and the Knight is intimate, the Soldiers are faceless but immediate. They are pawns, for whom the recipient is but one face among many. The appearance of the Soldier indicates coming hardship and conflict. Most often, this will be a battle in which the recipient will be outnumbered.",
                     "Darkness")
child_of_darkness = CardClass("Child of Darkness",
                     "Where the other servants of Darkness act with intent, a Child is merely the product of its circumstances. This card represents the unintended consequences of evil; the aftershocks left in evil’s wake that do its work unbeknownst to it. The appearance of the Child foretells the fallout from the King’s schemes, a twist of fate or betrayal as a result of evil deeds. ",
                     "Darkness")
chaos = CardClass("Chaos",
                     "Represents the chaos and bereavement that are the fulfillment of the King of Darkness’ plans. Foretells a time of uncertainty, fear, and loss for the recipient.",
                     "Darkness")
the_desert = CardClass("The Desert",
                      "Represents the aftermath of evil, the lifelessness left in the wake of Darkness. Foretells the fall or defilement of familiar places, a loss of a home or haven.",
                      "Darkness")

queen_of_light = CardClass("Queen of Light",
                       "One of the brightest omens the Saen’dal Arcana can bestow, the Queen of Light is the equal and opposite of the King of Darkness. Her appearance indicates the presence in one’s life of a benefactor or provider who wishes to see the recipient succeed. She is an omen of hope: no matter how dark one’s circumstances may seem, the Queen reaches out with support and charity, even if she is unseen.",
                       "Light")
hero_of_light = CardClass("Hero of Light",
                       "The Queen’s presence is often distant or subtle, yet the Hero’s is visible and immediate. His appearance indicates an ally, a friend, a comrade-in-arms, one who will bear the struggles and trials of life alongside the recipient. Drawing the Hero may foretell the arrival of a champion, or it may simply indicate that one is not so alone as he or she believes.",
                       "Light")
painter_of_light = CardClass("Painter of Light",
                       "The Painter does not wield the power or influence of the Queen, nor the shining sword of the Hero, but she is a foe of the Darkness all the same. Her appearance indicates something of beauty and worth in the recipient’s life: a bastion to which one can retreat in the face of suffering and loss, whether she takes the form of a person, a work of art, or a simple pleasure from which the recipient might draw strength. If the Painter appears, one should devote himself to the search for beauty in his life; often, it will be lurking nearby, unseen.",
                       "Light")
sword_of_light = CardClass("Sword of Light",
                       "Represents the Keystones and their bearers, the six elite champions who represent the best of their species.",
                       "Light")
order = CardClass("Order",
                       "Represents unity and stability, the Phaen peace that covered Arion during their reign as its masters.",
                       "Light")
the_sea = CardClass("The Sea",
                       "Represents the Sea of Sorrows which once contained Phaedyn, and the Tower of Light that is all that remains of the Phaen.",
                       "Light")

the_tower = CardClass("The Tower",
                    "An ambiguous card, representing defense and resilience. Historically, it also represents the six Towers, the masterworks of the Phaen that sustain Arion’s shattered heart.",
                    "Unaligned")
the_fist = CardClass("The Fist",
                      "An ambiguous card, representing military power. Thought to recall images of the armies of the Phaen, during the great First War.",
                      "Unaligned")
the_sceptre = CardClass("The Sceptre",
                      "An ambiguous card, representing political power. Thought to recall images of Prince Lethen’s Sceptre, by which he ruled the southern kingdoms of Tharyd in ancient days.",
                      "Unaligned")
the_chalice = CardClass("The Chalice",
                      f"An ambiguous card, representing unforeseen circumstances. Thought to recall images of Prince Lethen’s drinking cup, which was eventually recovered and used by Archon Asrahmat.",
                      "Unaligned")
the_crown = CardClass("The Crown",
                      "An ambiguous card, representing sovereignty and leadership. Thought to recall images of the Crown of Light, worn by Archon Asrahmat in the days of the Amaraen’dal, the Society of Light.",
                      "Unaligned")
the_beast = CardClass("The Beast",
                      "Represents the Dragons, the great beasts that fought at Altherion’s side during the First and Second Wars, and who rule over the lands of Sunyd.",
                      "Unaligned")
the_consort = CardClass("The Consort",
                      "An ambiguous card, representing sexuality or marriage. Thought to recall images of the Silver Queen, the wife of Archon Asrahmat and the mother of Silanah and her sisters.",
                      "Unaligned")
the_maiden = CardClass("The Maiden",
                      "An ambiguous card; representing true love. Thought to recall images of a young Silanah, when hers was the most sought-after hand in all of the Amaraen’dal.",
                      "Unaligned")
the_man_in_chains = CardClass("The Man In Chains",
                      "A feared card; represents the Three Sisters and their machinations, as well as the damned souls trapped in their thrall.",
                      "Unaligned")
the_ghost = CardClass("The Ghost",
                      "Represents the spirits of the dead, as well as the Lost Realm that lies in wait for those the Angels cannot save.",
                      "Unaligned")
death = CardClass("Death",
                      "The darkest of all omens; represents death, though also has a deeper tie to the Devourer, the ultimate enemy of life, who consumes the souls of the Lost dead.",
                      "Unaligned")
rebirth = CardClass("Rebirth",
                      "A bright omen, representing new life, thought to recall the rebirth of the Phaen way at the beginning of the Amaraen’dal, or the restoration of the Warden at the founding of Livania.",
                      "Unaligned")

errored_card = CardClass("Error", "This card doesn't actually exist; it was given in error!", "Unaligned")


# for p in CardClass.registry:
#     print(p.n)

# for p in CardClass.registry:
#     p.show()
#     print(p.explain())
