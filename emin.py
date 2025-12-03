import os
clear = lambda: os.system('cls')
clear()

import matplotlib
matplotlib.rcParams['toolbar'] = 'none'

import matplotlib.pyplot as plt # Fürs plotten
import numpy as np

import random

#Aufgabe: Eine Funktion die Ableitungen von Polynomen berechnet.

class MathWithPolynomials:

    def poly_dervitive(coeffs):

        grad = len(coeffs) #höhste potenz von polynom
        result_coeffs = [] #leeres arry für ergebnis

        for i in range(1, grad, +1): #für itteration aber dekrementierend
            result_coeffs.append(coeffs[i] * i)#den coeff mal den index [potenz] ergbit neuen coeff

        return result_coeffs

    #UNITTESTS :)
    def unit_tests(p, expected): 
        result = MathWithPolynomials.poly_dervitive(p)#GUYS WIESO IST HEIR DER KLASSENNAME NOCHMAL NÖTIG??? Python is fucked up
        if result == expected:#vergleich für console output
            print(f"Test Passed: {MathWithPolynomials.print_poly(result)} == {MathWithPolynomials.print_poly(expected)}")
        else:
            print(f"Test Failed: {MathWithPolynomials.print_poly(result)} != {MathWithPolynomials.print_poly(expected)}")

    #Mathematische Schriebeweise
    def print_poly(coeffs):
        if not coeffs:
            return "0"

        result = []

        for grad, coeff in enumerate(coeffs):
            if coeff != 0:
                if grad == 0:
                    term = f"{coeff}"
                else:
                    power = MathWithPolynomials.superscript(grad)
                    term = f"{coeff}x{power}"

                result.insert(0, term)

        return " + ".join(result)
    
    def superscript(n):
        table = {
            "0": "", "1": "", "2": "²", "3": "³", "4": "⁴",
            "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹"
        }
        return "".join(table[d] for d in str(n))

    def poly_mul(p, q):
        r = [0] * (len(p) + len(q) - 1)
        for i in range(len(p)):
            for j in range(len(q)):
                r[i+j] += p[i] * q[j]
        return r
    def poly_add(p, q):
        n = max(len(p), len(q))
        r = [0]*n
        for i in range(n):
            if i < len(p): r[i] += p[i]
            if i < len(q): r[i] += q[i]
        return r

class NewtonInterpolation: #Von ChatGPT verkürzt und optimiert

    @staticmethod
    def newton_interpolation_poly(x_stuetz, y_stuetz):
        coeffs = NewtonInterpolation.newton_coeffs(x_stuetz, y_stuetz)
        return NewtonInterpolation.newton_to_poly(x_stuetz, coeffs)

    @staticmethod
    def newton_coeffs(x_stuetz, y_stuetz):
        n = len(x_stuetz)
        copy = y_stuetz[:]  # kopiere
        coeffs = [copy[0]]  # erster Newton-Koeffizient

        for k in range(1, n):
            for i in range(n - 1, k - 1, -1):
                copy[i] = (copy[i] - copy[i - 1]) / (x_stuetz[i] - x_stuetz[i - k])
            coeffs.append(copy[k])

        return coeffs

    @staticmethod
    def newton_to_poly(x_stuetz, coeffs):
        poly = [0]
        for k in range(len(coeffs)):
            term = [1]
            for j in range(k):
                term = MathWithPolynomials.poly_mul(term, [-x_stuetz[j], 1])  # (x - xj)
            
            term = [coeffs[k] * c for c in term]
            poly = MathWithPolynomials.poly_add(poly, term)

        return poly

class PolynomialPlotter: #ChatGPT für uns damit wir mal was sehen



    @staticmethod
    def eval_poly(p, x):
        """Horner-Schema: Wert des Polynoms p an der Stelle x."""
        v = 0
        for c in reversed(p):
            v = v * x + c
        return v

    @staticmethod
    def plot_polynomial(poly, xs=None, ys=None, resolution=400):
        """
        Zeichnet das Polynom poly = [a0, a1, ..., an].
        Optional xs, ys für Stützstellen.
        """
        if xs is None:
            # Standardbereich
            Xmin, Xmax = -5, 5
        else:
            Xmin, Xmax = min(xs), max(xs)

        X = np.linspace(Xmin, Xmax, resolution)
        Y = [PolynomialPlotter.eval_poly(poly, x) for x in X]

        fig = plt.figure()
        fig.canvas.manager.set_window_title("Ergebnis als Graph")

        plt.plot(X, Y, label="Interpolationspolynom")
        
        if xs is not None and ys is not None:
            plt.scatter(xs, ys, color="red", label="Stützstellen")

        plt.grid(True, linestyle="--", linewidth=0.7)
        plt.legend()
        plt.title("Interpolationspolynom")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()

class HermiteInterpolation:
    @staticmethod
    def hermite_interpolation_poly(nodes):
        # 1. Erstelle erweiterte Knotenliste z und Anfangswerte y
        z = []
        y = []
        for x, vals in nodes:
            multiplicity = len(vals)
            for v in vals:
                z.append(x)
                y.append(v)

        # 2. Erzeuge dividierte Differenzen-Tabelle mit Hermite-Handling
        n = len(z)
        Q = [[0]*n for _ in range(n)]
        for i in range(n):
            Q[i][0] = y[i]

        # Hermite-Spezialfall: gleiche Knoten → Ableitungen
        for i in range(1, n):
            for j in range(1, i+1):
                if abs(z[i] - z[i-j]) < 1e-14:
                    # Wenn Ableitung vorhanden, Wert schon korrekt
                    if Q[i][j] == 0:
                        # Annahme: einfacher Fall 1. Ableitung
                        Q[i][j] = 0  # Standard: nur f'(x) sollte hier stehen, ggf. später anpassen
                else:
                    Q[i][j] = (Q[i][j-1] - Q[i-1][j-1]) / (z[i] - z[i-j])

        # 3. Newton-Koeffizienten
        coeffs_newton = [Q[i][i] for i in range(n)]

        # 4. Konvertiere Newton-Form in Normalform
        poly = [0]
        for k in range(n):
            term = [1]
            for j in range(k):
                term = MathWithPolynomials.poly_mul(term, [-z[j], 1])
            term = [coeffs_newton[k]*c for c in term]
            poly = MathWithPolynomials.poly_add(poly, term)

        return poly


def randomList():
    # n = random.randint(2, 10)
    n = 8
    array = []
    for i in range(n):
        array.append(random.randint(-10, 10))
    
    return array


print("START OF TEST/S")

xs = [0, 1, 2, 3, 4, 5]
ys = [1, 3, 4, 1, -2, -4]

poly = NewtonInterpolation.newton_interpolation_poly(xs, ys)

print(MathWithPolynomials.print_poly(poly))

PolynomialPlotter.plot_polynomial(poly, xs, ys)

nodes = [
    (0, [1]),  # f(0)=1, f'(0)=0
    (1, [3]),     # f(1)=3
    (2, [4]),
    (3, [1]),
    (4, [-2]),
    (5, [-4]),
]

poly_coeffs = HermiteInterpolation.hermite_interpolation_poly(nodes)
print(MathWithPolynomials.print_poly(poly_coeffs))

PolynomialPlotter.plot_polynomial(poly_coeffs, xs, ys)

print("END OF TEST/S")
