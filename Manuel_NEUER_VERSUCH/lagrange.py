from polynom import Polynom

def lagrange_basis(x_wert, i):
    n = len(x_wert)
    L = Polynom([1])   # Start: konstantes Polynom 1

    for j in range(n):
        if j != i:
            # (x - x_j)
            faktor = Polynom([-x_wert[j], 1])

            # multipliziere Polynom
            L = L * faktor

            # dividiere durch (x_i - x_j)
            denom = x_wert[i] - x_wert[j]
            L = L.poly_number_div(denom)

    return L


def lagrange_interpolation(x_wert, y_wert):
    n = len(x_wert)
    P = Polynom([0])   # Startpolynom

    print("Berechnung der Lagrange-Basis-Polynome:")
    for i in range(n):
        Li = lagrange_basis(x_wert, i)
        print(f"L_{i}(x) = {Li}")

        # y_i * L_i(x)
        term = Li.poly_number_mult(y_wert[i])

        # Summation
        P = P + term

    print(f"\nInterpolationspolynom P(x) = {P}")
    return P


if __name__ == "__main__":
    x = [1, 2, 3]
    y = [2, 3, 5]
    lagrange_interpolation(x, y)
