
class CardClass:
    registry = []

    def __init__(self, name, description, house):
        """

        :rtype: object
        """
        self.n = name
        self.d = description
        self.h = house
        self.registry.append(self)

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


ghost = CardClass(
    "Ghost",
    "The lingering spirits of those who should have passed on, the Ghost indicates unfinished business. The longer it "
    "is left undone, the worse things will be, but the Ghost can often not bring things to a conclusion without help "
    "from those who are more capable. Depending on the context, this can mean that something the subject thought was "
    "concluded needs revisiting, an admonishment to wrap things up, or a warning that it’s time to give up a pursuit "
    "before it consumes them.",
    "Dead")
corpse = CardClass(
    "Corpse",
    "Specifically referring to the reanimated corpse, this card represents something or someone that has been kept at "
    "their purpose beyond what is healthy, usually against their will and to the detriment of their body and soul. It "
    "indicates an emptying of the vessel of warmth and meaning, and a reduction of the sacred and living to a mere "
    "tool.",
    "Dead")
vampire = CardClass(
    "Vampire",
    "Represents a parasitism of autonomy; the Vampire is unable to do many things themselves, and rather than fail or "
    "leave those things undone, they co-opt the wills of the able to see them through. The Vampire is a compulsive "
    "manipulator, be it through charm, deception, or force of personality. In hand it often represents the holder's "
    "own propensity for manipulation, or someone who wishes to use them.",
    "Dead")
wight = CardClass(
    "Wight",
    "Represents a parasitism of warmth and vitality. Just as a Wight drains the heat from their victims’ bodies, "
    "the individual or power represented by the Wight can only exist by leeching the warmth from the hearts of "
    "others. Like his monstrous antecedent, the one portrayed as the Wight will often leave his victims to rise as "
    "Wights themselves, seeking to replace the warmth stolen from them by draining it from others. In hand it "
    "represents a person or cause that will drain the life from those who associate with or pursue them.",
    "Dead")
malice = CardClass(
    "Malice",
    "Hatred and wrath. Indicates the final evolution of the Wraith, after a Ghost has lingered overlong and been "
    "consumed by a desire whose end it has long forgotten. The Malice exists now only to destroy, and hates the light "
    "of life that it will never taste again. There is no negotiation, no catharsis, no maneuvering to be done against "
    "the Malice; it must be destroyed, lest it destroy you. In hand, the Malice indicates someone who continues in a "
    "pursuit out of inertia rather than desire; they may no longer even remember why they took it up to begin with. "
    "Unlike the Corpse, the Malice's enslavement of purpose is their own doing.",
    "Dead")
necromancer = CardClass(
    "Necromancer",
    "The one who raises the Corpse; the Necromancer represents someone who takes something that is Dead and puts it "
    "to a new and profane use, pushing it beyond its natural and decent limits to serve his goals. As a card, "
    "the Necromancer often represents a relational imprisonment, keeping one or more people in an association that is "
    "detrimental to them, yet benefits the Necromancer.",
    "Dead")
grave = CardClass(
    "Grave",
    "The aspect of Death that is the Final Rest; all Undead both fear and long for the embrace of the Grave. In hand, "
    "it can represent the final closing of a matter; a door closed, never to be opened again. This can be a good or "
    "an ill omen, depending upon what is on each side of the door. Death is frequently both a tragedy and a mercy, "
    "and the concentration of each is dependent upon what was lost. ",
    "Dead")
revenant = CardClass(
    "Revenant",
    "The Revenant represents a thirst for revenge, a maniacal need to see things set right or bring ruin to those who "
    "harmed them. Unlike the Ghost, the Revenant’s unfinished business is direct and singular; they will not return "
    "to the Grave alone. This card may represent the holder or someone who is seeking vengeance against them, "
    "but in either case, that debt of blood is going to come due, and soon.",
    "Dead")
shadowlands = CardClass(
    "Shadowlands",
    "Depicts the ashen wasteland where disembodied souls exist when they cannot penetrate the veil and manifest in "
    "the physical plane. In hand, the Shadowlands indicates a place where someone has lingered overlong. It is often "
    "a call to move on, or a warning against stagnation. Nothing will change so long as the subject lingers within "
    "the Shadowlands.",
    "Dead")
silent_chorus = CardClass(
    "Silent Chorus",
    "The Silent Chorus is the name given to a ghostly zeitgeist formed by souls or fragments thereof that are not "
    "strong or driven enough to manifest as distinct apparitions. With the right respect and preparation, "
    "a necromancer or diviner can consult them for answers. In hand, it indicates the wisdom gained by experience, "
    "and urges the holder to heed the examples of the fallen.",
    "Dead")
banshee = CardClass(
    "Banshee",
    "The ancient specter of Irish origin whose keening signaled the recent or imminent death of someone dear to those "
    "who hear her. The Banshee represents grief for what is lost, and the danger of being trapped within its "
    "boundless depths. It is a warning not to wallow in grief for the Dead to the exclusion of one's appreciation for "
    "the Living; otherwise, the bereaved may find themselves reunited all too soon.",
    "Dead")
dusk = CardClass(
    "Dusk",
    "When the Night pulls her veil over the firmament and the Sun descends below the horizon, the Dead find the world "
    "a more welcome place. Be it the haunting of a Ghost, the wail of a Banshee, or the schemes of a Vampire, "
    "Dusk marks a time when darker powers gain dominion over the earth. In hand, it is a warning that the holder "
    "treads ground that does not belong to them; they are advised to shelter and wait for the Dawn, or else remain "
    "vigilant and be prepared to defend themselves.",
    "Dead")
fallen_angel = CardClass(
    "Fallen Angel",
    "Depicts a white-feathered winged man falling through the air, his wings aflame, leaving tattered black remnants. "
    "Many forget that each Demon was once an Angel. The Fallen Angel represents rebellion, and the deadly sin of "
    "Pride that inspires it. In hand, it serves as a warning not to overestimate one's ability, and is typically "
    "interpreted as an ill omen for anyone about to undertake an ambitious task.",
    "Damned")
dragon = CardClass(
    "Dragon",
    "Often depicted in ancient art as agents of the Devil, the Dragon is often seen as hoarding and guarding piles of "
    "gold, gems, and other valuables. It is a ready representation of the deadly sin of Greed, and often serves as an "
    "admonishment for the holder to be content with what they already have.",
    "Damned")
succubus = CardClass(
    "Succubus",
    "Some demonologists hold that Succubi prefer to smother their victims in their sleep. In hand, the Succubus "
    "represents the deadly sin of Sloth, and serves as a warning that the time will soon come that they will be "
    "called to action, and that they must not hesitate when that time arrives.",
    "Damned")
salome = CardClass(
    "Salome",
    "Daughter of Herodias and Herod II, Salome is said to have danced for her stepfather Herod Antipas and so pleased "
    "him and his guests that he promised her anything she desired, up to half his kingdom. Prompted by her mother, "
    "she requested the head of John the Baptist on a platter, which Herod was obligated to provide. She represents "
    "the deadly sin of Lust, which brings people to ruin by clouding their judgment and narrowing their view until "
    "they can think of nothing but their immediate desires. It is a warning for the holder not to seek or value "
    "fleeting pleasure, for it is often a hook in the mouths of the unwary.",
    "Damned")
grendel = CardClass(
    "Grendel",
    "Depicts the monster from the ancient poem Beowulf, which consumed its foes to feed its ravenous hunger, "
    "eventually leading to its own destruction. This card represents the deadly sin of gluttony: of letting one’s "
    "instinctive drive to consume, consume them in turn. In hand, it is an admonishment to take only what one needs, "
    "and not an ounce more.",
    "Damned")
claw = CardClass(
    "Claw",
    "When Temptation and Possession fail, a particularly tenacious Demon may leash out directly; a triple claw mark "
    "is often the sign of a demonic attack, as well as a mark to indicate the subject of their rage. The Claw thus "
    "represents the deadly sin of Wrath, and indicates a focused, personal desire for the destruction or debasement "
    "of another.",
    "Damned")
ahriman = CardClass(
    "Ahriman",
    "Ancient Greeks held that the eyes of the envious could lay a curse upon those who received their stare. The "
    "demon known as Ahriman is often depicted as a great, winged eye, representative of the deadly sin of Envy. It is "
    "often interpreted as an admonishment that the holder already has what they need to fulfill their undertaking.",
    "Damned")
patient = CardClass(
    "Patient",
    "The target of demonic attention. The Patient represents someone who is being intentionally corrupted, usurped, "
    "or oppressed. It is said that Demons latch on to individuals and devote their attention to them the way a doctor "
    "might to their patient. This card speaks of a tenacity and possessiveness on the part of the Demon; they do not "
    "let their Patients go easily. In hand, it represents a foe who wants something from the subject, and will not "
    "rest until they get it.",
    "Damned")
serpent = CardClass(
    "Serpent",
    "Demons prefer to tempt their Patients into performing and indulging in evil deeds, just as their supposed leader "
    "did to the first Man and Woman in that mythical Garden. In hand, the Serpent indicates an ongoing test of will, "
    "where failure carries dire consequences. The temptation posed by the Serpent will not be a single instance, "
    "to be passed or failed and then moved beyond, but rather a test of endurance as the Serpent tries again and "
    "again to achieve its goals.",
    "Damned")
possession = CardClass(
    "Possession",
    "When the Serpent of temptation fails, a Demon may often resort to outright Possession, taking direct control of "
    "their Patient. In hand, Possession represents someone whose actions are being manipulated or dictated without "
    "their knowledge or without their consent.",
    "Damned")
hell = CardClass(
    "Hell",
    "It is a misinterpretation that Hell serves as the headquarters of the Damned, or that they hold some special "
    "station of power there. In truth, they shall suffer Hell more than anyone, for they alone understood the "
    "consequences of their rebellion before they committed it. In hand, Hell represents the foreseen, "
    "warned-of consequences of Pride, or the bad end of a gamble or risk that was taken willingly.",
    "Damned")
the_black_tower = CardClass(
    "The Black Tower",
    "Often depicted as an office building or seat of government rising against a slate sky spiderwebbed with crimson "
    "lightning. The Black Tower is a worldly edifice created to twist power and authority to serve the powers of "
    "Hell: to corrupt, steal, control, victimize, and deceive. In hand, it can often mean that one should reexamine "
    "the institutions with which they interact, and not assume that they are as just or as beneficial as they claim.",
    "Damned")
sidhe = CardClass(
    "Sidhe",
    "Representative of the proverbial and literal Courts of the Fey Folk, who are renowned for their trickery and "
    "wordplay, the Sidhe indicates a challenge in which the holder’s words and actions will be strictly judged, "
    "often by an individual who wishes to hoodwink them, or else a test whose rules are unknown to the taker. It is "
    "an omen dripping with danger, but those who outwit or please the Sidhe are often showered in riches beyond their "
    "imagining.",
    "Fae")
changeling = CardClass(
    "Changeling",
    "The Changeling has had something of a spotted history in myth and legend, often highlighting the struggle of "
    "families to survive during lean times. It is said that the Faeries would exchange human infants with children of "
    "their own, and that the Changeling child would be disagreeable, ravenous, and a source of neverending trouble "
    "for the families. Many of those who have survived the touch of the Fae have spoken to the benevolence of the "
    "Seelie Court, and insist that if they were to take a child, it would be only because the parents could not or "
    "would not care for it properly, and that the Changeling would be left as both a monitor and a punishment for "
    "their neglect. In hand, the Changeling represents a dire warning: something you love carries with it a burden of "
    "terrible responsibility, and if you fail to care for it properly, it will be given to someone more deserving.",
    "Fae")
forest = CardClass(
    "Forest",
    "The Forest was a place of both bounty and danger in the early days of Humanity. To venture into it always "
    "carried an element of risk, for to enter the Forest was to enter the Unknown, and to risk contact with the "
    "Faerie. In hand, The Forest indicates a leaving of what is comfortable in order to attain what is needful.",
    "Fae")
fairy_circle = CardClass(
    "Fairy Circle",
    "Anyone from the old lands knows better than to step into a circle of mushrooms. The Fairy Circle indicates "
    "detainment or kidnapping, where the holder or someone dear to them will be swept away and prevented from "
    "returning. Because the best way to help someone escape a faerie circle is from outside, this omen often "
    "indicates that the imprisoned will not be freed without the holder’s help.",
    "Fae")
leshy = CardClass(
    "Leshy",
    "A creature that enforces respect for the Forest, the Leshy is quite survivable to those who are humble, "
    "mild-mannered, and pay due respect to the Green. To those who are none of those things, the Leshy is a terror, "
    "and often the last thing they will ever see. In hand, the Leshy is a warning to be respectful of one’s "
    "surroundings, for you never know who is watching, and by what scales they judge you.",
    "Fae")
treant = CardClass(
    "Treant",
    "A mythical being that is said to be little more or less than an animate, sapient tree. In hand, the Treant "
    "represents someone who has put down their roots, and for better or worse, will not be moved, come Hell or high "
    "water.",
    "Fae")
spring = CardClass(
    "Spring",
    "The first half of the Seelie Court, Spring Faeries are often outgoing, if a bit shy, and have a love of "
    "cultivation. Spring is a good omen for beginnings of all kinds, and is a signal that now is the time to begin a "
    "project long planned or anticipated.",
    "Fae")
summer = CardClass(
    "Summer",
    "The second half of the Seelie Court, Summer Fae are often riotous, energetic, and eager to experience new "
    "things. Summer is an omen of the making of new friendships. It is no time to stay home!",
    "Fae")
autumn = CardClass(
    "Autumn",
    "The first half of the Unseelie Court, Autumn Fae are often detached, reclusive, and slow to trust. Autumn is an "
    "omen of impending loss and trimming away of weak or unnecessary attachments.",
    "Fae")
winter = CardClass(
    "Winter",
    "The second half of the Unseelie Court, Winter Fae are wise and insular, aloof toward all but other members of "
    "their own Court. Winter signifies a lean time, when difficulties and scarcity will drive people closer together "
    "for the sake of survival. It is often considered an ill omen, but the truth is that the surest of bonds are "
    "tempered in the Winter.",
    "Fae")
black_eyed_children = CardClass(
    "Black-Eyed Children",
    "An unusually persistent myth across the world, Black-Eyed Children are most often seen asking–and then "
    "demanding, if the inhabitants resist their enchanting presence–to be let into people’s homes or vehicles. It is "
    "generally agreed that this is some sort of test of the Fae, likely from the Unseelie Court, but no one who has "
    "“failed” their test by allowing them inside has managed to bear their tales to the keepers of lore, "
    "so no-one can know for sure. In hand, the Black-Eyed Children most often represent a warning to be especially "
    "wary in the coming season of who receives your charity and hospitality, for among them may be an imposter who "
    "seeks to harm you or someone you shelter. It can also be an indication that someone already receiving your "
    "hospitality, affection, or energy is unworthy of them, and will use them to harm you, intentionally or "
    "otherwise.",
    "Fae")
pooka = CardClass(
    "Pooka",
    "While many of the Fae are fair of countenance and mild of demeanor, even the ones of the Seelie Court are known "
    "to at times cause horrible suffering, not out of malice, but because of the differences between the Fair Folk "
    "and mortals. What a Pooka might see as a delightful favor or a hilarious jape might in truth be a harrowing "
    "experience. In hand, the Pooka represents good intentions going wrong and leading to suffering. It is thus often "
    "interpreted as an admonition to fully understand one's circumstances before taking any action.",
    "Fae")
angel = CardClass(
    "Angel",
    "Often employed as messengers, warriors, and wardens of forbidden places, one of the most popular depictions of "
    "Angels is that of an unseen Guardian. Where a Demon latches with the persistence of a parasite to their Patient, "
    "the Angel stands nearby with equal devotion, vigilant against harm. In hand, it represents a power or individual "
    "who is devoted to protecting another.",
    "Divine")
exorcism = CardClass(
    "Exorcism",
    "An ancient rite said to drive out demons and unclean spirits from place and person alike, Exorcism is the "
    "opposite to Possession - it represents a reclaiming of one’s will, an awakening to the bonds of manipulation and "
    "subjugation, and the shattering of those chains, for one’s self or another. As one cannot perform an exorcism "
    "for one’s self, Exorcism usually indicates that the liberation will come at the hands of another power "
    "benevolent toward the subject of the Possession.",
    "Divine")
vestal = CardClass(
    "Vestal",
    "Said to depict the Vestal Virgins dedicated to the Roman goddess Vesta, the term has come to have a more "
    "agnostic meaning, often depicting virginity or similar purity gained through abstinence. In hand, it represents "
    "above all a devotion to an individual or cause, to the exclusion of something else; the Vestal gains power over "
    "themselves and their circumstances by a righteous and singleminded denial of those things that would distract "
    "them.",
    "Divine")
martyr = CardClass(
    "Martyr",
    "The Martyr is a straightforward omen: someone who dies or makes a great sacrifice for the sake of others. The "
    "greatest act of love, it is said, is to lay down one’s life for another. It is a bitter omen, but ultimately a "
    "good one: the Martyr never dies in vain, and their name will be remembered on Earth and echoed eternally through "
    "the halls of Heaven.",
    "Divine")
temple = CardClass(
    "Temple",
    "The Temple is a place where individuals sharing goals or beliefs can come together and enjoy fellowship, "
    "sanctuary, and mutual education. In hand, it represents a gathering of like-minded individuals, and reminds the "
    "holder that it is dangerous to be alone for too long.",
    "Divine")
scripture = CardClass(
    "Scripture",
    "Divinely inspired or not, much can be learned from all forms of Scripture. This card represents a collection of "
    "knowledge penned by those who have gone before. It may take the form of a bestiary for a Hunter, full of the "
    "banes and weaknesses of his quarry, or a literal Scripture, with advice for life and the cultivation of the "
    "Spark within. ",
    "Divine")
judgment = CardClass(
    "Judgment",
    "Often wrongly conflated with a divine Wrath, Judgment represents above all a fair but exacting measuring of an "
    "individual’s deeds, with an aim of cutting away what falls short, for the good of the whole. In the light of a "
    "true and just Judgment, nothing will remain hidden, and only that which is unhealthy shall be cast into the "
    "fire.",
    "Divine")
redemption = CardClass(
    "Redemption",
    "The brightest of all omens, Redemption represents the end of the journey of atonement; the washing-clean of the "
    "slate, where the subject shall keep all of the wisdom learned through their adversity, and no longer suffer the "
    "scars thereof. The subject has long ago turned their back on evil, and finally, Hell’s curse has lost its grip "
    "upon them.",
    "Divine")
the_spark = CardClass(
    "The Spark",
    "It is said by some that the truest essence of the Divine is Love, and by others that the Divine Spark exists "
    "within the souls of all humans. Thus the Spark represents love in all its forms, and the power and unity that "
    "can come from it. In some contexts, the Spark can also represent the eternal hope of Redemption, even in the "
    "darkest of circumstances; no amount of darkness can blot out even the tiniest spark of light, and the Spark of "
    "the Divine is infinite and unquenchable.",
    "Divine")
the_green_chapel = CardClass(
    "The Green Chapel",
    "While the Temple facilitates closeness with the Divine through association with others who carry and cultivate "
    "the Spark within themselves, the Green Chapel is a place of solitude and reflection, often in nature, "
    "where one can look inward rather than outward. It is a time of care for one’s self, be it a time of rest and "
    "self-forgiveness, or a trial of internal reckoning. The Green Chapel represents quiet and singlemindness, "
    "an elimination of distractions, and a re-centering upon one’s goals and values.",
    "Divine")
dawn = CardClass(
    "Dawn",
    "Just as Dusk signals the dying of the Light and the dominion of the Dead over the Earth, Dawn indicates a "
    "sudden, sometimes unexpected awakening of the Light of Day, when the forces of Good and Life gain the upper hand "
    "and push back the Darkness. It is a symbol of eucatastrophe, a turn for the better against all odds.",
    "Divine")
marriage = CardClass(
    "Marriage",
    "One unfamiliar with this deck might be surprised to see depicted on this card not a happy couple standing and "
    "smiling before a cheering crowd, but a fierce and battle-worn pair standing back-to-back, covering their "
    "partner’s blind spots with their shields, their swords pointed outward at a teeming horde of shadows. Marriage "
    "represents the ultimate commitment to another: an ironclad promise that they shall put the other’s wellbeing "
    "above all else. It is the joining of causes and goals, and the promise that they shall live or die as one. In "
    "hand, this does not always represent a monogamous, exclusive, or romantic relationship, and can instead indicate "
    "a lifelong friendship or alliance, or simply trust and the safety that it can offer.",
    "Divine")
the_king_in_yellow = CardClass(
    "The King in Yellow",
    "He is known by many names, among them \"The Crawling Chaos.\" The King in Yellow represents the dangerous side "
    "of the truth, the tearing-away of the curtain before the eyes of an unprepared audience. Wherever the King in "
    "Yellow goes, Chaos follows behind him.",
    "Eldritch")
shoggoth = CardClass(
    "Shoggoth",
    "An ancient slave race bioengineered by precursors known only as The Old Ones, the Shoggoth are said to have "
    "overthrown and slaughtered their makers. In hand, it is a warning to those who would seek to leash individuals "
    "to their own will, or to make themselves masters of a power they cannot trust or control.",
    "Eldritch")
madman = CardClass(
    "Madman",
    "The victim of the King in Yellow, and truly any survivor of contact with the Old Gods. The Madman is one who has "
    "learned things that have shattered his view of reality, truths that once glimpsed cannot be denied or unlearned. "
    "Thus, the Madman represents the end of something known and comfortable by way of a shattering revelation, "
    "and being thrust into the unknown.",
    "Eldritch")
mutation = CardClass(
    "Mutation",
    "The touch of the Old Gods changes more than just the victim's mind. Mutation represents the changes undergone by "
    "those who have been forced to adapt to inhospitable circumstances; those who, rather than continue to fight for "
    "their petty view of reality, instead surrendered and allowed themselves to be changed, so that they might thrive "
    "amidst the Chaos of their new situation. This card often represents emotional or mental scars gained through "
    "prior suffering that are maladaptive for current circumstances, but it can sometimes have more literal or "
    "esoteric meanings.",
    "Eldritch")
the_stars = CardClass(
    "The Stars",
    "The Stars, astronomers say, are balls of constantly-exploding gas, impossibly large spheres of nuclear hellfire "
    "scattered over vast distances. And perhaps that is true. But anyone who spends much time gazing into the night "
    "sky knows that from the surface of our world, they are more than that. They know that, in time, that starry "
    "abyss will gaze back into you. The Stars represent realms and thoughts which can be glimpsed, imagined, "
    "but never grasped; an abyss of infinite and terrifying possibility, from which anything could spring and fall to "
    "the earth… or swallow it whole. In hand, this card is often a warning not to examine too closely those things "
    "which we take for granted, lest the holder discover maddening knowledge.",
    "Eldritch")
chaos = CardClass(
    "Chaos",
    "Said by many Eldritch scholars to be the ultimate, underlying truth of reality: that we and everything we can "
    "know are merely the dream of the Idiot God Azathoth; that there is no reason, no law, no method to the madness "
    "of our existence. That things happen not because they must, or because someone or something willed it, "
    "but simply because they can. The card Chaos speaks of what is left when our meticulously-constructed reality is "
    "stripped away. It represents both the horror and the comfort in the belief–or the knowledge–that nothing "
    "matters.",
    "Eldritch")
the_cats_of_ulthar = CardClass(
    "The Cats of Ulthar",
    "It is said that in his darkest hour on the dark side of the moon, the Dream-Quester Randolph Carter was saved "
    "from Eldritch abominations by an unexpected ally: an army of cats, with whom he had unknowingly gained rapport "
    "through his kindness to the strays in that great dream-city of Ulthar. The Cats of Ulthar represent shelter from "
    "the eldritch and strange in the shade of the mundane. This can often mean finding that something once thought "
    "innocuous held hidden depths that will make you, or simply the solace and safety offered by what is known and "
    "familiar.",
    "Eldritch")
rlyeh = CardClass(
    "Rl'yeh",
    "Ia, Rl'yeh! That sunken and cyclopean city that rests beneath the waves, where dead Cthulhu waits dreaming. That "
    "which is dead may eternal lie, and in strange eons, even death may die. Someday, Rl'yeh will rise once again "
    "from beneath the noisome ocean, its lone tenant shall awaken, and all the world and its inhabitants shall fall "
    "into the roiling pit of Chaos. Such a fate may be postponed, but never averted. As such, Rl'yeh represents the "
    "inexorable and unavoidable. Whatever this card denotes will certainly come to pass; it is just a question of "
    "where and when.",
    "Eldritch")
ghoul = CardClass(
    "Ghoul",
    "It is said that those who spend too much time wandering graveyards and contemplating the Dead and the nature of "
    "Death will find their minds, then their appetites, and finally their bodies twisted until they become Ghouls: "
    "loathsome, gibbering cannibals which subsist upon the dead, burrowing in their endless warrens beneath "
    "graveyards to take their malodorous meals. The Ghoul represents the dangers of obsession, and warns against "
    "becoming so involved with any one pursuit that one forgets how to be human.",
    "Eldritch")
the_elder_sign = CardClass(
    "The Elder Sign",
    "A geometric sigil, or sometimes a hand gesture, that seems to hold some sway over the powers of the Eldritch. "
    "The Elder Sign represents the rewards to be gained by looking deep within The Stars; while much Eldritch "
    "revelation is to the detriment of the learner, sometimes the only way to fight fire is with fire. Thus, "
    "The Elder Sign represents the gaining of mastery over something by a thorough, if maddening, understanding "
    "thereof.",
    "Eldritch")
ruins = CardClass(
    "Ruins",
    "Beneath every city lies the bones of another. There are secrets buried among those bones. Few are the places "
    "that have not known the touch of man, and none have been untouched by their Eldritch predecessors. This card "
    "represents secrets of the past, and the study thereof, often with the aim of preventing the calamity which "
    "befell one’s predecessors. It is a suggestion for the holder to look into the past for answers to their "
    "troubles.",
    "Eldritch")
the_depths = CardClass(
    "The Depths",
    "The Sea, that most bountiful of providers and facilitator of travel, holds fathomless depths where the light of "
    "the sun cannot penetrate. Abominations of nature and unimaginable horrors call The Depths home, and upon the "
    "ocean floor rest cyclopean ruins of civilizations best left forgotten. Sometimes something horrible will float "
    "or wash up to the surface which should have remained buried beneath the waves, and each time this will herald "
    "someone’s descent into madness. This card is a warning that while one might be safe on the surface, danger lies "
    "in investigation of the depths. No matter what you do, do not look down.",
    "Eldritch")
wendigo = CardClass(
    "Wendigo",
    "Native American myth holds that those who consume human flesh, or hoard too much for themselves during the lean "
    "times, gradually find that their hunger increases more and more, until it consumes their humanity, "
    "and they become a Wendigo. This card represents Hunger above all: a bestial, irresistible drive that will "
    "eventually consume the subject and turn them into a shadow of their former self. Whereas Gluttony represents "
    "consumption beyond one’s need, the Wendigo indicates a bottomless pit that can never be satisfied.",
    "Beasts")
werewolf = CardClass(
    "Werewolf",
    "Where the Wendigo represents Hunger, the Werewolf represents Rage, and the power that can be granted by its "
    "indulgence. Werewolves are known for preying first and foremost upon those they loved the most before their "
    "transformation, just as anger tends to do when it roots in the hearts of men. The Werewolf is not merely guided "
    "or controlled, but transfigured entirely by his fury, unrecognizable to those who knew him as a man. This grants "
    "him great power, but even those with supreme discipline understand that the beast within is always just one lax "
    "moment away from slipping its chains and bringing ruin to those they love.",
    "Beasts")
doppelganger = CardClass(
    "doppelganger",
    "A catchall for any phenomenon that generates a body double of a living (or dead) human, Doppelgangers have been "
    "found to be apparitions of the Dead, Shapeshifters, omens of fate, and much more besides. Ranging from "
    "benevolent and protective to malicious and alien, this card indicates that someone or something near the "
    "subject–or perhaps the subject themselves–is not what they seem. It frequently appears as a warning for the "
    "holder to judge an individual by their actions, not their words or appearance.",
    "Beasts")
skinwalker = CardClass(
    "Skinwalker",
    "The less said of this being, the better. Witches and medicine-men who have learned and employed dark, "
    "unspeakable knowledge, it is said that to mention their name is to invite their notice, which always brings "
    "calamity. This card represents an individual whose attention will destroy the subject; this individual should "
    "not be befriended, crossed, or even spoken-of. If they are glimpsed or noticed, the only survivable course of "
    "action is to pretend with all your might that you saw nothing, heard nothing, know nothing.",
    "Beasts")
unicorn = CardClass(
    "Unicorn",
    "Beings that are said to only make themselves known to the truly pure-hearted, the Unicorn represents an "
    "opportunity for those who are pure of heart or intention. To see a Unicorn, let alone to interact with one or "
    "earn its favor, is a bright omen of good fortune to come, and an indication of the subject’s trustworthiness and "
    "goodness. In hand it represents innocence and healing.",
    "Beasts")
gryphon = CardClass(
    "Gryphon",
    "Noble and beautiful, the Gryphon soars on the winds, sometimes glimpsed but never cornered or captured. The "
    "Gryphon represents freedom in all its forms, and the pure, unharnessed joy of soaring on high. Rather than the "
    "negative freedom of release from captivity, the Gryphon represents the positive freedom of having the ability to "
    "reach new heights and attain one's goals.",
    "Beasts")
phoenix = CardClass(
    "Phoenix",
    "The Phoenix is a bittersweet omen, always following a death, but promising rebirth. The Phoenix which rises from "
    "the ashes of its predecessor will rarely be identical to its prior form; this card often represents an epiphany "
    "or change of heart resulting from the loss of another, which grants new life to the survivor. More rarely, "
    "it represents the total shedding of an individual’s prior life and personality, in search of something better.",
    "Beasts")
sphinx = CardClass(
    "Sphinx",
    "The Sphinx is known to interrogate its prospective victims with riddles, consuming them if they fail to answer "
    "true. It is also fond of learning new riddles, and while it is often infuriated if it cannot guess their answer, "
    "it is a being of its word and will leave alive anyone who can confound it. In hand, the Sphinx represents a test "
    "of knowledge or cunning that the holder will soon undergo.",
    "Beasts")
basilisk = CardClass(
    "Basilisk",
    "A serpent born of strange and unlikely circumstances, the Basilisk’s gaze is said to be deadly, killing or "
    "turning to stone anyone who glimpses it. In hand, the Basilisk represents a problem or challenge that will "
    "surely be failed with disastrous consequences if the subject attempts to address it head-on; it will require a "
    "more circumspect and considered approach.",
    "Beasts")
thunderbird = CardClass(
    "Thunderbird",
    "Said by Native American legend to be a great spirit of the sky, the Thunderbird was the defender of humanity "
    "against the spirits and powers of the deep. It is said that these impossibly large birds brought thunder with "
    "their wings, lightning with their beaks, and brought lifegiving rains and storms in their wake. This card "
    "represents pure, raw power. ",
    "Beasts")
shadow = CardClass(
    "Shadow",
    "An unusually persistent and widespread myth is the existence of shadow-people. Some theorize them to be members "
    "of the Dead, others some type of Demonic activity. They are often thought to indicate warnings or threats, "
    "but the simple fact is that no one truly knows; the Shadows do not communicate in any way. The only consistent "
    "element is that whether your Shadow is a mirror doppelganger or a Hat Man, their appearance is always an "
    "occasion of pure, animal terror. In hand, the Shadow indicates an upcoming test of courage, when something the "
    "subject fears will confront them directly.",
    "Beasts")
the_moon = CardClass(
    "The Moon",
    "The Moon has a long association with temporary insanity, an episode in which someone takes leave of their "
    "senses, only to later recover them, often to the horror of what they have done. In hand it can often indicate "
    "remorse, or warn the holder to maintain strict control over their emotions.",
    "Beasts")
the_all_father = CardClass(
    "The All-Father",
    "Representing the Norse god Odin, who hung from the World Tree for nine nights and thereby learned the Runes, "
    "the All-Father represents wisdom and the process of gaining it, which is almost always painful. In hand, "
    "it is often an admonition to reflect on one’s past experiences and see if there is a lesson amidst the pain that "
    "they may soon need.",
    "Myths")
medusa = CardClass(
    "Medusa",
    "Born as a beautiful demigoddess, it is said that Medusa was ravaged by Poseidon, god of the sea, and then cursed "
    "by the goddess Athena for the crime of losing her virginity. In hand, she represents a cruel or unjust "
    "punishment that far exceeds the severity of a crime, a twisting of justice to serve its opposite.",
    "Myths")
excalibur = CardClass(
    "Excalibur",
    "Said to be both a symbol of King Arthur’s station and divine authority, and a sword of great power in its own "
    "right, Excalibur represents political or social power and those who wield it.",
    "Myths")
charon = CardClass(
    "Charon",
    "The Boatsman of the Styx is said to be the only way to legitimately enter the underworld. Ancient Greeks once "
    "buried their kindred with a coin over each eye so that they would be able to pay Charon once they arrived at the "
    "shores of the Styx, so that they could reach their afterlife. In hand, Charon represents a price that must be "
    "paid if one wishes to attain their goals.",
    "Myths")
the_knights_code = CardClass(
    "The Knight's Code",
    "Life before Death; Strength before Weakness; Journey before Destination. The Knight’s Code represents a creed or "
    "oath that binds like-minded individuals to the same course, keeps the oathbound’s feet on the righteous path, "
    "and grants them power in exchange for their devotion. The worst thing that can happen to a Knight is to be found "
    "in violation of his Code; death would be far preferable.",
    "Myths")
heimdall = CardClass(
    "Heimdall",
    "The Watcher of the Bifrost, Heimdall stands ready to sound the alarm when the winds of Ragnarok blow into the "
    "nine realms. In hand, he represents vigilance and watchfulness; if one is planning a deception when they draw "
    "this card, they would be well-served to reconsider, for nothing passes by him unnoticed.",
    "Myths")
gjallarhorn = CardClass(
    "Gjallarhorn",
    "The mythical horn that hangs from Heimdall’s belt, the voice of the Gjallarhorn will signal the beginning of "
    "Ragnarok and empty the halls of Valhalla onto the battlefield for that last great struggle. In hand, Gjallarhorn "
    "represents a clear call to decisive action. Woe to those who ignore the voice of that most urgent call.",
    "Myths")
minotaur = CardClass(
    "Minotaur",
    "An abomination born of a bull, a mortal woman, and a vindictive curse from the gods, hidden away in a labyrinth "
    "to hide it from all eyes. This card represents the horrid consequences of evil deeds or the breaking of taboos.",
    "Myths")
lights_in_the_sky = CardClass(
    "Lights in the Sky",
    "A white light shines from the midnight sky. To his senses, he immediately awakens leagues from where he was "
    "standing, with the sun rising in the east and no memory of what happened. This card often indicates that the "
    "holder is being watched, usually without their knowledge. It can also indicate that the holder has forgotten "
    "something important.",
    "Myths")
siren = CardClass(
    "Siren",
    "Said to be beautiful women who lured sailors to their deaths upon the rocky shores of their homes, "
    "a Siren represents a powerful lure and a danger in following it. This card represents a warning not to be "
    "distracted from one’s course.",
    "Myths")
hydra = CardClass(
    "Hydra",
    "The many-headed monster that was defeated by the demigod Heracles, it was said that if one severed a head of "
    "this creature, two more would spring forth to take its place. This card indicates that the holder will triumph "
    "over one of their problems, only to have more spring up as a direct result of their victory.",
    "Myths")
yggdrasil = CardClass(
    "Yggdrasil",
    "The many-headed monster that was defeated by the demigod Heracles, it was said that if one severed a head of "
    "this creature, two more would spring forth to take its place. This card indicates that the holder will triumph "
    "over one of their problems, only to have more spring up as a direct result of their victory.",
    "Myths")
hunter = CardClass(
    "Hunter",
    "A Hunter is little more or less than a human being who has chosen to hunt those which would hunt him. In hand, "
    "it often represents courage, but more than that, a forsaking of the comfortable and mundane world in order to "
    "protect it from the shadows that lurk without. It is a heroic but bitter omen; a Hunter rarely dies old and "
    "toothless, surrounded by loved ones.",
    "Hunters")
silver = CardClass(
    "Silver",
    "A bane of shapeshifters and ward against illusions, Silver represents truth and purity of intent. In hand, "
    "it is an encouragement to strike to the heart of a matter and trust in the truth to see things to an agreeable "
    "end.",
    "Hunters")
iron = CardClass(
    "Iron",
    "A bane of fae beings and symbol of mankind's mastery over nature, Iron indicates strength, ingenuity, "
    "and triumph over one's circumstances. In hand it is an encouragement to have faith in one's ability to overcome "
    "obstacles that may seem insurmountable.",
    "Hunters")
wizard = CardClass(
    "Wizard",
    "A Wizard, traditionally, is one who studies the underlying mathematics of the universe, and uses that knowledge "
    "to impose their will upon reality. In hand, it represents the use of knowledge and harnessing of greater powers "
    "to overcome one’s shortcomings. ",
    "Hunters")
witch = CardClass(
    "Witch",
    "Where the Wizard commands the mathematics of reality, the Witch whispers to the soul of the universe. The Witch "
    "represents the use of diplomacy, entreaty, “headology,” or trickery to accomplish one’s goals.",
    "Hunters")
priest = CardClass(
    "Priest",
    "The Priest is where the fingertip of God meets the outstretched hand of Man. The Priest represents the wielding "
    "of a power greater in potency and scope than one’s self; the carrying of a mantle of authority into dark places "
    "not as to use it as a tool, but rather to be used by it.",
    "Hunters")
familiar = CardClass(
    "Familiar",
    "Represents a bond with a faithful friend or ally, from which the holder can draw strength in times of need. In "
    "hand, it often indicates a source of good advice that will guide the holder through a difficult or unfamiliar "
    "situation.",
    "Hunters")
circle_of_salt = CardClass(
    "Circle of Salt",
    "A traditional ward against ghosts and most forms of ethereal travel, the Circle of Salt is one of the first "
    "tools learned by prospective Hunters. In hand, it represents a place of safety from powers that would do the "
    "subject harm.",
    "Hunters")
ritual = CardClass(
    "Ritual",
    "Practitioners of the arcane, Witches and Wizards both, utilize the Ritual to focus their will and tap into "
    "powers that do not bend easily to the mortal mind. In hand, the Ritual often indicates that there is only one "
    "right way to do something, and that attempting to improvise or failing to follow the steps will result in "
    "disaster.",
    "Hunters")
mirror = CardClass(
    "Mirror",
    "Used to unmask shapeshifters and vampires alike, the Mirror represents the gaining of advantage or clarity "
    "through a change of perspective.",
    "Hunters")
scrying = CardClass(
    "Scrying",
    "A silver ewer filled with water; reflected on the water is the image of a man stealing furtively into a dark "
    "alley. Scrying represents the gaining of knowledge through arcane or unconventional means.",
    "Hunters")
torch = CardClass(
    "Torch",
    "The profession of the Hunter is one passed down from father to son, master to apprentice. The Hunter's work is "
    "never done, so the Torch must be passed to the next generation, for unlike many of their foes, no man can live "
    "forever. In hand, the Torch represents a distinct responsibility or role that has recently been or soon will be "
    "passed down from one person to another. It is vital that they not let their flame gutter out.",
    "Hunters")
mantle = CardClass(
    "Mantle",
    "The Mantle is what gives Angels and Demons both the vast majority of their power. Fueled by the Authority of "
    "Heaven for Angels and the servitude of human souls in the case of Demons, the Mantle represents power married to "
    "responsibility or obligation. One cannot have one without the other, and to forsake the obligation is to forfeit "
    "the Mantle.",
    "Unaligned")
victim = CardClass(
    "Victim",
    "The Victim is an individual who challenges or is targeted by powers they cannot overcome. The line between "
    "Hunter and Victim often lies only in adequate preparation.",
    "Unaligned")
death = CardClass(
    "Death",
    "Represents a final farewell, though not always a literal death. Unlike many other omens, this one resonates with "
    "finality; whatever is lost will be both precious and irrecoverable.",
    "Unaligned")
the_lethe = CardClass(
    "The Lethe",
    "The river of the Underworld said to flow through the domain of the god Hypnos, The Lethe's waters were said to "
    "induce forgetfulness if consumed. In hand, The Lethe represents forgetting and the erasure of knowledge. As "
    "anyone who has tangled with the Eldritch powers can tell you, this is often a blessing, and sought out by those "
    "with wounds too deep to heal.",
    "Unaligned")
crossroads = CardClass(
    "Crossroads",
    "A worryingly common concept within supernatural lore, the Crossroads represents a liminal space, on the border "
    "between one thing and another. It is a place where many go to make dark deals or speak with beings beyond their "
    "understanding. In hand, it indicates an unlikely meeting of two powers or individuals.",
    "Unaligned")
grim = CardClass(
    "Grim",
    "The Black Dog is a common apparition, often misunderstood and feared by those who have no cause to do so. It was "
    "said in some parts of the world that the first person to be buried in a graveyard would forever have the "
    "responsibility of leading the rest to the afterlife. As a result, many societies would bury dogs there first, "
    "and the faithful hounds would then be glimpsed as great, hulking beasts prowling the graveyards, guarding them "
    "from desecration. In hand, the Grim represents a solemn and unenviable duty, faithfully discharged.",
    "Unaligned")
scales = CardClass(
    "Scales",
    "The Egyptian god Osiris was said to weigh the souls of the dead to determine their fates. The Scales represent a "
    "test of character; cunning, strength, and will do not come into this test. It is only a question of how much "
    "light is within one's heart, and how much darkness.",
    "Unaligned")
golem = CardClass(
    "Golem",
    "An ancient Jewish myth concerning the mystical art of Kabbalah, it is said that an adequately trained, "
    "faithful Rabbi could recreate the process that God used to create the first humans, breathing life into an "
    "automaton who would faithfully serve and protect the Rabbi and the Jewish people. However, many of the legends "
    "have the Golem as a loyal but unpredictable force, meaning well but often causing catastrophe in the course of "
    "its duty. In hand, the Golem usually represents an individual whose goals and intentions are aligned with the "
    "subject's, but whose judgment or preferred methods may produce an undesirable result.",
    "Unaligned")
loakerlach = CardClass(
    "Loakerlach",
    "A fiendish monster that belongs to another word, the Loakerlach is said to count the steps of its victims. In "
    "hand, the Loakerlach is an admonition not to deviate from one's plan or habits; especially where the Weird is "
    "concerned, there is safety in even the most mundane of rituals.",
    "Unaligned")
shiisa = CardClass(
    "Shiisa",
    "Great stone wards resembling lion-dog hybrids, one whose mouth yawns open, the other clamped shut. The Shiisa "
    "are placed in pairs and are believed to protect from some evils. The open-mouthed Shiisa traditionally wards off "
    "evil spirits and shares goodness, and the closed-mouth Shiisa keeps good spirits in and bad spirits out. In "
    "hand, they represent balance and the necessity thereof; one should not be entirely open or closed to those "
    "things and people without. This card is often an admonition to the holder to be discerning in what they consume "
    "and with whom they associate. ",
    "Unaligned")
kamaitachi = CardClass(
    "Kamaitachi",
    "A group of Yokai that appear as dust devils, it is said that one would trip a victim as the whirlwind engulfed "
    "them, another would cut them, and a third would numb the pain, so that the victim would not notice the wound "
    "until later. In hand, the Kamaitachi indicate that some recent harm that appeared to be an accident was in fact "
    "the result of directed malice.",
    "Unaligned")
hosogami = CardClass(
    "Hosogami",
    "Often depicted as small, nearly-microscopic demons, Hosogami were said to be the cause of smallpox in feudal "
    "Japan. The appearance of this card in hand indicates that illness will soon befall the holder’s house.",
    "Unaligned")

errored_card = CardClass("Error", "This card doesn't actually exist; it was given in error!", "Unaligned")

for p in CardClass.registry:
    print(p.n)

for p in CardClass.registry:
    p.show()
    print(p.explain())
