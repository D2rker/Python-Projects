import tkinter as tk
from tkinter import messagebox
import random

def start_game():
    global random_number, attempts
    random_number = random.randint(1, 100)
    attempts = 0
    result_label.config(text="Game started! Guess a number between 1 and 100.", fg="blue")
    guess_entry.delete(0, tk.END)

def check_guess():
    global attempts
    try:
        guess = int(guess_entry.get())
        attempts += 1

        if guess < random_number:
            result_label.config(text="Too low! Try again.", fg="red")
        elif guess > random_number:
            result_label.config(text="Too high! Try again.", fg="red")
        else:
            messagebox.showinfo("Congratulations!", f"You guessed the number in {attempts} attempts!")
            start_game()
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid number.")

# Initialize main window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("500x400")
root.configure(bg="lightgray")

# Create widgets
title_label = tk.Label(root, text="Number Guessing Game", font=("Helvetica", 20, "bold"), bg="lightgray", fg="darkgreen")
title_label.pack(pady=20)

result_label = tk.Label(root, text="Click 'Start Game' to begin.", font=("Helvetica", 14), bg="lightgray", fg="black")
result_label.pack(pady=20)

guess_entry = tk.Entry(root, font=("Helvetica", 14), justify="center", bd=2, relief="solid")
guess_entry.pack(pady=10, ipadx=10, ipady=5)

check_button = tk.Button(root, text="Check Guess", font=("Helvetica", 14), bg="darkblue", fg="white", activebackground="blue", activeforeground="white", command=check_guess)
check_button.pack(pady=10, ipadx=10, ipady=5)

start_button = tk.Button(root, text="Start Game", font=("Helvetica", 14), bg="darkgreen", fg="white", activebackground="green", activeforeground="white", command=start_game)
start_button.pack(pady=10, ipadx=10, ipady=5)

# Start the game for the first time
start_game()

# Run the application
root.mainloop()
