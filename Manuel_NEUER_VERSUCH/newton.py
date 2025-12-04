from polynom import Polynom

def dividierte_differenzen(x_wert, y_wert):
    """
    Berechnet die Newton-Koeffizienten über dividierte Differenzen.
    """
    n = len(x_wert)
    F = y_wert.copy()
    coeffs = [F[0]]

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            F[i] = (F[i] - F[i - 1]) / (x_wert[i] - x_wert[i - j])
        coeffs.append(F[j])

    return coeffs


def newton_basis(x_wert, i):
    """
    Berechnet das i-te Newton-Basis-Polynom vollständig ausmultipliziert.
    """
    N = Polynom([1])
    for j in range(i):
        faktor = Polynom([-x_wert[j], 1])  # (x - x_j)
        N = N * faktor
    return N


def newton_interpolation(x_wert, y_wert):
    """
    Berechnet das Newton-Interpolationspolynom und die Basis-Polynome.
    """
    coeffs = dividierte_differenzen(x_wert, y_wert)

    basis_polynome = []
    P = Polynom([0])

    for i in range(len(x_wert)):
        Ni = newton_basis(x_wert, i)
        basis_polynome.append(Ni)

        term = Ni.poly_number_mult(coeffs[i])
        P = P + term

    return basis_polynome, P, coeffs