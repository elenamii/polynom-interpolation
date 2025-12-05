# main.py
"""
Hauptprogramm für Polynom-Interpolation
- Menü für Lagrange, Newton, Hermite
- Einlesen von Stützstellen/Ableitungen über io_input.py
- Ausgabe der Basis-Polynome und Interpolationspolynome
- Auswertung des Polynoms an einer Stelle
"""

from io_input import einlesen_stuetzstellen
from lagrange import lagrange_interpolation, lagrange_basis
from newton import newton_interpolation, newton_basis
from hermite import hermite_interpolation
from polynom import Polynom, MathWithPolynomials

def menu():
    print("\n--- Polynom-Interpolation ---")
    print("1. Lagrange-Interpolation")
    print("2. Newton-Interpolation")
    print("3. Hermite-Interpolation")
    print("4. Beenden")
    return input("Bitte wählen Sie eine Option (1-4): ")


def format_poly(poly_object):
    """Gibt die Koeffizienten-Liste des Polynom-Objekts zur Formatierung weiter."""
    # HIER wird das Attribut .coeffs des Polynom-Objekts an die Druckfunktion übergeben!
    return MathWithPolynomials.print_poly_schoen(poly_object.coeffs)

def auswahl_lagrange(x_wert, y_wert):
    print("\n--- Lagrange-Basis-Polynome ---")
    basisfunktionen = []
    for i in range(len(x_wert)):
        L = lagrange_basis(x_wert, i)
        basisfunktionen.append(L)
        print(f"L_{i}(x) = {format_poly(L)}") 

    print("\n--- Lagrange-Interpolationspolynom ---")
    P = lagrange_interpolation(x_wert, [y[0] for y in y_wert])  # nur Funktionswerte
    print(f"P(x) = {format_poly(P)}")

    x_eval = float(input("\nPolynom an welcher Stelle auswerten? "))
    wert = P.horner(x_eval) 
    print(f"P({x_eval}) = {wert}")

    return basisfunktionen, P

def auswahl_newton(x_wert, y_wert):
    print("\n--- Newton-Basis-Polynome ---")
    basisfunktionen = []
    for i in range(len(x_wert)):
        Ni = newton_basis(x_wert, i)
        basisfunktionen.append(Ni)
        print(f"N_{i}(x) = {format_poly(Ni)}")

    print("\n--- Newton-Interpolationspolynom ---")
    P = newton_interpolation(x_wert, [y[0] for y in y_wert])
    print(f"P(x) = {format_poly(P)}")

    x_eval = float(input("\nPolynom an welcher Stelle auswerten? "))
    wert = P.horner(x_eval) 
    print(f"P({x_eval}) = {wert}")

    return basisfunktionen, P

def auswahl_hermite(x_wert, y_wert):
    print("\n--- Hermite-Interpolation ---")
    P = hermite_interpolation(x_wert, y_wert)
    print(f"H(x) = {format_poly(P)}")

    x_eval = float(input("\nPolynom an welcher Stelle auswerten? "))
    wert = P.horner(x_eval) 
    print(f"P({x_eval}) = {wert}")

    return P

def main():
    print("Willkommen zur Polynom-Interpolation!")
    while True:
        wahl = menu()

        if wahl == "4":
            print("Programm wird beendet.")
            break

        # Stützstellen einlesen
        x_wert, y_wert = einlesen_stuetzstellen()

        if wahl == "1":
            auswahl_lagrange(x_wert, y_wert)
        elif wahl == "2":
            auswahl_newton(x_wert, y_wert)
        elif wahl == "3":
            auswahl_hermite(x_wert, y_wert)
        else:
            print("Ungültige Auswahl. Bitte 1-4 eingeben.")

if __name__ == "__main__":
    main()
