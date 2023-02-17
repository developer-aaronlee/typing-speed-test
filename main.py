from tkinter import *
from PIL import Image
from tkinter import messagebox
from random_word import Wordnik
from datetime import datetime
from typing_test import TypingTest
from score_board import ScoreBoard

ws = Wordnik()
easy = ws.get_random_words(hasDictionaryDef="true", maxLength=5, limit=15)
medium = ws.get_random_words(hasDictionaryDef="true", maxLength=6, limit=30)
hard = ws.get_random_words(hasDictionaryDef="true", maxLength=7, limit=30)


def easy_mode():
    # if name_entry.get() == "":
    #     messagebox.showwarning("Warning", "Name cannot be blank.")
    # else:
        window.destroy()
        TypingTest(easy)


def medium_mode():
    if name_entry.get() == "":
        messagebox.showwarning("Warning", "Name cannot be blank.")
    else:
        window.destroy()
        TypingTest(medium)


def hard_mode():
    if name_entry.get() == "":
        messagebox.showwarning("Warning", "Name cannot be blank.")
    else:
        window.destroy()
        TypingTest(hard)


def score_board():
    pass


window = Tk()
window.title("Typing Speed Test")
window.geometry("900x700")
window.config(padx=50, pady=50, bg="pink")

original_image = Image.open("logo.png")
resized_image = original_image.resize((800, 400))
resized_image.save("logo.png")
logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=800, height=400, highlightbackground="pink")
canvas.create_image(403, 203, image=logo_img)
canvas.grid(column=0, row=0, columnspan=3)

name_label = Label(width=10, text="Name:", bg="pink", fg="black", highlightbackground="pink")
name_label.grid(column=0, row=1, padx=(10, 0), pady=(60, 20), sticky="e")

name_entry = Entry(width=20, bg="white", fg="black", highlightbackground="pink")
name_entry.grid(column=1, row=1, padx=(0, 10), pady=(60, 20), sticky="w")
name_entry.focus()

score_button = Button(width=10, text="Score Board", highlightbackground="pink", fg="purple", command=score_board)
score_button.grid(column=2, row=1, padx=(10, 10), pady=(60, 20))

easy_button = Button(width=10, text="Easy Mode", highlightbackground="pink", command=easy_mode)
easy_button.grid(column=0, row=2, padx=(10, 10), pady=(50, 50))

medium_button = Button(width=10, text="Medium Mode", highlightbackground="pink", command=medium_mode)
medium_button.grid(column=1, row=2, padx=(10, 10), pady=(50, 50))

hard_button = Button(width=10, text="Hard Mode", highlightbackground="pink", command=hard_mode)
hard_button.grid(column=2, row=2, padx=(10, 10), pady=(50, 50))







window.mainloop()




