import tkinter as tk
import random
import winsound

emoji_symbols = {
    "rock": "✊",
    "paper": "✋",
    "scissors": "✌️"
}

user_wins = 0
computer_wins = 0
ties = 0
rounds_played = 0
game_ongoing = True

def play(user_choice):
    global user_wins, computer_wins, ties, game_ongoing, rounds_played
    if not game_ongoing:
        return

    computer_choice = random.choice(list(emoji_symbols.keys()))
    user_label.config(text=emoji_symbols[user_choice])
    computer_label.config(text=emoji_symbols[computer_choice])

    if user_choice == computer_choice:
        result_label.config(text="It's a tie!", fg="orange")
        ties += 1
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result_label.config(text="You win!", fg="green")
        user_wins += 1
        winsound.Beep(600, 200)
    else:
        result_label.config(text="Computer wins!", fg="red")
        computer_wins += 1
        winsound.Beep(400, 200)

    rounds_played += 1
    update_stats()
    game_ongoing = False
    play_again_button.config(state=tk.NORMAL)

def play_again():
    global game_ongoing
    user_label.config(text="")
    computer_label.config(text="")
    result_label.config(text="")
    update_stats()
    play_again_button.config(state=tk.DISABLED)
    game_ongoing = True

def update_stats():
    stats_label.config(text=f"User: {user_wins} | Computer: {computer_wins} | Ties: {ties} | Rounds Played: {rounds_played}")

def on_window_resize(event):
    window_width = root.winfo_width()

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x400")

root.option_add('*TButton*highlightThickness', 0)
root.option_add('*TButton*borderWidth', 0)
root.option_add('*TButton.padding', [0, 0])
root.option_add('*TButton*relief', 'flat')

user_label = tk.Label(root, text="", font=("Arial", 48))
computer_label = tk.Label(root, text="", font=("Arial", 48))
result_label = tk.Label(root, text="", font=("Arial", 24))
stats_label = tk.Label(root, text="", font=("Arial", 18))
update_stats()

button_frame = tk.Frame(root)
button_frame.grid(row=3, column=0, columnspan=3, pady=10)
rock_button = tk.Button(button_frame, text="Rock", command=lambda: play("rock"))
paper_button = tk.Button(button_frame, text="Paper", command=lambda: play("paper"))
scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: play("scissors"))
rock_button.grid(row=0, column=0, padx=10)
paper_button.grid(row=0, column=1, padx=10)
scissors_button.grid(row=0, column=2, padx=10)

play_again_button = tk.Button(root, text="Play Again", command=play_again, state=tk.DISABLED)
play_again_button.grid(row=4, column=0, columnspan=3, pady=10)

user_label.grid(row=0, column=0, padx=10)
computer_label.grid(row=0, column=1, padx=10)
result_label.grid(row=1, column=0, columnspan=2, pady=10)
stats_label.grid(row=2, column=0, columnspan=2, pady=10)

root.configure(bg="lightgray")
user_label.configure(bg="lightgray")
computer_label.configure(bg="lightgray")
result_label.configure(bg="lightgray")
stats_label.configure(bg="lightgray")
rock_button.configure(bg="red", fg="white")
paper_button.configure(bg="green", fg="white")
scissors_button.configure(bg="blue", fg="white")
play_again_button.configure(bg="lightgray")

game_ongoing = True
root.bind("<Configure>", on_window_resize)
root.mainloop()
