from tkinter import *
from tkinter import messagebox
import random

entekhab = ["sang", "kaghaz", "ghaichi"]
cscore = 0
uscore = 0

def play_game():
    global cscore, uscore
    computer = random.choice(entekhab)
    user = user_choice.get()
    
    if user not in entekhab:
        messagebox.showinfo("Invalid Input", "Please select 'sang', 'kaghaz', or 'ghaichi'.")
    else:
        if user == computer:
            result = "Draw"
        elif user == "sang":
            if computer == "kaghaz":
                cscore += 1
                result = "Computer wins"
            else:
                uscore += 1
                result = "User wins"
        elif user == "kaghaz":
            if computer == "ghaichi":
                cscore += 1
                result = "Computer wins"
            else:
                uscore += 1
                result = "User wins"
        elif user == "ghaichi":
            if computer == "sang":
                cscore += 1
                result = "Computer wins"
            else:
                uscore += 1
                result = "User wins"
        
        messagebox.showinfo("Result", f"User: {user}\nComputer: {computer}\n{result}\n\nScores:\nUser: {uscore}\nComputer: {cscore}")

window = Tk()
window.title("Rock Paper Scissors")
window.geometry("500x500")
window.resizable(False, False)
window.config(bg="black")

fname = Label(window, text="Select 'sang', 'kaghaz', or 'ghaichi'", bg="gray", font=18)
fname.pack()

user_choice = StringVar()
user_choice.set("sang")

sang_radio = Radiobutton(window, text="Sang", variable=user_choice, value="sang",bg="gray")
sang_radio.pack()

kaghaz_radio = Radiobutton(window, text="Kaghaz", variable=user_choice, value="kaghaz", bg="gray")
kaghaz_radio.pack()

ghaichi_radio = Radiobutton(window, text="Ghaichi", variable=user_choice, value="ghaichi",bg="gray")
ghaichi_radio.pack()

play_button = Button(window, text="Play", command=play_game,bg="red")
play_button.pack()

window.mainloop()