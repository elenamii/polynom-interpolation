# lagrange.py

from polynom import poly_mult, poly_add, poly_number_mult, poly_number_div

def lagrange_basis(x_wert, i):
    """
    Berechnet das i-te Lagrange-Basis-Polynom L_i(x) in ausmultiplizierter Form.
    """
    anzahl = len(x_wert)
    L = [1]  # Startpolynom

    for j in range(anzahl):
        if j != i:
            factor = [-x_wert[j], 1]  # (x - x_j)
            L = poly_mult(L, factor)
            denominator = x_wert[i] - x_wert[j]
            L = poly_number_div(L, denominator)
    return L


def lagrange_interpolation(x_wert, y_wert):
    """
    Berechnet das Lagrange-Interpolationspolynom P(x) in ausmultiplizierter Form.
    """
    anzahl = len(x_wert)
    P = [0]  # Startpolynom

    print("Berechnung der Lagrange-Basis-Polynome:")
    for i in range(anzahl):
        L = lagrange_basis(x_wert, i)
        print(f"L_{i}(x) = {L}")  # Ausgabe des Basis-Polynoms

        L = poly_number_mult(L, y_wert[i])
        P = poly_add(P, L)

    print(f"\nInterpolationspolynom P(x) = {P}")
    return P


# Optional: Testaufruf, kann beim Import aus io.py weggelassen werden
if __name__ == "__main__":
    x_wert = [1, 2, 3]
    y_wert = [2, 3, 5]
    lagrange_interpolation(x_wert, y_wert)
