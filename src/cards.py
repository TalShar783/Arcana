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
                    "Historically representative of Altherion, the architect of all suffering for the children of the Phaen, though often refers to Elimatar now that he has gained ascendancy over his father.",
                    "Darkness")
knight_of_darkness = CardClass("Knight of Darkness",
                     "Historically representative of Elimatar, the blade of Darkness that destroyed everything the Saen’dal and their makers held dear.",
                     "Darkness")
soldier_of_darkness = CardClass("Soldier of Darkness",
                     "Representative of the Ul’ssan, the generals and commanders who waged the First War against the Phaen and their children, and who lurk beneath the world plotting vengeance.",
                     "Darkness")
child_of_darkness = CardClass("Child of Darkness",
                     "Representative of the Dak’ashi, Lomath, and the other spawn of Altherion’s machinations and the minions of True Darkness.",
                     "Darkness")
chaos = CardClass("Chaos",
                     "Represents suffering, chaos, disorder, and the dissolution of society; the defeat of the Phaen and the triumph of Altherion.",
                     "Darkness")
the_desert = CardClass("The Desert",
                      "Represents Kaladyn, the wastelands from which the threat of Altherion and the forces of Darkness arose.",
                      "Darkness")

queen_of_light = CardClass("Queen of Light",
                       "Represents the Mother of All, creator of the Saen’dal, Avun, Shayen, Berellen, and Apsaeri.",
                       "Light")
hero_of_light = CardClass("Hero of Light",
                       "Represents Fleetmaster Dasion, the heroic leader of the Phaen, champion of the Mother.",
                       "Light")
painter_of_light = CardClass("Painter of Light",
                       "Represents the Architects, the leaders of the Phaen who designed the biomes and biology of Arion, and who built the legendary technologies upon which they relied.",
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
the_man_in_chains = CardClass("The Main In Chains",
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
