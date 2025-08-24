import random, art, os, re, sys

#The player and dealer's hand will be global
dealer_hand = []
player_hand = []

#Make a deck of cards (purely random, no card removal as cards are drawn)
deck = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]

def main():
    global dealer_hand, player_hand
    while True:
        #Print initial hand (player and dealer are str for the art)
        player, dealer = start_game()
        update_screen(player, dealer)

        #Ask user what to do
        while card_value(player_hand) < 21:
            action = input("What do you want to do? (Hit or Stand) ")
            player = act(action)
            update_screen(player, dealer)
            if re.search(r"S(tand)?$", action, re.IGNORECASE):
                break

        #Determine the outcome of the game
        if end_game(dealer_hand, player_hand):
            print(art.text2art(f"You Win! Dealer had {card_value(dealer_hand)}", font="small"))
        else:
            update_screen(player, "".join(dealer_hand))
            print(art.text2art(f"You Lose :( Dealer had {card_value(dealer_hand)}", font="small"))

        #Ask player if they want to keep playing
        x = input("Do you want to keep playing? (y/n) ")
        while True:
            if re.search(r"^Y(es)?$", x, re.IGNORECASE):
                #Reset hands
                dealer_hand = []
                player_hand = []
                break
            elif re.search(r"^N(o)?$", x, re.IGNORECASE):
                print(art.text2art("Thanks for playing :)", font="small"))
                sys.exit()
            else:
                x = input("Do you want to keep playing? (y/n) ")


#Function that draws everything to the terminal (takes input str w/o spaces for printing)
def update_screen(player, dealer):
    os.system("clear")
    print(art.text2art("Dealer", font="small"))
    print(art.text2art(dealer,font="card",chr_ignore=True))
    print(art.text2art(f"You: {card_value(player_hand)}", font="small"))
    print(art.text2art(player,font="card",chr_ignore=True))

#Start gameplay loop, return str (testable)
def start_game():
    #Deal initial hand
    for _ in range(2):
        #Convert the random choice to a string before putting it in the list
        dealer_hand.append("".join(random.choices(deck)))
        player_hand.append("".join(random.choices(deck)))
    #Return str of player and dealer hand
    return "".join(player_hand), str(dealer_hand[0]) + "X"

#Ask the user whether they want to hit or stand
def act(action):
    while True:
        if re.search(r"^H(it)?$", action, re.IGNORECASE):
            player_hand.append("".join(random.choices(deck)))
            return "".join(player_hand)
        elif re.search(r"S(tand)?$", action, re.IGNORECASE):
            return "".join(player_hand)
        else:
            action = input("What do you want to do? (Hit or Stand) ")

#Keep a total of the hand inputted (testable). Return value of hand
def card_value(hand):
    value = 0
    ace_is_11 = False
    for card in hand:
        #If the ace being 11 causes value to go over 21, make its value 1
        if card == "A" and value < 11:
            value += 11
            ace_is_11 = True
        elif card == "A":
            value += 1
            ace_is_11 = False
        elif card in ["J", "K", "Q", "T"]:
            value += 10
        else:
            value += int(card)
        #This exists to make sure aces convert to one if it being 11 would cause a bust
        if value > 21 and ace_is_11:
            value-=10
            ace_is_11 = False
    return value

#Have dealer play out their hand by casino rules, return True (player win) or False (dealer win)
def end_game(dealer, player):
    #Check if the player busted
    if card_value(player) > 21:
        return False
    #Dealer must hit until hand is 17 or more
    update_screen("".join(player), "".join(dealer))
    while card_value(dealer) < 17:
        dealer.append("".join(random.choices(deck)))
        update_screen("".join(player), "".join(dealer))
    #Figure out who won
    if card_value(dealer) > 21:
        return True
    elif card_value(dealer) < card_value(player):
        return True
    elif card_value(dealer) > card_value(player):
        return False

if __name__ == "__main__":
    main()