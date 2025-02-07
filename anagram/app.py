import tkinter as tk
from tkinter import ttk
from itertools import permutations


def find_anagrams():
    a = entry.get().strip().lower()

    if a:
        b = a.split()
        c = []
        for d in b:
            e = ["".join(f) for f in permutations(d)]
            c.extend(e)

        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, ", ".join(c))
        result_text.config(state=tk.DISABLED)
    else:
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Please enter a valid string.")
        result_text.config(state=tk.DISABLED)


# Main app window
app = tk.Tk()
app.title("Anagram Finder")
app.geometry("480x350")
app.configure(bg="#1e1e1e")

# Frame with padding
frame = tk.Frame(app, padx=20, pady=20, bg="#2c2c2c")
frame.pack(expand=True, fill="both")

# Header Label
label = tk.Label(frame, text="🔠 Enter a word:", fg="white", bg="#2c2c2c", font=("Helvetica", 14, "bold"))
label.grid(row=0, column=0, pady=10, sticky="w")

# Input field with rounded corners
entry = tk.Entry(frame, font=("Helvetica", 12), width=30, bg="#444", fg="white", insertbackground="white", bd=0, relief="flat")
entry.grid(row=0, column=1, padx=10, pady=10)

# Find Button with hover effect
def on_enter(e):
    find_button.config(bg="#555", fg="white")

def on_leave(e):
    find_button.config(bg="#444", fg="white")

find_button = tk.Button(frame, text="🔍 Find", font=("Helvetica", 12, "bold"), bg="#444", fg="white", bd=0, relief="flat",
                        command=find_anagrams, padx=15, pady=5, activebackground="#666", activeforeground="white")
find_button.grid(row=0, column=2, padx=10, pady=10)
find_button.bind("<Enter>", on_enter)
find_button.bind("<Leave>", on_leave)

# Textbox with results
result_text = tk.Text(frame, height=6, wrap="word", state=tk.DISABLED, font=("Helvetica", 11), bg="#333", fg="white", bd=0, relief="flat", padx=10, pady=10)
result_text.grid(row=1, column=0, columnspan=3, pady=15, sticky="ew")

# Run app
app.mainloop()
