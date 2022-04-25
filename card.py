from PIL import ImageTk, Image
import os
import random

card_location = './Assets/cards/'
hidden_card_location = './Assets/hidden.png'

def get_cards():
    cards = os.listdir(card_location)
    cards = [c.split('.')[0] for c in cards]
    return cards

class Card:
    def __init__(self, name, value=11, displayed=True):
        self.name = name
        self._value = value
        self._displayed = displayed

    @property
    def displayed(self):
        return self._displayed

    @displayed.setter
    def displayed(self, value):
        self._displayed = value

    @property
    def value(self):
        if str(self.name)[0] in ['j','q','k','1']:
            self._value = 10
        elif str(self.name)[0] in ['a']:
            pass #assigns value later since value can be changed 
        else:
            self._value = int(self.name.split('_')[0])
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


    def suit(self):
        return self.name.split('_')[1]

    @staticmethod
    def rand_card(i):
        cards = i
        random.shuffle(cards)
        dealt_card = cards[0]
        return dealt_card

    @staticmethod
    def get_card_image(card):
        try:
            card_f_location = f"{card_location}/{getattr(card,'name')}.png"
            card_image = Image.open(card_f_location)
            card_image_shape = card_image.resize((159,225), Image.ANTIALIAS)
            card_image = ImageTk.PhotoImage(card_image_shape)
            return card_image
        except:
            print("Could not find cards. Missing cards folder or card images")

    @staticmethod
    def hidden_card():
        try:
            card_image = Image.open(hidden_card_location)
            card_image_shaped = card_image.resize((159,225), Image.ANTIALIAS) 
            card_image = ImageTk.PhotoImage(card_image_shaped)

            return card_image
        except:
            print("Could not find cards. Missing cards folder or card images")


