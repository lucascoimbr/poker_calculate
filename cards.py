#%%

import this


suits = ("S", "C", "H", "D")

ranks_string = '23456789TJQKA'

# %%

class card:

    # Strings must be in format TS, AH, 4D, etc.
    def __init__(self, card_string):
        self.value, self.suit = card_string[:-1].upper(), card_string[-1].upper()
        self.suit_index = ranks_string.index(self.value)

class complete:
    # create a complete deck

    def __init__(self):
        deck = []
        for rank in ranks_string:
            for suit in suits:
                deck.append(rank.upper()+suit.upper())
        
        self.deck = deck

def deck(hand,open_cards,complete_deck):
    # get the deck after all the open cards + hand

    hand = list(map(lambda x: x.upper(), hand))
    open_cards = list(map(lambda x: x.upper(), open_cards))

    visible_cards = set(hand + open_cards)

    deck = list(set(complete_deck) - set(visible_cards))

    return deck




thisCard = card('qs')
# print(thisCard.value,thisCard.suit)
# print(thisCard.suit_index)

initial_deck = complete().deck

print(deck(['ac','td'],['ac','4d','2h'],initial_deck))

