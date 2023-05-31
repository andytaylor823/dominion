from typing import dataclass, List
from card import Card

class Decision:
    def __init__(self):
        pass

    def isTrivial(self):
        pass


@dataclass
class DecisionResponse:
    choice: Decision = None
    singleCard: Card = None
    cards: List = [].copy()