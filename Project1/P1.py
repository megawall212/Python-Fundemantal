from p1_random import P1Random
import p1_random as p1

rng = p1.P1Random()

# Put all the variables here:

game_boolean_1 = True
games_played = -1
current_game = 0
player_hand = 0
player_card = 0
player_win = 0
dealer_win = 0
tie_game = 0

# Start blackjack game
while game_boolean_1:
    # games played and count the current game:
    games_played += 1
    current_game += 1
    # variable requiring for the loop:
    player_hand = 0
    dealer_hand = 0

    # print the game message
    print(f"START GAME #{current_game}\n")

    # deals player a card
    player_card = rng.next_int(13) + 1
    # if conditions for which card the player received
    # According to the blackjack rule
    if player_card == 1:
        print("Your card is a ACE!")
    elif 2 <= player_card <= 10:
        print(f"Your card is a {player_card}!")
    elif player_card == 11:
        print("Your card is a JACK!")
    elif player_card == 12:
        print("Your card is a QUEEN!")
    elif player_card == 13:
        print("Your card is a KING!")

    # Change face card value to 10
    if player_card >= 11:
        player_card = 10

    # Add  player hand
    player_hand += player_card
    print(f"Your hand is: {player_hand}\n")

    # Redisplay the menu
    while True:

        print("""1. Get another card
2. Hold hand
3. Print statistics
4. Exit\n""")

        print("Choose an option: ", end="")
        menu_choice = int(input().strip())
        print("")

        # Apply the blackjack rules with if conditions
        if menu_choice == 1:
            # Then deals player a card
            player_card = rng.next_int(13) + 1
            # Tell players the cards
            if player_card == 1:
                print("Your card is a ACE!")
            elif 2 <= player_card <= 10:
                print(f"Your card is a {player_card}!")
            elif player_card == 11:
                print("Your card is a JACK!")
            elif player_card == 12:
                print("Your card is a QUEEN!")
            elif player_card == 13:
                print("Your card is a KING!")

            # Change face card value to 10
            if player_card >= 11 and player_card <= 13:
                player_card = 10

            # Adding and print out the player hand
            player_hand += player_card
            print(f"Your hand is: {player_hand}\n")

            # player wins, we then do addition
            if player_hand == 21:
                print("BLACKJACK! You win!\n")
                player_win += 1
                break
            # player unfortunately lost, do subtraction
            elif player_hand > 21:
                print("You exceeded 21! You lose.\n")
                dealer_win += 1
                break

        elif menu_choice == 2:
            # Let's generate the dealer's hand
            dealer_hand = rng.next_int(11) + 16
            # print hands
            print(f"Dealer's hand: {dealer_hand}")
            print(f"Your hand is: {player_hand}\n")

# decide who wins and do increment for win/tie counters
            if dealer_hand > 21:
                print("You win!\n")
                player_win += 1
            elif dealer_hand == player_hand:
                print("It's a tie! No one wins!\n")
                tie_game += 1
            elif dealer_hand > player_hand:
                print("Dealer wins!\n")
                dealer_win += 1
            elif dealer_hand < player_hand:
                print("You win!\n")
                player_win += 1

            break

        elif menu_choice == 3:
            print(f"Number of Player wins: {player_win}")
            print(f"Number of Dealer wins: {dealer_win}")
            print(f"Number of tie games: {tie_game}")
            print(f"Total # of games played is: {games_played}")
            if games_played > 0:
                win_percentage = int(player_win / games_played * 100)
            else:
                win_percentage = 0
            print(f"Percentage of Player wins: {win_percentage}.0%\n")

        elif menu_choice == 4:
            exit()

        else:
            print("Invalid input!")
            print("Please enter an integer value between 1 and 4.")
