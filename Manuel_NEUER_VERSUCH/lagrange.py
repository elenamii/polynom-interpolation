from polynom import Polynom

def lagrange_basis(x_wert, i):
    """
    Berechnet das i-te Lagrange-Basis-Polynom L_i(x) als Polynom-Objekt.
    """
    anzahl = len(x_wert)
    L = Polynom([1])  # Startpolynom: 1
    denom = 1

    for j in range(anzahl):
        if j != i:
            L *= Polynom([-x_wert[j], 1])  # (x - x_j)
            denom *= (x_wert[i] - x_wert[j])

    L = L.poly_number_div(denom)
    return L



def lagrange_interpolation(x_wert, y_wert):
    if len(x_wert) != len(set(x_wert)):
        raise ValueError("Mehrere identische x-Werte ohne Ableitungen führen zu Fehlern. "
                         "Bitte Hermite-Interpolation verwenden.")
    P = Polynom([0])
    for i, yi in enumerate(y_wert):
        L = lagrange_basis(x_wert, i)
        P = P + yi*L
    return P
