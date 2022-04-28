# %%
import holdem as h
import game as g

initial_deck = g.complete().deck

hand = ['tc', 'qc']
opened = []

visible = g.visible_cards(hand,opened)


deck = g.deck(visible,initial_deck)

# cards_straight = g.cards_to_straigh_flush(visible,2,deck)

cards_royal_straight = g.cards_to_straigh_flush(visible,deck,royal=True)

print(cards_royal_straight)
# %%
