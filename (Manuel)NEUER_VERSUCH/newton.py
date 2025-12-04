# Dividierte Differenzen + Newton-Basis + Interpolationspolynom

# newton.py
"""
Newton-Interpolation
- Berechnet das Newton-Polynom über Dividierte Differenzen
- Gibt die Newton-Basis-Polynome und das Interpolationspolynom in Normalform aus
- Nutzt polynom.py für Polynomoperationen
"""

from polynom import poly_mult, poly_add, poly_number_mult, Polynom

def dividierte_differenzen(x_wert, y_wert):
    """
    Berechnet die Tabelle der div. Differenzen.
    x_wert: Liste der Stützstellen
    y_wert: Liste der Funktionswerte
    Rückgabe: Liste der ersten Einträge jeder Spalte (Newton-Koeffizienten)
    """
    n = len(x_wert)
    # Tabelle initialisieren
    F = [y for y in y_wert]
    coeffs = [F[0]]  # erster Koeffizient

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            F[i] = (F[i] - F[i - 1]) / (x_wert[i] - x_wert[i - j])
        coeffs.append(F[j])

    return coeffs


def newton_basis(x_wert, i):
    """
    Berechnet das i-te Newton-Basis-Polynom in ausmultiplizierter Form
    """
    term = Polynom([1])
    for j in range(i):
        term = poly_mult(term, [-x_wert[j], 1])  # (x - x_j)
    return term


def newton_interpolation(x_wert, y_wert):
    """
    Berechnet das Newton-Interpolationspolynom in ausmultiplizierter Form
    """
    coeffs = dividierte_differenzen(x_wert, y_wert)
    P = Polynom([0])

    print("--- Newton-Basis-Polynome ---")
    for i in range(len(x_wert)):
        B = newton_basis(x_wert, i)
        print(f"N_{i}(x) = {B}")
        term = poly_number_mult(B, coeffs[i])
        P = poly_add(P, term)

    print(f"\nNewton-Interpolationspolynom P(x) = {P}")
    return P


# Optional: Testlauf
if __name__ == "__main__":
    x_wert = [1, 2, 3]
    y_wert = [2, 3, 5]
    newton_interpolation(x_wert, y_wert)
