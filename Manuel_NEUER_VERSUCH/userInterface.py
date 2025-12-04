from polynom import Polynom
from math import factorial

def hermite_interpolation(x_wert, y_wert):
    """
    Hermite-Interpolation mit mehrfachen Stützstellen und Ableitungen.
    y_wert[i] = [f(x_i), f'(x_i), f''(x_i), ...] 
    """

    # 1. Wiederholte Stützstellen auflisten
    z = []
    f = []
    for xi, yi_list in zip(x_wert, y_wert):
        m = len(yi_list)
        for _ in range(m):
            z.append(xi)
            f.append(yi_list[0])  # Funktionswert immer in f

    n = len(z)

    # 2. Divided Differences Matrix initialisieren
    Q = [[0.0]*n for _ in range(n)]
    for i in range(n):
        Q[i][0] = f[i]

    # 3. Divided Differences berechnen
    for j in range(1, n):
        for i in range(j, n):
            if z[i] == z[i-j]:
                # gleiche Stützstelle -> Ableitung verwenden
                # Finde den Index der Original-Stützstelle
                idx = 0
                total = len(y_wert[0])
                while i >= total:
                    idx += 1
                    total += len(y_wert[idx])
                Q[i][j] = y_wert[idx][j] / factorial(j)
            else:
                Q[i][j] = (Q[i][j-1] - Q[i-1][j-1]) / (z[i] - z[i-j])

    # 4. Hermite-Polynom aufbauen
    H = Polynom([0])
    for i in range(n):
        term = Polynom([1])
        for j in range(i):
            term *= Polynom([-z[j], 1])  # (x - z_j)
        term *= Q[i][i]
        H += term

    return H

# --- Test ---
if __name__ == "__main__":
    main()