#W12A1034AW.py
#Bridge Hand
#Program to create a deck of cards, deal a hand of cards and randomly select thirteen cards from the deck

import random

class Card:
    def __init__(self, rank="", suit=""): #constructor
        self.rank = rank #instance of rank
        self.suit = suit #instance of suit

    def selectAtRandom(self): #randomly select a rank and suit
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"] #list of ranks
        self.rank = random.choice(ranks) #randomly select a rank

        self.suit = random.choice(["Clubs", "Diamonds", "Hearts", "Spades"]) #randomly select a suit  

    def __str__(self): #string representation of the card
        return self.rank + " of " + self.suit #Format the card as "rank of suit"

class Deck: #class for deck of cards
    def __init__(self): #create a deck of 52 cards
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits] #create a list of 52 cards

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self): #randomly draw a card from the deck
        return self.cards.pop() if self.cards else None #pop function removes the last element from the list

def main():
    # Create a deck of cards
    deck = Deck()
    # Shuffle the deck
    deck.shuffle()

    # Draw 13 cards from the deck
    hand = [deck.draw_card() for _ in range(13)]

    # Define the order of suits
    suit_order = {'Spades': 0, 'Hearts': 1, 'Diamonds': 2, 'Clubs': 3}
    # Define the order of ranks
    rank_order = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
    # Sort the hand by suit and then by rank
    hand.sort(key=lambda card: (suit_order[card.suit], rank_order[card.rank]))

    #Print the sorted hand
    for card in hand:
        print(card)
        
#Run the main function
main()