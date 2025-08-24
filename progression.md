# Progression

This was the `README.md` submitted for evaluation. It contains details of the development of the project.

## **Summary:**

This project is a culmination of what I have learned during CS50P. I decided to implement a simplified version of the popular card game Blackjack. When the program is run, the art module is used to show randomly generated cards. The user can then decide to hit or stand based on what they believe is the best move. The dealer will then play out their hand according to standard casino rules. The winner of the game will be determined, and then the user will be prompted if they want to play again.

### **Why Blackjack?**

When deciding what to do for this project, I had multiple considerations before landing on blackjack. At first, I wanted to make a UI using tkinter to convert a YouTube video to mp3 with pytube. I had it all thought up ... except that tkinter doesn't work with the CS50 developing environment.

So, after taking a glance a [YouTube video about a Python project](https://www.youtube.com/watch?v=th4OBktqK1I&t=1217s), I gained inspiration to make a new project. I initially wanted to make a casino with both a slot machine and blackjack. This proved rather challenging, and I found the blackjack difficult enough to implement and test.

### **The Design**

The project is designed to meet the requirements set by CS50P. I tried my best to use functions that returned a value, which would make them testable. Various libraries are also used, most of them being built in. These are re, sys, os, and random. The only custom library used is art.

The game plays like typical blackjack, without the complexities of betting, splitting, or doubling down. I used the art library to print the cards to the terminal, which gives a visual twist to what otherwise would have been a rather boring user experience. Unlike blackjack at a casino, I believe it is impossible to use card counting to gain a competitive advantage in this implementation because of the nature of how I deal the cards out.

```python
deck = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
#Start gameplay loop, return str (testable)
def start_game():
    #Deal initial hand
    for _ in range(2):
        #Convert the random choice to a string before putting it in the list
        dealer_hand.append("".join(random.choices(deck)))
        player_hand.append("".join(random.choices(deck)))
    #Return str of player and dealer hand
    return "".join(player_hand), str(dealer_hand[0]) + "X"
```

The random module will pull a random card out of the deck.

You may be wondering why I am returning a string, so allow me to explain by talking about the various problems I ran into while designing this project.

### **The Problems**

One of the biggest problems I encountered during this project is figuring out how to use the art module with my deck of cards. The eventual solution to this problem went through many iterations before it became optimal.

At first, I realized that trying to print list indices with the .text2art from the art module will print the list item, with square brackets. This made me realize that whatever I pass into the .text2art function must be a string if I want it to print nicely. This means that I had to convert both the dealer and player's hand from a list to a string. Poking around on the internet, I settled on the method above, based on [freeCodeCamp's method of joining lists into strings.](https://www.freecodecamp.org/news/python-list-to-string-how-to-convert-lists-in-python/) There are no spaces to ensure the cards print correctly. Regarding the font, I started at the "block" font but changed it to the "card" font to make the cards fit better in the terminal.

Also, I use a "T" instead of a "10" because the .text2art function is unable to display a card with 2 characters on it. I could have tried to make my own cards, but I didn't believe this to be a worthwhile use of my time.

The other time consuming problem was keeping track of the value of the player and dealer's hands. The code started as shown below, and it seemed to work well.

``` python
#Keep a total of the hand inputted (testable). Return value of hand
def card_value(hand):
    value = 0
    for card in hand:
        #If the ace being 11 causes value to go over 21, make its value 1
        if card == "A" and value < 11:
            value += 11
        elif card == "A":
            value += 1
        elif card in ["J", "K", "Q", "T"]:
            value += 10
        else:
            value += int(card)
```

This seemed to work, but after running lots of games, I noticed I sometimes lost when I shouldn't have. Specifically, the program wrongfully did not change the value of the ace to 1 if it was causing me to bust. I didn't really know where to start in solving this, so I took to the internet once again. I found someone who made a project like this and posted it on [LinkedIn](https://www.linkedin.com/pulse/building-blackjack-game-python-can-arslan/), so I took a look at how they handled the value of the ace.

```python
def calculate_hand_value(hand):
    value = 0
    has_ace = False

    for card in hand:
        rank = card.split()[0]

        if rank.isdigit():
            value += int(rank)
        elif rank in ['Jack', 'Queen', 'King']:
            value += 10
        elif rank == 'Ace':
            has_ace = True
            value += 11

    if has_ace and value > 21:
        value -= 10

    return value
```

Code sampled from LinkedIn, found [here.](https://www.linkedin.com/pulse/building-blackjack-game-python-can-arslan/)

I took note of the boolean value they use, which appears to determine if the user has an ace in their hand. I really only took inspiration from the use of a boolean, since I quickly realised that I didn't need to use a boolean for what they did.

What is really interesting is that the author's solution didn't work, and it missed some edge cases where an ace is drawn late into a hand. After a lot of thinking, I used a boolean value to keep track of if the ace is 1 or 11. I use conditionals to determine if the value of the ace needs to change.

```python
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

```

With solving these major problems, and some minor touch-ups to how the cards are displayed, and I finished the project. Overall, it was quite fun to go through this course and implement this project as its apex.
