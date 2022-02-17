from random import shuffle
# https://code.google.com/archive/p/vector-playing-cards/
# card images source link


class Cards:
    """makes cards"""
    def __init__(self, val, symbol):
        self.val = val
        self.symbol = symbol
    
    def __str__(self):
        if self.val == 1:
            val = "A"
        elif self.val == 11:
            val = "J"
        elif self.val == 12:
            val = "Q"
        elif self.val == 13:
            val = "K"
        else:
            val = self.val
        return f"{val}{self.symbol}"

class Deck:
    """makes Deck"""
    def __init__(self):
        self.cards = []
        self.generate_cards()

    def __len__(self):
        """Returns number of cards in the deck"""
        return len(self.cards)

    def show_cards(self):
        """Show all cards in the deck."""
        for card in self.cards:
            print(card)

    def __str__(self):
        """Alternate print method"""
        self.show_cards()

    def generate_cards(self):
        """Generate all cards in the deck."""
        self.cards = []
        for symbols in ['\u2660', '\u2665', '\u2663', '\u2666']:
            for val in range(1, 14):
                self.cards.append(Cards(val, symbols))

    def shuffle_deck(self):
        """Shuffle cards in the deck."""
        shuffle(self.cards)

    def deal_card(self):
        """Returns the top card from the deck"""
        return self.cards.pop()

class Player:
    """Creates a player"""
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def draw(self, deck, num=1):
        """Draw n cards from the deck"""
        # verifies that a card can be drawn from the deck
        if(len(deck) == 0):
            return "The deck is empty. Could not draw a card."

        for n in range(num):
            card = deck.deal_card()
            self.hand.append(card)

    def show_hand(self):
        """Show all cards in the hand in console."""
        clist = ""
        for card in self.hand:
            clist+=f" {card}"
        pval = f'{self.name}: {clist}'
        print(pval)
        return pval

    def get_hand(self):
        """return all cards in the player's hand (can be used for evaluating in GUI)."""
        return self.hand

    def get_total(self):
        """return total of player's hand"""
        sum = 0
        for i in self.hand:
            sum = sum + i.val
        return sum
        
    def __str__(self):
        self.show_hand()

    def __len__(self):
        "Return num of cards in the hand."
        return len(self.hand)

    def discard(self):
        """Remove cards from hand"""
        return self.hand.pop()