from polynom import Polynom
from math import factorial

def hermite_interpolation(x_wert, y_wert):
    """
    Korrekte Hermite-Interpolation.
    x_wert: Liste der Stützstellen
    y_wert: Liste von Listen [[y0], [y1, y1', ...], ...]
    """
    z = []
    f = []

    # 1. z und f vorbereiten
    for xi, yi_list in zip(x_wert, y_wert):
        m = len(yi_list)
        for _ in range(m):
            z.append(xi)
            f.append(yi_list[0])

    n = len(z)
    Q = [[0.0]*n for _ in range(n)]
    for i in range(n):
        Q[i][0] = f[i]

    # 2. Dividierte Differenzen korrekt berechnen
    for j in range(1, n):
        for i in range(j, n):
            if z[i] == z[i-j]:
                # Wiederholung -> Ableitung nutzen
                # Bestimme, welche Ableitung
                total = 0
                for vals in y_wert:
                    m = len(vals)
                    if i < total + m:
                        deriv_index = i - total
                        Q[i][j] = vals[deriv_index] / factorial(j)
                        break
                    total += m
            else:
                Q[i][j] = (Q[i][j-1] - Q[i-1][j-1]) / (z[i] - z[i-j])

    # 3. Hermite-Polynom aufbauen
    H = Polynom([0])
    for i in range(n):
        term = Polynom([1])
        for j in range(i):
            term *= Polynom([-z[j], 1])
        term *= Q[i][i]
        H += term

    return H
