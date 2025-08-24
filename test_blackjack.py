from blackjack import card_value, end_game, start_game

def test_card_value():
    assert card_value(["2", "A", "J"]) == 13
    assert card_value(["J", "J", "A"]) == 21
    assert card_value(["A", "A", "A"]) == 13
    assert card_value(["K", "4", "A", "K"]) == 25
    assert card_value(["9", "8", "A", "9"]) == 27

def test_end_game():
    #testing outcomes where the dealer never hits to ensure the test is not random
    assert end_game(["T", "7"], ["A", "J"]) == True
    assert end_game(["T", "7"], ["T", "6"]) == False
    assert end_game(["T", "7"], ["T", "K", "Q"]) == False

def test_start_game():
    #Ensure that whatever the rng generates, the function returns a str
    #From here: https://stackoverflow.com/questions/38573862/how-to-assert-that-a-type-equals-a-given-value
    player, dealer = start_game()
    assert type(player) == str
    assert type(dealer) == str