import tkinter as tk
import random

# Game Logic
def game(comp, mine):
    if comp == mine:
        return "It's a Draw!"
    elif (comp == 'snake' and mine == 'gun') or \
         (comp == 'water' and mine == 'snake') or \
         (comp == 'gun' and mine == 'water'):
        return "🎉 You Won!"
    else:
        return "😞 You Lost!"

# Function to handle user's choice
def play(choice):
    comp_choice = random.choice(["snake", "water", "gun"])
    result = game(comp_choice, choice)
    
    comp_label.config(text=f"Computer chose: {comp_choice}")
    result_label.config(text=result)

# GUI Setup
root = tk.Tk()
root.title("Snake Water Gun Game")
root.geometry("400x300")
root.config(bg="#1e1e1e")

# Labels
title_label = tk.Label(root, text="Snake Water Gun Game", font=("Arial", 16, "bold"), fg="white", bg="#1e1e1e")
title_label.pack(pady=10)

comp_label = tk.Label(root, text="Computer is waiting...", font=("Arial", 12), fg="white", bg="#1e1e1e")
comp_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="yellow", bg="#1e1e1e")
result_label.pack(pady=10)

# Buttons for Choices
button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(pady=10)

snake_button = tk.Button(button_frame, text="🐍 Snake", font=("Arial", 12), command=lambda: play("snake"), bg="#444", fg="white", padx=10, pady=5)
water_button = tk.Button(button_frame, text="💧 Water", font=("Arial", 12), command=lambda: play("water"), bg="#444", fg="white", padx=10, pady=5)
gun_button = tk.Button(button_frame, text="🔫 Gun", font=("Arial", 12), command=lambda: play("gun"), bg="#444", fg="white", padx=10, pady=5)

snake_button.grid(row=0, column=0, padx=5)
water_button.grid(row=0, column=1, padx=5)
gun_button.grid(row=0, column=2, padx=5)

# Run GUI
root.mainloop()
