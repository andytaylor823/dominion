### Set up ability to load cards from CSV
# Imports
from os import path
import pandas as pd

# Load card database
src_path = path.dirname(path.realpath(__file__))
database_path = path.join(path.dirname(src_path), 'card_database.csv')
df = pd.read_csv(database_path)

# Loading function
def CardLoader(name_without_spaces):
    # Convert name to match database
    name = name_without_spaces.replace('_', ' ')

    # Require card be in database
    if name not in df['classname'].unique():
        raise ValueError(f'No card data found for "{name}" -- capitalization matters!')
    
    # Pull card's attributes from database
    row = df[df['classname'] == name].iloc[0]

    # Apply attributes to new Card object
    c = Card(name)
    for attr in row.index:
        setattr(c, attr, row[attr])

    return c


from event import *
class Card:
    def __init__(self, name):
        self.name = name

    def onPlay(self):
        pass
    
    @property
    def isPureVictory(self):
        return self.isVictory and not (self.isTreasure or self.isAction or self.isDuration)
    
    def __eq__(self, other: "Card") -> bool:
        return self.name == other.name

class LoadedCard(Card):
    def __init__(self, name):
        self = CardLoader(name)

##################
# Treasure cards #
##################

class Copper(LoadedCard):
    def __init__(self):
        super().__init__('Copper')

class Silver(LoadedCard):
    def __init__(self):
        super().__init__('Silver')

class Gold(LoadedCard):
    def __init__(self):
        super().__init__('Gold')

#################
# Victory cards #
#################

class Curse(LoadedCard):
    def __init__(self):
        super().__init__('Curse')
class Estate(LoadedCard):
    def __init__(self):
        super().__init__('Estate')
class Duchy(LoadedCard):
    def __init__(self):
        super().__init__('Duchy')
class Province(LoadedCard):
    def __init__(self):
        super().__init__('Province')
class Gardens(LoadedCard):
    def __init__(self):
        super().__init__('Gardens')

################
# Action cards #
################

class Cellar(LoadedCard):
    def __init__(self):
        super().__init__('Cellar')
class Chapel(LoadedCard):
    def __init__(self):
        super().__init__('Chapel')
class Moat(LoadedCard):
    def __init__(self):
        super().__init__('Moat')
class Harbinger(LoadedCard):
    def __init__(self):
        super().__init__('Harbinger')
class Merchant(LoadedCard):
    def __init__(self):
        super().__init__('Merchant')
class Vassal(LoadedCard):
    def __init__(self):
        super().__init__('Vassal')
class Village(LoadedCard):
    def __init__(self):
        super().__init__('Village')
class Workshop(LoadedCard):
    def __init__(self):
        super().__init__('Workshop')
class Bureaucrat(LoadedCard):
    def __init__(self):
        super().__init__('Bureaucrat')
class Militia(LoadedCard):
    def __init__(self):
        super().__init__('Militia')
class Moneylender(LoadedCard):
    def __init__(self):
        super().__init__('Moneylender')
class Poacher(LoadedCard):
    def __init__(self):
        super().__init__('Poacher')
class Remodel(LoadedCard):
    def __init__(self):
        super().__init__('Remodel')
class Smithy(LoadedCard):
    def __init__(self):
        super().__init__('Smithy')
class ThroneRoom(LoadedCard):
    def __init__(self):
        super().__init__('Throne_Room')
class Bandit(LoadedCard):
    def __init__(self):
        super().__init__('Bandit')
class CouncilRoom(LoadedCard):
    def __init__(self):
        super().__init__('Council_Room')
class Festival(LoadedCard):
    def __init__(self):
        super().__init__('Festival')
class Laboratory(LoadedCard):
    def __init__(self):
        super().__init__('Laboratory')
class Market(LoadedCard):
    def __init__(self):
        super().__init__('Market')
class Mine(LoadedCard):
    def __init__(self):
        super().__init__('Mine')
class Sentry(LoadedCard):
    def __init__(self):
        super().__init__('Sentry')
class Witch(LoadedCard):
    def __init__(self):
        super().__init__('Witch')
class Artisan(LoadedCard):
    def __init__(self):
        super().__init__('Artisan')



