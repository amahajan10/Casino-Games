import tkinter as tk
from PIL import Image, ImageTk
from design import *
from card import Card, get_cards
from dealgame import Dealgame
import subprocess
import sys 


class PageContainer(tk.Tk):
    #multipage tutorial link: https://medium.com/analytics-vidhya/gui-for-your-python-program-with-multiple-windows-options-78c2ea8d259d
    """"Handles page switching"""
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self, bg="#252424")
        tk.Tk.geometry(self, '1280x720')
        container.pack(side='top', fill='both', expand=True)
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        self.frame = {}

        for f in (HomePage,StartPage,BjGamePage,HorseRacePage):

            frame = f(container, self)

            self.frame[f] = frame

            frame.grid(row=0,column=0,sticky='nsew')
        
        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frame[cont]
        frame.tkraise()


class HomePage(tk.Frame):
    """The first page (Only shows on launch for now)"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, parent, bg = "#252424")
        game_title_label = tk.Label(self, text="Casino Games Collection", font=font_medium, bg="#252424", fg="white")
        #game_title_label.grid(row=0, column=3)
        game_title_label.pack(side=TOP)
        orgimage = Image.open("Assets/logo.png").resize((100, 100), Image.ANTIALIAS)
        myimage = ImageTk.PhotoImage(orgimage)
        image_tile = tk.Label(self, image=myimage)
        image_tile.image = myimage
        #image_tile.grid(row=3, column=3)
        image_tile.pack(side=TOP)
        # nametag = tk.Text(self, height=1, width=30, font=font_small) 
        # #nametag.grid(row=4, column=3)
        # nametag.pack(side=TOP)   
        play_button = tk.Button(self, text="Play", command=lambda: controller.show_frame(StartPage), font=font_small)
        #play_button.grid(row=5, column=3)
        play_button.pack(side=TOP, pady=20)

class StartPage(tk.Frame):
    """The Page with Game Options"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#252424")
        label = tk.Label(self, text="Games", font=font_small, bg="#252424", fg="white")
        label.pack(padx=10, pady=10)
        button1 = tk.Button(self, text = "BlackJack", command = lambda: controller.show_frame(BjGamePage), width = 20, height = 1, font=font_small)
        button1.pack(pady=20)  
        button2 = tk.Button(self, text = "Horse Racing", command = lambda: controller.show_frame(HorseRacePage), width = 20, height = 1, font=font_small)
        button2.pack()  

class HorseRacePage(tk.Frame):
    """Horse Racing Game"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#252424")
        button_back = tk.Button(self, text= "<-", command=lambda: controller.show_frame(StartPage))
        button_back.pack(side=tk.TOP, anchor=tk.NW)

        button_start = tk.Button(self, text= "Start", command=lambda: subprocess.Popen([sys.executable, "horserace.py"]))
        button_start.pack(side=tk.TOP)
        


class BjGamePage(tk.Frame):
    """BlackJack game page"""
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent, bg="#252424")
        button_back = tk.Button(self, text= "<-", command=lambda: controller.show_frame(StartPage))
        button_back.pack(side=tk.TOP, anchor=tk.NW)

        #UI

        #Player:
        player_frame = tk.Frame(self, bg = background_color, **hightlight_frame_with_white )
        player_frame.pack(side = tk.BOTTOM, fill = X)

        player_cards_frame = tk.Frame(player_frame, bg = background_color)
        player_cards_frame.pack(side = tk.RIGHT, fill = Y)

        player_options_frame = tk.Frame(player_frame,bg = background_color)
        player_options_frame.pack(**pack_left_and_fill_y)           

        #CPU 
        dealer_frame = tk.Frame(self, bg = background_color, **hightlight_frame_with_white)
        dealer_frame.pack(side = tk.TOP,fill = X)

        dealer_cards_frame = tk.Frame(dealer_frame, bg = background_color)
        dealer_cards_frame.pack(side = tk.TOP, fill = Y)
        
        
        #Score Board:
        scoreboard = tk.Frame(self, bg = background_color, **hightlight_frame_with_white)
        scoreboard.pack(side = LEFT, fill = Y)

        dealer_score = tk.Frame(scoreboard,bg = background_color)
        dealer_score.pack(side = TOP, fill = BOTH)

        player_score = tk.Frame(scoreboard,bg = background_color)
        player_score.pack(side = BOTTOM, fill = BOTH)
        
        player_score_label = tk.Label(player_score, bg = background_color, text = 'Player Score: ', **button_args)
        player_score_label.pack()

        dealer_score_label = tk.Label(dealer_score, bg = background_color, text = "CPU Score: ", **button_args)
        dealer_score_label.pack()

        # Player Actions
        deal = tk.Button(player_options_frame, text = 'DEAL', **button_args, bg = "#10DEB9")
        deal.pack(side= LEFT, fill= Y)
        
        player_game_options_frame = tk.Frame(player_options_frame, bg = background_color)
        player_game_options_frame.pack(**pack_left_and_fill_y)
    

        hit = tk.Button(player_options_frame, text = 'HIT', bg = '#FF3300', **button_args, state = tk.DISABLED, name = 'hit')
        stand = tk.Button(player_options_frame, text = 'STAND', bg = '#B5BD18', **button_args, state = tk.DISABLED, name = 'stand')

        hit.pack(side = TOP, fill = X)
        stand.pack(side = TOP, fill = X)

        #player card stuff

        #player
        player_card1_image = Card.hidden_card()
        player_card1_label = tk.Label(player_cards_frame, image = player_card1_image, name='dealcard1_player')
        player_card1_label.pack(side = 'right')

        player_card2_image = Card.hidden_card()
        player_card2_label = tk.Label(player_cards_frame, image = player_card2_image, name='dealcard2_player')
        player_card2_label.pack(side = 'right')

        #dealer
        dealer_card1_image = Card.hidden_card()
        dealer_card1_label = tk.Label(dealer_cards_frame, image=dealer_card1_image, name='dealcard1_dealer')
        dealer_card1_label.pack(side='right')

        dealer_card2_image = Card.hidden_card()
        dealer_card2_label = tk.Label(dealer_cards_frame, image=dealer_card2_image, name='dealcard2_dealer')
        dealer_card2_label.pack(side='right')

        #busted labels and results
        player_busted_notif = tk.Label(player_cards_frame, text="Busted", font=font_medium, bg = background_color)
        dealer_busted_notif = tk.Label(dealer_cards_frame, text="Busted", font=font_medium, bg = background_color)

        deal_result_frame = tk.Frame(self, bg = background_color)
        deal_result_frame.pack(fill='both', side='left')

        def deal_start():
            Dealgame.clean_table([player_cards_frame, dealer_cards_frame, deal_result_frame])

            cards_deck = []
            for card in get_cards():
                cards_deck.append(Card(name = card))
                print(f'{card} added to deck')



            game = Dealgame(
                deck = cards_deck,
                main_screen = self,
                player_cards_frame = player_cards_frame,
                player_options_frame = player_options_frame,
                player_card1_label = player_card1_label,
                player_card2_label = player_card2_label,
                dealer_cards1_label= dealer_card1_label,
                dealer_cards2_label= dealer_card2_label,
                player_score_label = player_score_label,
                dealer_score_label = dealer_score_label,
                dealer_cards_frame = dealer_cards_frame,
                deal_result_frame = deal_result_frame,
                player_busted_notif = player_busted_notif,
                dealer_busted_notif = dealer_busted_notif,

            )

            game.deal_player()
            
            dealer_1 = game.get_cards(dealer_card1_label, is_player = False)
            dealer_2 = game.get_cards(dealer_card2_label, is_player=False, display=False)

            game.set_scoreboard()

            hit.bind('<Button-1>', lambda event: game.hit(dealer_2))
            stand.bind('<Button-1>', lambda event: game.finish_player_turn(dealer_2))
       
        deal.bind('<Button-1>', lambda event: deal_start())
        

       
       
       
       
       
        
        
        
        






app = PageContainer()
app.mainloop()   