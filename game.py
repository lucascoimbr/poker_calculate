#%%
suits = ("S", "C", "H", "D")
suit_weight = {"S":100, "C":200, "H":300, "D":400}

ranks_string = '23456789TJQKA'

class card:

    # Strings must be in format TS, AH, 4D, etc.
    def __init__(self, card_string):
        self.value, self.suit = card_string[:-1].upper(), card_string[-1].upper()
        self.suit_index = ranks_string.index(self.value)+1
        self.numeric_representation = suit_weight[self.suit]+self.suit_index

class complete:
    # create a complete deck

    def __init__(self):
        deck = []
        for rank in ranks_string:
            for suit in suits:
                deck.append(rank.upper()+suit.upper())
        
        self.deck = deck

def visible_cards(hand,open_cards):
    hand = list(map(lambda x: x.upper(), hand))
    open_cards = list(map(lambda x: x.upper(), open_cards))

    return set(hand + open_cards)

def deck(visible_cards,current_deck):
    # get the deck after all the open cards + hand

    deck = list(set(current_deck) - set(visible_cards))

    return deck

def cards_to_straigh_flush(visible_cards,deck,royal=False):


    cards_to_be_opened = 5 - (len(visible_cards) - 2)

    visible_numeric_representation = list(map(lambda x: card(x).numeric_representation, visible_cards))

    #Minimum set of cards necessaire
    minimum_cards = [1,2,3,4,5,6]
    for num in visible_numeric_representation:

        suit_group = int(num/100)*100
        left_range = -1*min(num - suit_group,4)

        if not royal:
            for i in range(left_range,1):
                left_border = num+i
                right_border = num+i+5
                rank_group = list(range(left_border, right_border))
            
                necessaire_cards = list(set(rank_group) - set(visible_numeric_representation))

                if len(necessaire_cards) < len(minimum_cards):
                    minimum_cards = necessaire_cards
        else:
            left_border = suit_group+9
            right_border = suit_group+14
            rank_group = list(range(left_border, right_border))

            necessaire_cards = list(set(rank_group) - set(visible_numeric_representation))

            if len(necessaire_cards) < len(minimum_cards):
                    minimum_cards = necessaire_cards
    
    #probability of getting this rank
    p = 0
    all_cards = len(deck)

    if len(minimum_cards) <= cards_to_be_opened:
        p = 1
        for i in minimum_cards:
            p = p*1/all_cards
            all_cards -=1
    return p