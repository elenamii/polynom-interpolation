import os
clear = lambda: os.system('cls')
clear()

import emin
import ast

breite = 400

def click():
    poly = ast.literal_eval(entry.get())
    result_str = emin.MathWithPolynomials.print_poly(poly)
    ergebnis.config(text= result_str)

def click2():
    result_str = select.get()
    ergebnis.config(text= result_str)


import tkinter as ui
import re

window = ui.Tk()
window.title("Mathe-Programm")
window.geometry("420x500")

#1.
label1 = ui.Label(window, text="1. Wählen Sie eine Methode aus")
label1.place(x=10, y=10, width=breite, height=50)

select = ui.StringVar()
select.set("1")

radio1 = ui.Radiobutton(window, text="Methode 1", variable=select, value="1").place(x=10, y=60, width=breite, height=40)
radio2 = ui.Radiobutton(window, text="Methode 2", variable=select, value="2").place(x=10, y=100, width=breite, height=40)
radio3 = ui.Radiobutton(window, text="Methode 3", variable=select, value="3").place(x=10, y=140, width=breite, height=40)

#2.
label2 = ui.Label(window, text="2. Geben Sie ihr Polynom ein")
label2.place(x=10, y=180, width=breite, height=50)

entry = ui.Entry(window, font=("Arial", 16))
entry.place(x=10, y=230, width=breite, height=50)

btn = ui.Button(window, text="Berechnen", command=click)
btn.place(x=10, y=290, width=breite, height=50)

#3.
label3 = ui.Label(window, text="3. Ergebnis")
label3.place(x=10, y=340, width=breite, height=50)

ergebnis = ui.Label(window)
ergebnis.place(x=10, y=390, width=breite, height=50)



window.mainloop()