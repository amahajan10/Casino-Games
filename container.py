import tkinter as tk
from PIL import Image, ImageTk
import blackjack

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

        for f in (HomePage,StartPage, BjGamePage):# HorseRacePage):

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
        # change after this line
        game_title_label = tk.Label(self, text="Casino Games Collection", font=('Hoefler_Text',30))
        game_title_label.grid(row=0, column=3)
        orgimage = Image.open("Assets/logo.png").resize((100, 100), Image.ANTIALIAS)
        myimage = ImageTk.PhotoImage(orgimage)
        image_tile = tk.Label(self, image=myimage)
        image_tile.grid(row=3, column=3)
        nametag = tk.Text(self, height=1, width=30) 
        nametag.grid(row=4, column=3)   
        play_button = tk.Button(self, text="Play", command=lambda: controller.show_frame(StartPage))
        play_button.grid(row=5, column=3)

class StartPage(tk.Frame):
    """The Page with Game Options"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Games")
        label.pack(padx=10, pady=10)
        button1 = tk.Button(self, text = "BlackJack", command = lambda: controller.show_frame(BjGamePage), width = 20, height = 1)
        button1.pack()  

class BjGamePage(tk.Frame):
    """BlackJack page"""
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        button_back = tk.Button(self, text= "<-", command=lambda: controller.show_frame(StartPage))
        button_back.grid(row=0, column=0)





app = PageContainer()
app.mainloop()   