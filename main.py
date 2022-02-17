import sqlite3
import tkinter as tk
from PIL import Image, ImageTk

#database stuff

root = tk.Tk()
root.title("Casino Games Collection")
root.geometry("848x480") #16:9 aspect ratio 

def game_screen():
    pass
# main screen widgets
game_title_label = tk.Label(root, text="Casino Games Collection", font=('Hoefler_Text',30))
game_title_label.grid(row=0, column=3)

orgimage = Image.open("Assets/logo.png").resize((100, 100), Image.ANTIALIAS)
myimage = ImageTk.PhotoImage(orgimage)
image_tile = tk.Label(root, image=myimage)
image_tile.grid(row=3, column=3)

play_button = tk.Button(root, text="Play", command=game_screen)
play_button.grid(row=5, column=3)

tk.mainloop()
