# import modules and define variables

import random

suits = ('Hearts','Diamonds', 'Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8 ,'Nine': 9, 'Ten':10,'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

current_playing = True

# define classes

class Card: # create cards

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:  # create deck of cards

    def __init__(self):
        self.deck = [] # haven't made a deck yet
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_combo = ''
        for card in self.deck:
            deck_combo += '\n ' + card.__str__()
            return 'The deck has: ' + deck_combo

    def shuffle(self): # shuffle the cards in the deck
        random.shuffle(self.deck)

    def deal(self): # pick a card from the deck
        one_card = self.deck.pop()
        return one_card

class Hand: # show all cards that dealer and player have
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0 # keep track of the aces

    def add_cards_deck(self, card): # add cards to player or dealer hand
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_ace (self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips: # tracking numb of chips

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_the_bet(self):
        self.total += self.bet

    def lose_the_bet(self):
        self.total -= self.bet

