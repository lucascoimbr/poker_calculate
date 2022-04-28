# %%
import holdem as h
import game as g

initial_deck = g.complete().deck

hand = ['tc', '6c']
opened = ['2d', '3d', '4d','5d']

visible = g.visible_cards(hand,opened)

deck = g.deck(visible,initial_deck)

cards_straight = g.cards_to_straigh_flush(visible,2,deck)

print(cards_straight)
# %%
