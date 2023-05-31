from event import *


class Card:
    def __init__(self, name, cost, pointValue=0):
        self.name = name
        self.baseCost = cost
        self.basePointValue = pointValue
    
        # Cost + point value modifiers
        self.pointModifier = 0
        self.costModifier = 0

    def onPlay(self):
        pass

    @property
    def pointValue(self):
        return self.basePointValue + self.pointModifier
    
    @property
    def cost(self):
        return self.baseCost + self.costModifier
    
    @property
    def isPureVictory(self):
        return 
    
    def __eq__(self, other: object) -> bool:
        return self.name == other.name



class Chapel(Card):
    def __init__(self, id):
        super().__init__('chapel', 2)

    def onPlay(self, state):
        pass

class Estate(Card):
    def __init__(self):
        super().__init__('estate', 2, 1)

class Village(Card):
    def __init__(self):
        super().__init__('village', 3)

    def onPlay(self, state):
        state.events.append(EventDrawCard)
        state.currentPlayer.actions += 1

def CardLoader(name):
    # Load csv
    # Search for given name
    # Store all columns in that row as variables
    # add class.name = name.lower()
    pass