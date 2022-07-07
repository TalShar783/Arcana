from enum import Enum
import Rolls
import random


class LegendaryWeapons(Enum):
    GLORY = "Glory, the supreme Bow of Light"
    SUBTLETY = "Subtlety, the supreme Spear of Shadow"
    FURY = "Fury, the supreme Axe of Fire"
    INSIGHT = "Insight, the supreme Rapier of Water"
    LIBERATION = "Liberation, the supreme Staff of Air"
    RESILIENCE = "Resilience, the supreme Hammer of Earth"
    DEVOTION = "Devotion, the supreme Mace of Life"
    HATRED = "Hatred, the supreme Longsword of Death"


class ShamanismPaths(Enum):
    ELENDAS = "Elendas"
    DEST = "Dest"
    MOROK = "Morok"
    LAVE = "Lave"
    URGAR = "Urgar"
    IRAHZ = "Irahz"
    KALUMERE = "Kalumere"
    ASHALANARIS = "Ashal’anaris"
    MERLU = "Merlu"
    SEYU = "Seyu"
    ARGAI = "Argai"
    STADAR = "Stadar"
    ANASK = "Anask"
    ELDARA = "Eldara"
    DERAK = "Derak"
    ANDAI = "Andai"
    FRAY = "Fray"
    PALEUS = "Paleus"
    SERATIS = "Seratis"
    PYRAEN = "Pyraen"
    KARASHARR = "Karasharr"
    XENAI = "Xenai"
    HYDRA = "Hydra"
    ISHALAH = "Ishalah"
    AQUIRIS = "Aquiris"
    MIMYR = "Mimyr"
    LINNEKAL = "Linnekal"
    VAYN = "Vayn"
    EANNAS = "Eannas"
    LYRIAN = "Lyrian"
    ZELIAN = "Zelian"
    KASSIAN = "Kassian"
    SEKTARA = "Sektara"
    ARIOLAN = "Ariolan"
    ROLAAN = "Rolaan"
    MARDA = "Marda"
    NIARAN = "Niaran"
    ORDAN = "Ordan"
    WORLDSPEAKER = "Worldspeaker"
    HANALURIS = "Hanaluris"
    ANTARIS = "Antaris"
    AURYNN = "Aurynn"
    DRAKARYN = "Drakaryn"
    JULIAN = "Julian"
    AMAKARI = "Amakari"
    ZAKAL = "Zakal"
    NYX = "Nyx"
    SHARRAKAL = "Sharrakal"
    NETHERYS = "Netherys"
    ZAREKKAR = "Zarekkar"
    SIREN = "Siren"
    ELYSAL = "Elysal"
    ANISTERIUS = "Anisterius"
    GWENARIS = "Gwenaris"


class WildMagicRolls(Enum):
    ONE = f"You teleport {Rolls.rollDice(1, 10)} squares, directly toward the nearest enemy."
    TWO = f"You explode in a chaotic fireball and take {Rolls.rollDice(5, 10)} Chaos damage. Each adjacent creature takes half as much damage."
    THREE = f"You gain vulnerable 5 to {Rolls.chooseElement()} damage until the end of the day."
    FOUR = f"You transform into a potted plant until the start of your next turn. As a plant, you have vulnerable 10 to all damage."
    FIVE = f"You gain resist 10 to {Rolls.chooseElement()} damage until the end of the day."
    SIX = f"You teleport {Rolls.rollDice(1, 10)} squares in the direction of your choice."
    SEVEN = f"You deal {Rolls.rollDice(5, 10)} Lightning damage to up to 3 targets in a close burst 10."
    EIGHT = f"You transform into another race for 24 hours (DM rolls randomly)."
    NINE = f"You drain a point of Resolve from your two nearest allies and gain a Shield equal to their combined surge value."
    TEN = f"You use Chaos Bolt as a free action."
    ELEVEN = f"You can spend a point of Resolve to take a healing surge and regain {Rolls.rollDice(5, 6)} additional Health."
    TWELVE = f"You recharge an Encounter power of your choice."
    THIRTEEN = f"You phase fully into the Aether. You return at the start of your next turn."
    FOURTEEN = f"You summon {Rolls.rollDice(1, 6)} Lomath Leaper-Beasts that are frightened of you. They disappear 1 minute later."
    FIFTEEN = f"You gain resist 25 to all damage until the end of your next turn."
    SIXTEEN = f"You immediately use the 4-Charge manifestation of {random.choice(list(ShamanismPaths)).value} (you don’t pay the Charge Cost)."
    SEVENTEEN = f"You use Chaos Bolt as a free action. It deals Chaos damage instead of its normal type."
    EIGHTEEN = f"You recharge a Daily power of your choice."
    NINETEEN = f"You summon the legendary {random.choice(list(LegendaryWeapons)).value}. It remains until the end of your next turn."
    TWENTY = f"You use Chaos Bolt as a free action. It automatically rolls a natural 20."


def WildMagicSurge():
    return random.choice(list(WildMagicRolls)).value

