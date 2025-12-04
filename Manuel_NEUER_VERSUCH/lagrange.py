# lagrange.py
"""
Lagrange-Interpolation
- Berechnet das Lagrange-Polynom in ausmultiplizierter Form
- Nutzt polynom.py für Polynom-Operationen
"""

from polynom import Polynom

def lagrange_basis(x_wert, i):
    """
    Berechnet das i-te Lagrange-Basis-Polynom L_i(x) in ausmultiplizierter Form.
    """
    n = len(x_wert)
    L = Polynom([1])  # Startpolynom

    for j in range(n):
        if j != i:
            # (x - x_j) / (x_i - x_j)
            factor = Polynom([-x_wert[j], 1])
            L = L * factor
            L = L.poly_number_div(x_wert[i] - x_wert[j])
    return L

def lagrange_interpolation(x_wert, y_wert):
    """
    Berechnet das Lagrange-Interpolationspolynom P(x) in ausmultiplizierter Form.
    Gibt nur das Polynom zurück, keine Liste von Objekten.
    """
    P = Polynom([0])  # Startpolynom

    for i in range(len(x_wert)):
        L = lagrange_basis(x_wert, i)
        term = L * y_wert[i]  # multiplizieren mit Funktionswert
        P = P + term

    return P
