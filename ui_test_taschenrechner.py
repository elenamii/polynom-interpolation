import os
clear = lambda: os.system('cls')
clear()

import tkinter as ui
import re

def validate(new_value):
    # Nur Ziffern, + - * / und Klammern erlauben
    if new_value == "":
        return True
    return bool(re.fullmatch(r"[0-9+\-*/() ]*", new_value))

def calculate():
    expr = entry.get()
    try:
        result = str(eval(expr))
        entry.delete(0, ui.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, ui.END)
        entry.insert(0, "Fehler")

window = ui.Tk()
window.title("Taschenrechner")
window.geometry("600x250")

# Validierung aktivieren
vcmd = (window.register(validate), "%P")

entry = ui.Entry(window, validate="key", validatecommand=vcmd, font=("Arial", 24))
entry.place(x=10, y=10, width=400, height=75)

btn = ui.Button(window, text="Berechnen", command=calculate)
btn.place(x=10, y=100, width=400, height=50)

window.mainloop()

#ChatGPT danke dir fÜr deine hilfe

