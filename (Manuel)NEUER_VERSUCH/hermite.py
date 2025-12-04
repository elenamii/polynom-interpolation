# Hermite-DivDif + Hermite-Polynom

# hermite.py
"""
Hermite-Interpolation
- Unterstützt mehrere gleiche Stützstellen mit Funktionswerten und Ableitungen
- Berechnet das Hermite-Polynom in ausmultiplizierter Normalform
- Nutzt polynom.py für Polynom-Operationen
"""

from polynom import poly_mult, poly_add, poly_number_mult, poly_number_div, Polynom

def hermite_interpolation(x_wert, y_wert):
    """
    Berechnet das Hermite-Interpolationspolynom in Normalform.
    
    x_wert: Liste der Stützstellen [x0, x1, ...]
    y_wert: Liste von Listen [[y0], [y1, y1'], [y2, y2', y2''], ...]
            Jede innere Liste enthält den Funktionswert und Ableitungen (für Hermite)
    """
    # Anzahl der "einfachen Punkte" nach Aufteilung
    n = sum(len(y) for y in y_wert)  # Gesamtanzahl der Einträge inkl. Ableitungen

    # Vorbereitung: wiederholte Stützstellen für Hermite
    z = []  # erweiterte x-Werte
    Q = []  # Dividierte Differenzen-Tabelle

    for xi, yi_list in zip(x_wert, y_wert):
        m = len(yi_list)  # Anzahl der Ableitungen + Funktionswert
        for k in range(m):
            z.append(xi)
        # Dividierte Differenzen initial f[x_i] = y_i
        for k in range(m):
            Q.append([yi_list[0]])  # Startwerte (Funktionswerte, für höhere Ableitungen werden später korrigiert)

    # Aufbau der Hermite-DivDif-Tabelle
    for i in range(1, n):
        for j in range(i, n):
            if z[j] == z[j - i]:
                # Mehrfaches Auftreten => Ableitung verwenden
                xi_index = 0
                count = 0
                # Bestimme zu welchem ursprünglichen xi diese Wiederholung gehört
                total = 0
                for xi_vals in y_wert:
                    total += len(xi_vals)
                    if j < total:
                        xi_index = count
                        break
                    count += 1
                # Dividierte Differenzen = Ableitung / factorial
                Q[j].append(y_wert[xi_index][i] / factorial(i))
            else:
                val = (Q[j][i - 1] - Q[j - 1][i - 1]) / (z[j] - z[j - i])
                Q[j].append(val)

    # Konstruktion des Hermite-Polynoms
    H = Polynom([0])
    for i in range(n):
        term = Polynom([1])
        for j in range(i):
            term = poly_mult(term, [-z[j], 1])  # (x - z_j)
        term = poly_number_mult(term, Q[i][i])
        H = poly_add(H, term)

    print(f"Hermite-Interpolationspolynom H(x) = {H}")
    return H


def factorial(n):
    """Einfache Fakultätsfunktion"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# Optional: Testlauf
if __name__ == "__main__":
    x_wert = [1, 2]
    y_wert = [[2], [3, 1]]  # Beispiel: x1=1, y1=2; x2=2, y2=3, y2'=1
    hermite_interpolation(x_wert, y_wert)
