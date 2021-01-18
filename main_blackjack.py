# import modules and define variables

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

current_playing = True


# define classes

class Card:  # create cards

    def initial (self, suit, rank):
        self.suit = suit
        self.rank = rank

    def str_value(self):
        return self.rank + ' of ' + self.suit


class Deck:  # create deck of cards

    def initial(self):
        self.deck = []  # haven't made a deck yet
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def str_value(self):
        deck_combo = ''
        for card in self.deck:
            deck_combo += '\n ' + card.str_value()
            return 'The deck has: ' + deck_combo

    def shuffle(self):  # shuffle the cards in the deck
        random.shuffle(self.deck)

    def deal(self):  # pick a card from the deck
        one_card = self.deck.pop()
        return one_card


class Hand:  # show all cards that dealer and player have
    def initial (self):
        self.cards = []
        self.value = 0
        self.aces = 0  # keep track of the aces

    def add_cards_deck(self, card):  # add cards to player or dealer hand
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:  # tracking numb of chips

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_the_bet(self):
        self.total += self.bet

    def lose_the_bet(self):
        self.total -= self.bet


# Functions

def take_bet(chips):  # asking user's bet
    while True:
        try:
            chips.bet = int(input("How many chips do you want to bet? "))
        except ValueError:
            print("Sorry, that did not work! Please input a number: ")
        else:
            if chips.bet > chips.totl:
                print("Your bet cannot exceed 100.")
            else:
                break


def hit(deck, hand):
    hand.add_cards_deck(deck.deal())
    hand.adjust_ace()


def hit_or_stand(deck, player_hand):
    pass


def hit_stand(deck, hand):
    global current_playing
    while True:
        question = input("Hit or Stand? Enter 'hand' or 'stand': ")
        if question[0].lower() == 'hand':
            hit(deck, hand)
        elif question[0].lower() == 'stand':
            print("Player = stands, Dealer = playing.")
            current_playing = False;
        else:
            print("Try again!")
            continue
        break

    def show(player, dealer):
        print("\nDealer's Hand: ")
        print(" <card hideen>")
        print("", dealer.cards[1])
        print("\nDealer's Hand: ", *dealer.cards, sep='\n')

    def show_all_cards(player, dealer):
        print("\nDealer's Hand: ", *dealer.cards, sep='\n ')
        print("Dealer's Hand =", dealer.value)
        print("\nPlayer's Hand: ", *player.cards, sep='\n ')
        print("Player's Hand =", player.value)



     def player_done(player, dealer, chips):
         print("Player is done :/")
         chips.lose_the_bet()
     def player_won(player, dealer, chips):
         print("Player WINS!!")
         chips.win_the_bet()
    def dealer_done(player, dealer, chips):
        print("Dealer is done")
        chips.win_the_bet()
    def dealer_won(player, dealer, chips):
        print("Dealer WINS!!!")
        chips.lose_the_bet()
    def push_up(player, dealer):
        print("Push! Player & Dealer Tie.")


    #gameplay

    while True:
        print("Welcome to BlackJack!")

        #shuffle deck
        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        player_hand.add_cards_deck()
        player_hand.add_cards_deck()

        dealer_hand = Hand()
        dealer_hand.add_cards_deck(deck.deal())
        dealer_hand.add_cards_deck(deck.deal())

        #setUp
        player_chips = Chips()

        #ask player for bet
        take_bet(player_chips)

         #show some cards
        show(player_hand, dealer_hand)

        while playing:

            hit_or_stand(deck, player_hand)
            show(player_hand, dealer_hand)

            if player_hand.value > 21:
                player_done(player_hand, dealer_hand, player_chips)
                break

        if player_hand.value <= 21:

            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

            show_all_cards(player_hand, dealer_hand)

            if dealer_hand.value > 21:
                dealer_done(player_hand, dealer_hand, player_chips)

            elif dealer_hand.value > player_hand.value:
                dealer_won(player_hand, dealer_hand, player_chips)

            elif dealer_hand.value < player_hand.value:
                player_won(player_hand, dealer_hand, player_chips)

            elif dealer_hand.value < player_hand.value:
                dealer_won(player_hand, dealer_hand, player_chips)

            if player_hand.value > 21:
                player_done(player_hand, dealer_hand, player_chips)

        print("\nPlayer's winnings stand at", player_chips.total)

        new_game = input("\nWould you like to play again? yes or no?")
        if new_game[0].lower() == 'yes':
            playing = True
            continue
        else:
            print("\nThanks for playing!")
            break