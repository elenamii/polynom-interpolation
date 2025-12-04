# newton.py
"""
Newton-Interpolation
- Berechnet das Newton-Polynom über Dividierte Differenzen
- Gibt die Newton-Basis-Polynome und das Interpolationspolynom in Normalform aus
- Nutzt polynom.py für Polynomoperationen
"""

from polynom import Polynom
from sympy import symbols, simplify, expand

def dividierte_differenzen(x_wert, y_wert):
    """
    Berechnet die Tabelle der div. Differenzen.
    x_wert: Liste der Stützstellen
    y_wert: Liste der Funktionswerte
    Rückgabe: Liste der Newton-Koeffizienten
    """
    n = len(x_wert)
    F = [yi for yi in y_wert]
    coeffs = [F[0]]

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            F[i] = (F[i] - F[i - 1]) / (x_wert[i] - x_wert[i - j])
        coeffs.append(F[j])

    return coeffs


def newton_basis(x_wert, i):
    """
    Berechnet das i-te Newton-Basis-Polynom in ausmultiplizierter Form.
    N_i(x) = ∏_{j=0..i-1} (x - x_j)
    """
    term = Polynom([1])   # Start: 1
    for j in range(i):
        term = poly_mult(term, [-x_wert[j], 1])   # multipliziere mit (x - x_j)
    return term


def newton_interpolation(x_wert, y_wert):
    """
    Berechnet das Newton-Interpolationspolynom vollständig ausmultipliziert.
    Gibt zusätzlich alle Newton-Basis-Polynome aus.
    """
    X = symbols('x')
    coeffs = dividierte_differenzen(x_wert, y_wert)
    P = Polynom([0])

    print("\n--- Newton-Basis-Polynome N_i(x) (ausmultipliziert) ---")
    basis_sympy = []

    for i in range(len(x_wert)):
        Ni = newton_basis(x_wert, i)
        print(f"N_{i}(x) = {Ni}")

        # Für die SymPy-Ausgabe (faktorisierte & ausmultiplizierte Darstellung)
        expr = 1
        for j in range(i):
            expr *= (X - x_wert[j])
        basis_sympy.append(expr)

        term = poly_number_mult(Ni, coeffs[i])
        P = poly_add(P, term)

    print("\n--- Newton-Basis-Polynome in SymPy (faktorisiert) ---")
    for i, bi in enumerate(basis_sympy):
        print(f"N_{i}(x) = {simplify(bi)}")

    print("\n--- Newton-Basis-Polynome in SymPy (ausmultipliziert) ---")
    for i, bi in enumerate(basis_sympy):
        print(f"N_{i}(x) = {expand(bi)}")

    print(f"\n--- Newton-Interpolationspolynom P(x) (ausmultipliziert) ---")
    print(P)

    return P


# ---------------------------
# Programmstart
# ---------------------------

if __name__ == "__main__":
    import sys

    print("Newton-Interpolation\n")

    n = int(input("Wie viele Punkte hast du? "))

    x = []
    y = []

    print("\nBitte die Punkte eingeben:")
    for i in range(n):
        xi = float(input(f"x{i}: "))
        yi = float(input(f"y{i}: "))
        x.append(xi)
        y.append(yi)

    newton_interpolation(x, y)
