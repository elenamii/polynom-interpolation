from polynom import Polynom

def lagrange_basis(x_wert, i):
    n = len(x_wert)
    L = Polynom([1])

    for j in range(n):
        if j != i:
            L = L * Polynom([-x_wert[j], 1])
            denom = x_wert[i] - x_wert[j]
            L = L.poly_number_div(denom)
    return L

def lagrange_interpolation(x_wert, y_wert):
    n = len(x_wert)
    P = Polynom([0])
    basis_polynome = []

    for i in range(n):
        Li = lagrange_basis(x_wert, i)
        basis_polynome.append(Li)
        term = Li.poly_number_mult(y_wert[i])
        P = P + term

    return basis_polynome, P, None  # kein extra_info nötig
