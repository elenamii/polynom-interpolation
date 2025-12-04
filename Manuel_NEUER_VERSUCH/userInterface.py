import tkinter as tk
from tkinter import messagebox
from polynom import Polynom
from lagrange import lagrange_interpolation, lagrange_basis
from newton import newton_interpolation, newton_basis
from hermite import hermite_interpolation
from io_input import horner

# --- Hilfsfunktionen für schöne Poly-Darstellung ---
class MathUtils:
    @staticmethod
    def superscript(n):
        table = {
            "0":"⁰","1":"¹","2":"²","3":"³","4":"⁴",
            "5":"⁵","6":"⁶","7":"⁷","8":"⁸","9":"⁹"
        }
        return "".join(table[d] for d in str(n))

    @staticmethod
    def print_poly(poly: Polynom, decimals=4):
        """
        Gibt ein Polynom in schöner Normalform zurück:
        - Höchste Potenz zuerst
        - Vorzeichen korrekt
        - 1/-1 wird sauber behandelt
        """
        coeffs = poly.coeffs
        if not coeffs:
            return "0"

        terms = []
        degree = len(coeffs) - 1

        for i in range(degree, -1, -1):  # höchste Potenz zuerst
            coeff = round(coeffs[i], decimals)
            if abs(coeff) < 1e-12:
                continue  # 0 überspringen

            # Vorzeichen
            sign = '+' if coeff > 0 else '-'
            a = abs(coeff)

            # Term bauen
            if i == 0:
                term = f"{a:g}"
            elif i == 1:
                term = "x" if a == 1 else f"{a:g}x"
            else:
                term = f"x{MathUtils.superscript(i)}" if a == 1 else f"{a:g}x{MathUtils.superscript(i)}"

            terms.append((sign, term))

        if not terms:
            return "0"

        # Erstes Vorzeichen entfernen, falls +
        first_sign, first_term = terms[0]
        s = first_term if first_sign == '+' else f"-{first_term}"

        for sign, term in terms[1:]:
            s += f" {sign} {term}"

        return s


# --- GUI ---
window = tk.Tk()
window.title("Polynom-Interpolation")
window.geometry("700x700")

method_var = tk.StringVar(value="1")
stuetz_entries_x = []
stuetz_entries_y = []

# --- Funktionen ---
def create_fields():
    global stuetz_entries_x, stuetz_entries_y
    try:
        n = int(anzStuetz.get())
        if n <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Fehler", "Bitte eine gültige positive Zahl eingeben!")
        return

    # Alte Felder entfernen
    for w in dynamic_frame.winfo_children():
        w.destroy()

    stuetz_entries_x = []
    stuetz_entries_y = []

    for i in range(n):
        tk.Label(dynamic_frame, text=f"x_{i} =").grid(row=i, column=0, padx=5, pady=5)
        entry_x = tk.Entry(dynamic_frame)
        entry_x.grid(row=i, column=1, padx=5, pady=5)

        tk.Label(dynamic_frame, text=f"y_{i} (Funktionswert, ggf. Ableitungen kommasepariert) =").grid(row=i, column=2, padx=5, pady=5)
        entry_y = tk.Entry(dynamic_frame)
        entry_y.grid(row=i, column=3, padx=5, pady=5)

        stuetz_entries_x.append(entry_x)
        stuetz_entries_y.append(entry_y)


def calculate():
    try:
        x_vals = [float(e.get()) for e in stuetz_entries_x]
        y_vals = []
        for e in stuetz_entries_y:
            val_str = e.get().replace(" ", "")
            y_list = [float(v) for v in val_str.split(",")]
            y_vals.append(y_list)
    except ValueError:
        messagebox.showerror("Fehler", "Bitte alle Eingaben korrekt ausfüllen!")
        return

    # Fehlende Ableitungen auffüllen (0)
    max_derivs = max(len(y) for y in y_vals)
    for i in range(len(y_vals)):
        while len(y_vals[i]) < max_derivs:
            y_vals[i].append(0.0)

    method = method_var.get()
    result_poly = None
    poly_name = "P(x)"

    try:
        if method == "1":  # Lagrange
            result_poly = lagrange_interpolation(x_vals, [y[0] for y in y_vals])
            poly_name = "L(x)"
        elif method == "2":  # Hermite
            result_poly = hermite_interpolation(x_vals, y_vals)
            poly_name = "H(x)"
        elif method == "3":  # Newton
            result_poly = newton_interpolation(x_vals, [y[0] for y in y_vals])
            poly_name = "N(x)"
    except Exception as e:
        messagebox.showerror("Interpolation fehlgeschlagen", f"{e}")
        return

    # Ergebnis schön anzeigen
    poly_str = MathUtils.print_poly(result_poly)
    ergebnis_label.config(text=f"{poly_name} = {poly_str}")


# --- GUI Aufbau ---
tk.Label(window, text="1. Methode wählen:").pack(pady=5)
tk.Radiobutton(window, text="Lagrange", variable=method_var, value="1").pack()
tk.Radiobutton(window, text="Hermite", variable=method_var, value="2").pack()
tk.Radiobutton(window, text="Newton", variable=method_var, value="3").pack()

tk.Label(window, text="2. Anzahl Stützstellen eingeben:").pack(pady=5)
anzStuetz = tk.Entry(window)
anzStuetz.pack(pady=5)

tk.Button(window, text="Formular erstellen", command=create_fields).pack(pady=5)

dynamic_frame = tk.Frame(window)
dynamic_frame.pack(pady=10)

tk.Button(window, text="Berechnen", command=calculate).pack(pady=10)

ergebnis_label = tk.Label(window, text="Ergebnis:", justify="left", font=("Arial", 12))
ergebnis_label.pack(pady=10)

window.mainloop()