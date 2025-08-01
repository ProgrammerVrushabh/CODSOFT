#task 4 ROCK , PAPER , SCISSOR

import tkinter as tk
from tkinter import messagebox
import random
uscore = 0
cscore = 0
def decide(ch):
    global uscore, cscore
    chs = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
    cchoice = random.randint(1, 3)
    utext = chs[ch]
    ctext = chs[cchoice]
    result_msg = f"You chose {utext}.\nComputer chose {ctext}.\n"
    if ch == cchoice:
        result_msg += "Ops! It's a Draw!"
        rlabel.config(fg="blue")
    elif (ch == 1 and cchoice == 3) or (ch == 2 and cchoice == 1) or (ch == 3 and cchoice == 2):
        uscore += 1
        result_msg += " Ahha! You Win this round!"
        rlabel.config(fg="green")
    else:
        cscore += 1
        result_msg += " Ohh! Computer Wins this round!"
        rlabel.config(fg="red")
    rlabel.config(text=result_msg)
    slabel.config(text=f" Your Score: {uscore} |  Computer Score: {cscore}")
def reset_game():
    global uscore, cscore
    uscore = 0
    cscore = 0
    rlabel.config(text="Choose Rock, Paper, or Scissors to start playing!", fg="#333")
    slabel.config(text=" Your Score: 0 |  Computer Score: 0")
def exit_game():
    if messagebox.askyesno("Exit", "Do you really want to quit?"):
        root.destroy()
root = tk.Tk()
root.title("Rock Paper Scissors Game ")
root.geometry("450x420")
root.config(bg="#e6f2ff")
tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold"), bg="#e6f2ff", fg="#333").pack(pady=10)
slabel = tk.Label(root, text="👤 Your Score: 0 |  Computer Score: 0", font=("Arial", 13), bg="#e6f2ff")
slabel.pack(pady=5)
rlabel = tk.Label(root, text="Choose Rock, Paper, or Scissors to start playing!",
                  font=("Arial", 12), wraplength=400, bg="#e6f2ff", justify="center", fg="#333")
rlabel.pack(pady=20)
bframe = tk.Frame(root, bg="#e6f2ff")
bframe.pack()
rbtn = tk.Button(bframe, text=" Rock", font=("Arial", 12), width=12, command=lambda: decide(1))
rbtn.grid(row=0, column=0, padx=10, pady=10)
pbtn = tk.Button(bframe, text=" Paper", font=("Arial", 12), width=12, command=lambda: decide(2))
pbtn.grid(row=0, column=1, padx=10, pady=10)
sbtn = tk.Button(bframe, text=" Scissors", font=("Arial", 12), width=12, command=lambda: decide(3))
sbtn.grid(row=0, column=2, padx=10, pady=10)
cframe = tk.Frame(root, bg="#e6f2ff")
cframe.pack(pady=10)
tk.Button(cframe, text=" Reset Game", font=("Arial", 12), command=reset_game).grid(row=0, column=0, padx=10)
tk.Button(cframe, text=" Exit", font=("Arial", 12), command=exit_game).grid(row=0, column=1, padx=10)
root.mainloop()

