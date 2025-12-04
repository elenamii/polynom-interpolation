# Einlesen von Stützstellen & Ableitungen

# io.py
"""
Dieses Modul kümmert sich um:
- Einlesen von Stützstellen und Stützwerten/Ableitungen
- Vorbereiten der Daten für Lagrange-, Newton- und Hermite-Interpolation
- Hilfsfunktionen wie Horner-Schema und Multiplizieren von Linearfaktoren
"""

from lagrange import lagrange_interpolation, lagrange_basis
from newton import newton_interpolation, newton_basis  # falls vorhanden
from hermite import hermite_interpolation  # falls vorhanden
from polynom import __mul__, __add__, poly_number_mul, poly_number_div, horner, __str__ , __rmul__

def einlesen_stuetzstellen():
    """
    Liest beliebige Anzahl Stützstellen mit Funktionswerten und Ableitungen ein.
    - x-Werte: Liste der Stützstellen
    - y-Werte: Liste der Listen: [y, y', y'', ...] bei Hermite
    """
    n = int(input("Wie viele Stützstellen möchten Sie eingeben? "))
    x_wert = []
    y_wert = []

    print("Hinweis: Für Hermite-Interpolation geben Sie mehrere Werte durch Komma getrennt ein.")
    print("Beispiel: Funktionswert, 1. Ableitung, 2. Ableitung ...")

    for i in range(n):
        x = float(input(f"x_{i} = "))
        x_wert.append(x)

        y_eingabe = input(f"y_{i} oder y_{i}, y'_{i}, ... bei Ableitungen: ")
        y_liste = [float(val) for val in y_eingabe.split(",")]
        y_wert.append(y_liste)

    return x_wert, y_wert


def horner(poly, x):
    """
    Horner-Schema zur effizienten Auswertung eines Polynoms poly an der Stelle x.
    poly: Liste von Koeffizienten [a0, a1, ..., an]
    """
    result = poly[0]
    for coef in poly[1:]:
        result = result * x + coef
    return result


def ausmultiplizieren_linearfaktoren(faktoren):
    """
    Multipliziert eine Liste von Linearfaktoren (Polynomen) aus.
    faktoren: Liste von Polynomen, z.B. [[1, -x0], [1, -x1], ...]
    """
    P = [1]
    for f in faktoren:
        P = __mul__(P, f)
    return P


def main():
    """
    Testfunktion für io.py – zeigt die Lagrange-Basis, Lagrange-Polynom und Auswertung.
    """
    # Einlesen der Stützstellen
    x_wert, y_wert = einlesen_stuetzstellen()

    # ---------------- Lagrange-Interpolation ----------------
    print("\n--- Lagrange-Basis-Polynome ---")
    for i in range(len(x_wert)):
        L = lagrange_basis(x_wert, i)
        print(f"L_{i}(x) = {L}")

    print("\n--- Lagrange-Interpolationspolynom ---")
    P_lagrange = lagrange_interpolation(x_wert, [y[0] for y in y_wert])  # nur Funktionswerte für Standard-Lagrange

    # Horner-Auswertung
    x_eval = float(input("\nAn welcher Stelle möchten Sie das Polynom auswerten? "))
    wert = horner(P_lagrange, x_eval)
    print(f"P({x_eval}) = {wert}")

    # ---------------- Newton-Interpolation ----------------
    try:
        print("\n--- Newton-Basis und Interpolation ---")
        P_newton = newton_interpolation(x_wert, [y[0] for y in y_wert])
        print(f"Newton-Interpolationspolynom: {P_newton}")
    except Exception as e:
        print("Newton-Interpolation nicht verfügbar:", e)

    # ---------------- Hermite-Interpolation ----------------
    if any(len(y) > 1 for y in y_wert):
        try:
            print("\n--- Hermite-Interpolation ---")
            P_hermite = hermite_interpolation(x_wert, y_wert)
            print(f"Hermite-Interpolationspolynom: {P_hermite}")
        except Exception as e:
            print("Hermite-Interpolation nicht verfügbar:", e)


if __name__ == "__main__":
    main()

