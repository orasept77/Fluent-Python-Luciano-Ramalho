import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

suit_values = dict(пики=3, черви=2, бубны=1, трефы=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)  # rank_value - порядковвый номер (у туза - 12, у 2 - 0)
    return rank_value * len(suit_values) + suit_values[card.suit]  # порядковый номер * 4 + вес из suit_values


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('ВКДТ')
    suits = 'бубны черви пики трефы'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()

# print(deck[1])
# print(len(deck))
# print(choice(deck))

for card in sorted(deck, key=spades_high):
    print(card)
