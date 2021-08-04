import collections
from typing import Sequence

import numpy as np
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchCard:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self) -> int:
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


french_card = FrenchCard()
print(type(french_card))
random_card: FrenchCard = choice(french_card)
print(choice(french_card))


