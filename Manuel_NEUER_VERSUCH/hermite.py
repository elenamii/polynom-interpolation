from polynom import Polynom
from math import factorial

def hermite_interpolation(x_wert, y_wert):
    """
    Hermite-Interpolation mit mehreren Ableitungen.
    y_wert[i] = [f(x_i), f'(x_i), f''(x_i), ...]
    Liefert ein Polynom-Objekt zurück.
    """

    # 1. Wiederholte Stützstellen erzeugen
    z = []
    f0 = []
    multiplicities = []
    for xi, yi_list in zip(x_wert, y_wert):
        m = len(yi_list)
        multiplicities.append(m)
        for _ in range(m):
            z.append(xi)
            f0.append(yi_list[0])

    n = len(z)
    Q = [[0.0]*n for _ in range(n)]

    # 2. Erste Spalte = f0
    for i in range(n):
        Q[i][0] = f0[i]

    # 3. Divided Differences berechnen
    for j in range(1, n):
        for i in range(j, n):
            if z[i] == z[i-j]:
                # gleiche Stützstelle -> j-te Ableitung
                idx = 0
                count = 0
                while count + multiplicities[idx] <= i:
                    count += multiplicities[idx]
                    idx += 1
                if j < len(y_wert[idx]):
                    Q[i][j] = y_wert[idx][j] / factorial(j)
                else:
                    Q[i][j] = 0.0
            else:
                Q[i][j] = (Q[i][j-1] - Q[i-1][j-1]) / (z[i] - z[i-j])

    # 4. Polynom aufbauen
    H = Polynom([0])
    for i in range(n):
        term = Polynom([1])
        for j in range(i):
            term *= Polynom([-z[j], 1])
        term *= Q[i][i]
        H += term

    return H
