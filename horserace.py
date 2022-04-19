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
def start_game():
    global Horse1x
    global Horse2x
    global Horse3x
    global Horse4x
    global winner 

    while winner == False:
        time.sleep(0.05)
        random_move_Horse1 = random.randint(0,20)
        random_move_Horse2 = random.randint(0,20)
        random_move_Horse3 = random.randint(0,20)
        random_move_Horse4 = random.randint(0,20)
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
        Label(main_screen, text=winner, font=('calibri', 20),fg = "green").place(x=200, y=450)
    else:
        show_winner()
        Label(main_screen, text=winner+ " Has Won", font=('calibri', 20),fg = "green").place(x=200, y=450)

def horses_move(Horse1_random_move, Horse2_random_move, Horse3_random_move, Horse4_random_move):
    canvas.move(Horse1, Horse1_random_move, 0)
    canvas.move(Horse2, Horse2_random_move, 0)
    canvas.move(Horse3, Horse3_random_move, 0)
    canvas.move(Horse4, Horse4_random_move, 0)

def show_winner():# display the winner

    winner = check_winner()
    test1.append(winner)
    if test1[0] == test1[1]:
        Label(main_screen, text="You win the bet", font=('calibri', 20),fg = "green").place(x=400, y=450)
    else:
        Label(main_screen, text="You lost the bet", font=('calibri', 20),fg = "green").place(x=400, y=450)
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

#Image Sizer
Horse1_jpg = Horse1_jpg.zoom(7)
Horse1_jpg = Horse1_jpg.subsample(90)
Horse2_jpg = Horse2_jpg.zoom(15)
Horse2_jpg = Horse2_jpg.subsample(90)
Horse3_jpg = Horse3_jpg.zoom(7)
Horse3_jpg = Horse3_jpg.subsample(90)
Horse4_jpg = Horse4_jpg.zoom(7)
Horse4_jpg = Horse4_jpg.subsample(90)

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

main_screen.mainloop()
