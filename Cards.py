# we're going to make a class (Card), that instantiates a card with a name, power, toughness, and card type

class Card:
    def __init__(self, name, power, toughness, creature_type):
        self.name = name
        self.toughness = toughness
        self.power = power
        self.creature_type = creature_type

