import tkinter as tk
from PIL import Image, ImageTk
from design import *
#import horserace as hr

class PageContainer(tk.Tk):
    #multipage tutorial link: https://medium.com/analytics-vidhya/gui-for-your-python-program-with-multiple-windows-options-78c2ea8d259d
    """"Handles page switching"""
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        #tk.Tk.iconbitmap(self,default="logo.png")

        container = tk.Frame(self)
        tk.Tk.geometry(self, '848x480')
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
        tk.Frame.__init__(self, parent, parent)
        game_title_label = tk.Label(self, text="Casino Games Collection", font=font_medium)
        #game_title_label.grid(row=0, column=3)
        game_title_label.pack(side=TOP)
        orgimage = Image.open("Assets/logo.png").resize((100, 100), Image.ANTIALIAS)
        myimage = ImageTk.PhotoImage(orgimage)
        image_tile = tk.Label(self, image=myimage)
        image_tile.image = myimage
        #image_tile.grid(row=3, column=3)
        image_tile.pack(side=TOP)
        nametag = tk.Text(self, height=1, width=30, font=font_small) 
        #nametag.grid(row=4, column=3)
        nametag.pack(side=TOP)   
        play_button = tk.Button(self, text="Play", command=lambda: controller.show_frame(StartPage), font=font_small)
        #play_button.grid(row=5, column=3)
        play_button.pack(side=TOP)

class StartPage(tk.Frame):
    """The Page with Game Options"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Games", font=font_small)
        label.pack(padx=10, pady=10)
        button1 = tk.Button(self, text = "BlackJack", command = lambda: controller.show_frame(BjGamePage), width = 20, height = 1, font=font_small)
        button1.pack()  
        button2 = tk.Button(self, text = "Horse Racing", command = lambda: controller.show_frame(HorseRacePage), width = 20, height = 1, font=font_small)
        button2.pack()  

class HorseRacePage(tk.Frame):
    """Horse Racing Game"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        button_back = tk.Button(self, text= "<-", command=lambda: controller.show_frame(StartPage))
        button_back.pack(side=tk.TOP, anchor=tk.NW)
        button_start = tk.Button(self, text= "Start", command=lambda: hr.runmain)
        button_start.pack(side=tk.TOP)


class BjGamePage(tk.Frame):
    """BlackJack game page"""
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
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
    

        hit = tk.Button(player_game_options_frame, text = 'HIT', bg = '#FF3300', **button_args, state = DISABLED, name = 'hit')
        stand = tk.Button(player_game_options_frame, text = 'STAND', bg = '#B5BD18', **button_args, state = DISABLED, name = 'stand')

        hit.pack(side = TOP, fill = X)
        stand.pack(side = TOP, fill = X)

       
       
       
       
       
       
       
       
        
        
        
        






app = PageContainer()
app.mainloop()   