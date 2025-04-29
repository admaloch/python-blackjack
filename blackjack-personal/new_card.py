#modules
import random
from utils import update_total

# for generating a new card dict

#generate random rank
def gen_rank():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return random.choice(ranks)

#genreate suit
def gen_suit():
    suits = ["♣️", "♠️", "♥️", "♦️"]
    return random.choice(suits)

#calculate input
def calc_card_val(rank_input, input_total):
    card_val = 0
    if rank_input == 'J' or rank_input == 'Q' or rank_input == 'K':
        card_val = 10
    elif rank_input == "A": #if new total is over 21 it will be 1
        if input_total + 11 > 21:
            card_val = 1
        else:
            card_val = 11
    else:
        card_val = int(rank_input) 
    return card_val


def gen_new_card_item(hand):
    total = update_total(hand) or 0
    suit = gen_suit()
    rank = gen_rank()
    val = calc_card_val(rank, total)
    return {"card": rank + suit, "value": val}
