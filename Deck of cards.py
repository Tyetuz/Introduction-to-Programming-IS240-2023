import random
import tkinter as tk

def main():
    c = Card()
    c.selectAtRandom()
    print(c)

class Card:
    def __init__(self, rank="", suit=""):
        self.rank = rank
        self.suit = suit

    def selectAtRandom(self):
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.rank = random.choice(ranks)
        self.suit = random.choice(["Clubs", "Diamonds", "Hearts", "Spades"])   

    def __str__(self):
        return self.rank + " of " + self.suit

def update_card_display():
    card.selectAtRandom()
    card_label.config(text=str(card))

# Create the main application window
root = tk.Tk()
root.title("Deck of Cards")

# Create a Card instance
card = Card()

# Create a frame to represent the card's border
card_frame = tk.Frame(root, bg="white", bd=2, relief="solid")
card_frame.pack(pady=20, padx=20)

# Create a label to display the card inside the frame
card_label = tk.Label(card_frame, text="", font=("Helvetica", 24), bg="white")
card_label.pack(padx=10, pady=10)

# Create a button to select a card at random
select_button = tk.Button(root, text="Select a Card", command=update_card_display)
select_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()
