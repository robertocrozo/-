import tkinter as tk
import random


secret_number = random.randint(1, 50)
attempts = 5

def check_guess():
    global attempts
    guess = guess_entry.get()
    try:
        guess = int(guess)
        if attempts > 1:
            attempts -= 1
            if guess < secret_number:
                result_label.config(text="Too low. Attempts left: " + str(attempts))
            elif guess > secret_number:
                result_label.config(text="Too high. Attempts left: " + str(attempts))
            else:
                result_label.config(text="Bravo! You guessed it!")
                attempts = 0
        else:
            result_label.config(text="No more attempts! Please reset")
    except ValueError:
        result_label.config(text="Enter a valid number")

def reset_game():
    global secret_number, attempts
    secret_number = random.randint(1, 50)
    attempts = 5
    result_label.config(text="Game reset! Guess the new number.")
    guess_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x400")  
root.configure(bg='dim gray') 
root.resizable(False, False)


guess_entry = tk.Entry(root, width=30)
guess_entry.pack(pady=60)


button_frame = tk.Frame(root, bg="dim gray")
button_frame.pack(pady=20)


guess_button = tk.Button(button_frame, text="Guess", command=check_guess, bg="red")
guess_button.pack(side=tk.LEFT, padx=20)


reset_button = tk.Button(button_frame, text="Reset Game", command=reset_game, bg="red")
reset_button.pack(side=tk.LEFT, padx=20)


result_label = tk.Label(root, text="Guess a number between 1 and 50. You have 5 attempts.", bg='dim gray')
result_label.pack(pady=10)

root.mainloop()