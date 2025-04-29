# Modules
from update_ace import update_ace_val
from new_card import gen_new_card_item
from utils import update_total, delayed_print

player_hand = [] #ex {'card': 'A♦️', 'value': 11},
dealer_hand = []
player_total = 0
dealer_total = 0
is_game_active = True

# *** Start game ***
while is_game_active:
    # *** Intro ***
    print('***** Blackjack *****')
    delayed_print('Welcome to the Blackjack table')
    delayed_print('Starting round')
    delayed_print('Dealer drawing cards...')
    #generate dealer initial card
    for i in range(2):
        # initial draw for dealer and player
        dealer_card = gen_new_card_item(dealer_hand)
        dealer_hand.append(dealer_card)
        player_card = gen_new_card_item(player_hand)
        player_hand.append(player_card)
    delayed_print(f"Dealer draw: {dealer_hand[0]["card"]}")
    delayed_print(f"Player draw: {player_hand[0]["card"]}")
    delayed_print(f"Dealer draw: {dealer_hand[0]["card"]} X")
    delayed_print(f"Player draw: {player_hand[0]["card"]} {player_hand[1]["card"]}")


    # *** Player turn ***
    is_player_turn_active = True
    while is_player_turn_active:
        # determine curr player sum of valu
        player_total = update_total(player_hand)
        # convert curr hand into a string to print
        player_cards = " ".join(card["card"] for card in player_hand)
        if  player_total > 21:
            #run to update ace val of 11 to 1
            player_hand = update_ace_val(player_hand)   
            player_total = update_total(player_hand)
            if player_total > 21:
                delayed_print(f"Player Hand: {player_cards} -- Total: {player_total}")
                delayed_print('Bust!')
                is_player_turn_active = False
                break
        if  player_total > 0:
            delayed_print(f"Player Hand: {player_cards} -- Total: {player_total}")
        if len(player_hand) == 2 and player_total == 21:
            delayed_print('***** BlackJack!! *****')
            is_player_turn_active = False
            break
        player_input = input("Hit or stay? ").strip().lower()
        if player_input == "hit" or player_input == "h":
            #gen new card
            new_card = gen_new_card_item(player_hand)
            player_hand.append(new_card)
            delayed_print(f"Player hit! -- {new_card["card"]}")
        elif player_input == "stay" or player_input == "s":
            delayed_print('Player stays')
            is_player_turn_active = False
        else:
            delayed_print('Invalid input: Type Hit or Stay')
    delayed_print('-------')    
    delayed_print('Begin dealer turn')
    delayed_print(f'Hidden card revealed: {dealer_hand[1]["card"]}')

    # *** dealer turn ***
    is_dealer_turn_active = True
    while is_dealer_turn_active:
        dealer_total = update_total(dealer_hand)
        # Concatenate hand into str to print
        dealer_cards = " ".join(card["card"] for card in dealer_hand)
        if  dealer_total > 21:
            #run to update ace val of 11 to 1
            dealer_hand = update_ace_val(dealer_hand)   
            dealer_total = update_total(dealer_hand)
            if dealer_total > 21:
                delayed_print(f"Dealer Hand: {dealer_cards} -- Total: {dealer_total}")
                delayed_print('Bust!')
                is_dealer_turn_active = False
                break
        if  dealer_total > 0:
            delayed_print(f"Dealer Hand: {dealer_cards} -- Total: {dealer_total}")
        if len(dealer_hand) == 2 and dealer_total == 21:
            delayed_print('***** BlackJack!! *****')
            is_dealer_turn_active = False
            break
        if  dealer_total > 16:
            delayed_print('Dealer stays')
            is_dealer_turn_active = False
            break
        #gen a rand and suit for new card
        new_card = gen_new_card_item(dealer_hand)
        dealer_hand.append(new_card)
        delayed_print(f"Dealer hit! -- {new_card["card"]}")
    delayed_print('Dealer round complete')
    delayed_print('-----')

    # *** Final Results ***
    delayed_print('Final results:')
    delayed_print(f"Player total: {player_total} -- Dealer total: {dealer_total}")
    if (player_total > 21 and dealer_total > 21) or (player_total == dealer_total):
        delayed_print('Draw!')
    elif (player_total > dealer_total and player_total <= 21) or (player_total <= 21 and dealer_total > 21): # Use <= 21 for clarity
        delayed_print('Player Wins!!!!')
    else:
        delayed_print('Dealer Wins :(')
    is_game_active = False
    delayed_print('-----')
    delayed_print('Round over!')
    delayed_print('Restart the program to play again unless you are afraid you will lose 😈!')