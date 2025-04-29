# runs when total exceeds 21
# check if there is an ace with value of 11 and change that to 1
# aces default to 1 after the first ace so there can only be one ace = 11 in a hand

def update_ace_dict(card_dict):
    if card_dict["value"] == 11:
        card_dict["value"] = 1
    return card_dict
    
def update_ace_val(hand):
    result = list(map(update_ace_dict, hand))
    return result