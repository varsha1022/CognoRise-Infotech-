import random
import tkinter as tk

root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("500x600")
root.configure(bg="#1E90FF")

def game_function():
    try:
        user_input = int(UserEntry.get())  
    except ValueError:
        DisplayWinner.config(text="Invalid input! Please enter a number between 0-2", fg="red")
        return

    if user_input < 0 or user_input > 2:
        DisplayWinner.config(text="Error: Please enter a valid number (0-2)", fg="red")
        return
    
    items = ["Rock", "Paper", "Scissors"]
    computer_input = random.randint(0, 2)
    index = items[computer_input]
    ComputerEntry.config(text=f"Computer Input: {computer_input} [{index}]", fg="white")
    
    if user_input == computer_input:
        result = "It's a Tie!"
    elif (user_input == 0 and computer_input == 1) or (user_input == 1 and computer_input == 2) or (user_input == 2 and computer_input == 0):
        result = "Computer Wins!"
    else:
        result = "User Wins!"

    DisplayWinner.config(text=result, fg="yellow")  

def clear():
    UserEntry.delete(0, tk.END)
    DisplayWinner.config(text="")
    ComputerEntry.config(text="")

Title = tk.Label(root, text="Rock,Paper,Scissors Game", font=("Arial", 16, "bold"), fg="black",bg="#1E90FF")
Title.pack(padx=10, pady=20)

MainLabel = tk.Label(root, text="Enter 0 for Rock, 1 for Paper, 2 for Scissors:", font=("Arial", 14), bg="#1E90FF", fg="white")
MainLabel.pack(padx=10, pady=10)

UserEntry = tk.Entry(root, width=10, font=("Arial", 14))
UserEntry.pack(padx=10, pady=10)

ComputerEntry = tk.Label(root, text="", width=30, font=("Arial", 14), bg="#1E90FF", fg="yellow")
ComputerEntry.pack(padx=10, pady=10)

CheckWinnerBtn = tk.Button(root, text="Check Winner", width=15, font=("Arial", 14), command=game_function, bg="#09e018", fg="white",borderwidth=0)
CheckWinnerBtn.pack(padx=10, pady=20)

DisplayWinner = tk.Label(root, text="", font=("Arial", 18, "bold"), bg="#1E90FF", fg="yellow")
DisplayWinner.pack(padx=10, pady=20)

Cleargame = tk.Button(root, text="Play Again", width=15, font=("Arial", 14), command=clear, bg="#f03333", fg="white",borderwidth=0)
Cleargame.pack(padx=10, pady=20)

root.mainloop()
