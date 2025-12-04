# hermite.py
from polynom import Polynom

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def hermite_interpolation(x_wert, y_wert):
    """
    Berechnet das Hermite-Interpolationspolynom H(x) in ausmultiplizierter Form.
    
    x_wert: Liste der Stützstellen [x0, x1, ...]
    y_wert: Liste von Listen [[y0], [y1, y1'], [y2, y2', y2''], ...]
    """
    n = sum(len(y) for y in y_wert)
    z = []  # erweiterte Stützstellen
    Q = []  # Dividierte Differenzen

    # Wiederholte Stützstellen vorbereiten
    for xi, yi_list in zip(x_wert, y_wert):
        m = len(yi_list)
        for _ in range(m):
            z.append(xi)
        for _ in range(m):
            Q.append([yi_list[0]])

    # Hermite-Tabelle aufbauen
    for i in range(1, n):
        for j in range(i, n):
            if z[j] == z[j - i]:
                # Ableitung verwenden
                total = 0
                xi_index = 0
                for vals in y_wert:
                    total += len(vals)
                    if j < total:
                        xi_index = xi_index
                        break
                    xi_index += 1
                Q[j].append(y_wert[xi_index][i] / factorial(i))
            else:
                val = (Q[j][i-1] - Q[j-1][i-1]) / (z[j] - z[j-i])
                Q[j].append(val)

    # Hermite-Polynom konstruieren
    H = Polynom([0])
    for i in range(n):
        term = Polynom([1])
        for j in range(i):
            term = term * Polynom([-z[j], 1])
        term = term * Q[i][i]
        H = H + term

    return H  # **nur das fertige Polynom zurückgeben**
