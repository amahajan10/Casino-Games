from tkinter import *
from card import Card, get_cards
from design import *
from dealer import DealerAI

class Dealgame:
    def __init__(self, deck, main_screen,
                player_cards_frame, player_options_frame,
                player_card1_label, player_card2_label,
                dealer_cards_frame,
                dealer_cards1_label, dealer_cards2_label,
                player_score_label, dealer_score_label,
                player_busted_notif, dealer_busted_notif,
                deal_result_frame):

        self.deck = deck                                
        self.main_screen = main_screen
        self.player_cards_frame = player_cards_frame
        self.player_options_frame = player_options_frame
        self.player_card1_label = player_card1_label
        self.player_card2_label = player_card2_label
        self.dealer_cards_frame = dealer_cards_frame
        self.dealer_cards1_label = dealer_cards1_label
        self.dealer_cards2_label = dealer_cards2_label
        self.player_score_label = player_score_label
        self.dealer_score_label = dealer_score_label
        self.player_busted_notif = player_busted_notif
        self.dealer_busted_notif = dealer_busted_notif
        self.deal_result_frame = deal_result_frame

        self.player_cards = []
        self.dealer_cards = []
        self.enable_buttons(buttons = ['hit', 'stand'])

    
    def enable_buttons(self,buttons):
        for button in self.player_options_frame.winfo_children():
            if button.winfo_name() in buttons:
                button.configure(state = 'normal')

    def get_cards(self, card_label, display=True, is_player=True):
        card = Card.rand_card(self.deck)
        card_image = Card.get_card_image(card)

        if is_player:
            self.player_cards.append(card)
            self.handle_aces(card, self.player_cards, self.get_player_score())

        if not is_player:
            self.dealer_cards.append(card)
            self.handle_aces(card, self.dealer_cards, self.get_dealer_sccore())

        print(card.name + str(card.value))

        if display:
            self.display_card(card_label, card_image)
        else:
            card.displayed = False
            hidden_card = Card.hidden_card()
            card_label.configure(image = hidden_card)
            card_label.image = hidden_card

        self.deck.remove(card)
        return card

    def display_card(self,card_label, card_image):
        card_label.configure(image = card_image)
        card_label.image = card_image

    def deal_player(self):
        card1 = self.get_cards(self.player_card1_label)
        card2 = self.get_cards(self.player_card2_label)

    def hit(self, dealer_card_2 = None, is_player = True):
        hidden_card = Card.hidden_card()

        if is_player:
            new_card = Label(self.player_cards_frame, image = hidden_card)
            new_card.pack(side = 'right')

            card = self.get_cards(new_card)
            self.update_player_score_after_hit()

            if self.player_is_busted():
                self.player_busted_notif.pack(side = 'top', anchor = 'nw')
                self.finish_player_turn(dealer_card_2)

            return card
        else:
            new_card = Label(self.dealer_cards_frame, image = hidden_card)
            new_card.pack(side = 'right')

            card = self.get_cards(new_card, is_player=False)
            self.update_dealer_score_after_hit()

            return card

    
    def get_player_score(self):
        value = 0
        for card in self.player_cards:
            value = value + card.value
        return str(value)

    def get_dealer_sccore(self):
        value = 0
        for card in self.dealer_cards:
            value = value + card.value
        return str(value)

    
    def set_scoreboard(self):
        self.player_score_label.configure(text=f'Player Score: {self.get_player_score()}')
        self.dealer_score_label.configure(text = f'Dealer Score: {self.get_dealer_sccore()}')

    def update_player_score_after_hit(self):
        self.player_score_label.configure(text=f'Player Score: {self.get_player_score()}')
    
    def update_dealer_score_after_hit(self):
        self.dealer_score_label.configure(text=f'Dealer Score: {self.get_dealer_sccore()}')

    @staticmethod
    def clean_table(frames):
        for frame in frames:
            delete = frame.winfo_children()

            for widget in delete:
                if not str(widget.winfo_name()).startswith('dealcard'):
                    widget.forget()

    def player_is_busted(self):
        if int(self.get_player_score()) > 21:
            return True
        else:
            return False
    
    def dealer_is_busted(self):
        if int(self.get_dealer_score()) > 21:
            return True
        else:
            return False

    def stand_or_bust(self, dealer_card_2):
        card_image = Card.get_card_image(dealer_card_2)
        self.display_card(card_label=self.dealer_cards2_label, card_image=card_image)
        dealer_card_2.displayed = True
        self.update_dealer_score_after_hit()

    def finish_player_turn(self,dealer_card_2):
        for button in self.player_options_frame.winfo_children():
            # button['state'] = 'disabled'
            button.unbind('<Button-1>')

        self.stand_or_bust(dealer_card_2)


        dealer = DealerAI(dealer_score=self.get_dealer_sccore())
        while dealer.do_hit():
            self.hit(is_player=False)
            dealer.dealer_score = self.get_dealer_sccore()
            if self.dealer_is_busted():
                self.dealer_busted_notif.pack(side='left')

        self.choose_winner()


    def choose_winner(self):
        player_score = int(self.get_player_score())
        dealer_score = int(self.get_dealer_sccore())

        result = Label(self.deal_result_frame, text='', font=font_large, bg=background_color)
        result.pack(side='top', fill='both')


        if self.player_is_busted() and self.dealer_is_busted():
            result.configure(text='Both Busted!')
        
        if self.player_is_busted() and not self.dealer_is_busted():
            result.configure(text='Dealer Wins!')
        
        if not self.player_is_busted() and self.dealer_is_busted():
            result.configure(text='You Win!')
        
        if not self.player_is_busted() and not self.dealer_is_busted():
            if player_score > dealer_score:
                result.configure(text='You Win!')
            elif player_score < dealer_score:
                result.configure(text='Dealer Wins!')
            else:
                result.configure(text='You Tied')


    def count_aces(self, cards):
        counter = 0
        for card in cards:
            if str(card.name)[0] == 'a':
                counter = counter + 1

        return counter

    def aces(self, cards):
        aces = []
        for card in cards:
            if str(card.name)[0] == 'a':
                aces.append(card)
        return aces

    def not_aces(self, cards):
        not_aces = 0
        for card in cards:
            if str(card.name)[0] != 'a':
                not_aces += card.value
        return not_aces


    def handle_aces(self, curr, cards, cards_score):
        if self.count_aces(cards) == 1 and int(cards_score) > 21:
            for card in cards:
                if str(card.name)[0] == 'a':
                    card.value = 1 

        if self.count_aces(cards) > 1:
            if str(curr.name)[0] == 'a':
                curr.value = 1

            elif self.not_aces(cards) >= 12 - self.count_aces(cards):
                for card in self.aces(cards):
                    card.value = 1 
