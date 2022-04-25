
from tkinter import *
import random
import time


# Game defining Code
global test1
test1 = []
def selected_horse(color):
    bet = color
    #start_game()
    return bet

winner = False

global total_move_Horse1
global total_move_Horse2
global total_move_Horse3
global total_move_Horse4
global label_1
global label_2
global currency
global bet
global my_var


def reset():
    global Horse1x
    global Horse2x
    global Horse3x
    global Horse4x
    global winner
    global test1
    global total_move_Horse1
    global total_move_Horse2
    global total_move_Horse3
    global total_move_Horse4
    global label_1
    global label_2

    canvas.move(Horse1, -total_move_Horse1, 0)
    canvas.move(Horse2, -total_move_Horse2, 0)
    canvas.move(Horse3, -total_move_Horse3, 0)
    canvas.move(Horse4, -total_move_Horse4, 0)

    Horse1x = 0
    Horse2x = 0
    Horse3x = 0
    Horse4x = 0

    total_move_Horse1 = 0
    total_move_Horse2 = 0
    total_move_Horse3 = 0
    total_move_Horse4 = 0

    winner = False
    label_1.destroy()
    label_2.destroy()
    test1 = []
    main_screen.update()
        
def set_bet(num):
    global bet
    bet = num

    print(bet)



    

    





def start_game():
    global Horse1x
    global Horse2x
    global Horse3x
    global Horse4x
    global winner 
    global label_2

    global total_move_Horse1
    global total_move_Horse2
    global total_move_Horse3
    global total_move_Horse4

    total_move_Horse1 = 0
    total_move_Horse2 = 0
    total_move_Horse3 = 0
    total_move_Horse4 = 0    
    
    while winner == False:
        time.sleep(0.05)
        random_move_Horse1 = random.randint(0,20)
        random_move_Horse2 = random.randint(0,19)
        random_move_Horse3 = random.randint(0,19)
        random_move_Horse4 = random.randint(0,18)

        total_move_Horse1 += random_move_Horse1
        total_move_Horse2 += random_move_Horse2
        total_move_Horse3 += random_move_Horse3
        total_move_Horse4 += random_move_Horse4

        #Updates movements
        Horse1x += random_move_Horse1
        Horse2x += random_move_Horse2
        Horse3x += random_move_Horse3
        Horse4x += random_move_Horse4

        #Updates Screen for movements
        horses_move(random_move_Horse1, random_move_Horse2, random_move_Horse3, random_move_Horse4)
        main_screen.update()
        winner = check_winner()
        
    if winner == "Tie":
        show_winner()
        label_2 = Label(main_screen, text=winner, font=('calibri', 20),fg = "green")
    else:
        show_winner()
        label_2 = Label(main_screen, text=winner+ " Has Won", font=('calibri', 20),fg = "green")
    label_2.place(x=200, y=450)      
def horses_move(Horse1_random_move, Horse2_random_move, Horse3_random_move, Horse4_random_move):
    canvas.move(Horse1, Horse1_random_move, 0)
    canvas.move(Horse2, Horse2_random_move, 0)
    canvas.move(Horse3, Horse3_random_move, 0)
    canvas.move(Horse4, Horse4_random_move, 0)

def show_winner():# display the winner
    global label_1
    winner = check_winner()
    test1.append(winner)
    if test1[0] == test1[1]:
        label_1 = Label(main_screen, text="You win the bet", font=('calibri', 20),fg = "green")
        process_bet(True)
    else:
        label_1 = Label(main_screen, text="You lost the bet", font=('calibri', 20),fg = "green")
        process_bet(False)
    label_1.place(x=400, y=450)
def check_winner():
    if Horse1x >= 550:
        return "Blue"
    if Horse2x >= 550:
        return "Red"
    if Horse3x >= 550:
        return "Black"
    if Horse4x >= 550:
        return "Green"
    if Horse1x >= 550 and Horse2x >= 550:
        return "Tie"
    if Horse3x >= 550 and Horse4x >= 550:
        return "Tie"
    if Horse1x >= 550 and Horse4x >= 550:
        return "Tie"
    if Horse2x >= 550 and Horse4x >= 550:
        return "Tie"
    if Horse2x >= 550 and Horse3x >= 550:
        return "Tie"
    if Horse1x >= 550 and Horse3x >= 550:
        return "Tie"
    if Horse1x >= 550 and Horse2x >= 550 and Horse3x >= 550:
        return "Tie"
    if Horse1x >= 550 and Horse2x >= 550 and Horse4x >= 550:
        return "Tie"
    if Horse2x >= 550 and Horse3x >= 550 and Horse4x >= 550:
        return "Tie"
    if Horse1x >= 550 and Horse2x >= 550 and Horse3x >= 550 and Horse4x >= 550:
        return "Tie"
    return False

#Horse Positions
Horse1x = 0
Horse1 = 0

Horse2x = 0
Horse2 = 40

Horse3x = 0
Horse3 = 80

Horse4x = 0
Horse4 = 120

currency = 100
bet = 0

#Main Screen Code 
main_screen = Tk()
main_screen.title("Casino")
main_screen.geometry("600x500")
main_screen.config(background="white")
#Canvas
canvas = Canvas(main_screen, width=600, height=200, bg="white")
canvas.pack(pady=20)


#Image Importer
Horse1_jpg = PhotoImage(file="./images/blue-horse.png")
Horse2_jpg = PhotoImage(file="./images/red-horse.png")
Horse3_jpg = PhotoImage(file="./images/black-horse.png")
Horse4_jpg = PhotoImage(file="./images/green-horse.png")
Finishline_png = PhotoImage(file="./images/finishline.png")
#Image Sizer
Horse1_jpg = Horse1_jpg.zoom(7)
Horse1_jpg = Horse1_jpg.subsample(90)
Horse2_jpg = Horse2_jpg.zoom(15)
Horse2_jpg = Horse2_jpg.subsample(90)
Horse3_jpg = Horse3_jpg.zoom(7)
Horse3_jpg = Horse3_jpg.subsample(90)
Horse4_jpg = Horse4_jpg.zoom(7)
Horse4_jpg = Horse4_jpg.subsample(90)
Finishline_png = Finishline_png.zoom(40)
Finishline_png = Finishline_png.subsample(90)
Finishline = canvas.create_image(600, 100, image=Finishline_png)
Horse1 = canvas.create_image(Horse1x, Horse1, anchor = NW, image =Horse1_jpg)
Horse2 = canvas.create_image(Horse2x, Horse2, anchor = NW, image =Horse2_jpg)
Horse3 = canvas.create_image(Horse3x, Horse3, anchor = NW, image =Horse3_jpg)
Horse4 = canvas.create_image(Horse4x, Horse4, anchor = NW, image =Horse4_jpg)

#Labels main screen
label1 = Label(main_screen, text='Select Your Horse', font=('calibri', 20),bg ="white")
label1.place(x=200, y=280)
label2= Label(main_screen, text='Press Play', font=('calibri', 20),bg ="white")
label2.place(x=200, y=330)
label_win = Label(main_screen, text = "", font=('calibri', 20),bg ="white" )
label_win.place(x=200, y=450)
# label_money = Label(main_screen, text='$100', font=('calibri', 20),bg ="white")
# label_money.place(x=250, y=450)



Button1 = Button(main_screen, text='Play!', height=2, width=15, bg='white', command=start_game)
Button1.place(x=200, y=390)
Button2 = Button(main_screen, text='Blue Horse', height=2, width=15, bg='white', command=lambda: test1.append("Blue"))
Button2.place(x=0, y=460)
Button3 = Button(main_screen, text='Red Horse', height=2, width=15, bg='white', command=lambda: test1.append("Red"))
Button3.place(x=0, y=420)
Button4 = Button(main_screen, text='Black Horse', height=2, width=15, bg='white', command=lambda: test1.append("Black"))
Button4.place(x=0, y=380)
Button5 = Button(main_screen, text='Green Horse', height=2, width=15, bg='white', command=lambda: test1.append("Green"))
Button5.place(x=0, y=340)

Button6 = Button(main_screen, text='$10', height=2, width=15, bg='white', command=lambda: set_bet(10))
Button6.place(x=500, y=460)
Button7 = Button(main_screen, text='$20', height=2, width=15, bg='white', command=lambda: set_bet(20))
Button7.place(x=500, y=420)
Button8 = Button(main_screen, text='$30', height=2, width=15, bg='white', command=lambda: set_bet(30))
Button8.place(x=500, y=380)
Button9 = Button(main_screen, text='$50', height=2, width=15, bg='white', command=lambda: set_bet(50))
Button9.place(x=500, y=340)

ButtonReset = Button(main_screen, text = 'Reset', height = 2, width = 15, bg = 'white', command=reset)
ButtonReset.place(x=330, y=390)

str_currency = StringVar()
str_currency.set(currency)
label_currency = Label(main_screen,textvariable=str_currency,font=('calibri', 20),bg="white")
label_currency.place(x=20, y=300)
def process_bet(is_win):
    global currency
    global bet

    global str_currency
    

    if is_win:
        if test1[1] == "Blue": 
            currency += bet*1.25
            str_currency.set(currency)
        elif test1[1] == "Red": 
            currency += bet*1.5
            str_currency.set(currency)
        elif test1[1] == "Black": 
            currency += bet*1.75
            str_currency.set(currency)
        elif test1[1] == "Green": 
            currency += bet*1.75
            str_currency.set(currency)

    else: 
        currency -= bet
        str_currency.set(currency)

main_screen.mainloop()
