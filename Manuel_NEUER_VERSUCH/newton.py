from polynom import Polynom

def newton_basis(x_wert, i):
    term = Polynom([1])
    for j in range(i):
        term = term * Polynom([-x_wert[j], 1])
    return term

def dividierte_differenzen(x_wert, y_wert):
    n = len(x_wert)
    F = y_wert.copy()
    coeffs = [F[0]]
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            F[i] = (F[i] - F[i-1]) / (x_wert[i] - x_wert[i-j])
        coeffs.append(F[j])
    return coeffs

def newton_interpolation(x_wert, y_wert):
    coeffs = dividierte_differenzen(x_wert, y_wert)
    P = Polynom([0])
    for i in range(len(x_wert)):
        Ni = newton_basis(x_wert, i)
        term = Ni * coeffs[i]
        P = P + term
    return P  # nur das Polynom zurückgeben
