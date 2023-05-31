class Event:
    def __init__(self, isAttack=False):
        self.isAttack = isAttack
        self._advance = False

    def advance(self, state):
        raise NotImplementedError("Must be created for each event")


class EventDrawCard(Event):
    def __init__(self, player):
        super().__init__()
        self.player = player

    def advance(self, state):
        state.drawCard(self.player)
        return True
    
class EventDiscardCard(Event):
    def __init__(self, player, card, zone):
        super().__init__()
        self.player = player
        self.card = card
        self.zone = zone

    def advance(self, state):
        return True
    
