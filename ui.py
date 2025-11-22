import os
clear = lambda: os.system('cls')
clear()

# Importe:
import tkinter as ui
import lib

#Variablen:
breite = 400

# Liste für dynamische Entry-Felder
stuetz_entries1 = []
stuetz_entries2 = []

# Funktionen:
def create_fields():
    global stuetz_entries1
    global stuetz_entries2
    
    # Eingabe auslesen
    try:
        n = int(anzStuetz.get())
    except ValueError:
        print("Ungültige Zahl.")
        return

    # Alte Felder entfernen
    for w in dynamic_frame.winfo_children():
        w.destroy()
    stuetz_entries1 = []   # alte Referenzen löschen
    stuetz_entries2 = []   # alte Referenzen löschen

    # Neue Felder erzeugen
    for i in range(n):
        lbl = ui.Label(dynamic_frame, text=f"Stützstelle x {i+1}:")
        lbl.grid(row=i, column=0, padx=5, pady=5)

        entry1 = ui.Entry(dynamic_frame)
        entry1.grid(row=i, column=1, padx=5, pady=5)
        
        lbl = ui.Label(dynamic_frame, text=f"Stützstelle y {i+1}:")
        lbl.grid(row=i, column=2, padx=5, pady=5)

        entry2 = ui.Entry(dynamic_frame)
        entry2.grid(row=i, column=3, padx=5, pady=5)

        stuetz_entries1.append(entry1)
        stuetz_entries2.append(entry2)
        
def read_fields():
    values1 = []
    for e in stuetz_entries1:
        values1.append(int(e.get()))
    
    values2 = []
    for e in stuetz_entries2:
        values2.append(int(e.get()))
    
    print("Stützstellen x:", values1)
    print("Stützstellen y:", values2)
    
    ergebnis.config(text=f"Ergebnis: {lib.MathWithPolynomials.print_poly(values1)} + {lib.MathWithPolynomials.print_poly(values2)} = {lib.MathWithPolynomials.print_poly(lib.poly_add(values1, values2))}")
    

# Hauptfenster:
window = ui.Tk()
window.title("Mathe-Programm")
window.geometry("500x600")

# 1.
label1 = ui.Label(window, text="1. Wählen Sie eine Methode aus")
label1.pack()

select = ui.StringVar()
select.set("1")

ui.Radiobutton(window, text="Lagrange", variable=select, value="1").pack()
ui.Radiobutton(window, text="Hermite", variable=select, value="2").pack()
ui.Radiobutton(window, text="Newton", variable=select, value="3").pack()

# 2.
label2 = ui.Label(window, text="2. Geben Sie die Stützstellen-Anzahl ein")
label2.pack()

anzStuetz = ui.Entry(window, font=("Arial", 16))
anzStuetz.pack()

btn = ui.Button(window, text="Formular erstellen", command=create_fields)
btn.pack()

# Container für dynamische Felder
dynamic_frame = ui.Frame(window)
dynamic_frame.pack()

# 3. 
ui.Button(window, text="Berechnen", command=read_fields).pack()

ergebnis = ui.Label(window, text="Ergebnis: ")
ergebnis.pack()

window.mainloop()
