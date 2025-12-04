from polynom import Polynom

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def hermite_interpolation(x_wert, y_wert):
    n = sum(len(y) for y in y_wert)
    z = []
    Q = []

    for xi, yi_list in zip(x_wert, y_wert):
        m = len(yi_list)
        for k in range(m):
            z.append(xi)
        for k in range(m):
            Q.append([yi_list[0]])

    for i in range(1, n):
        for j in range(i, n):
            if z[j] == z[j - i]:
                xi_index = 0
                count = 0
                total = 0
                for xi_vals in y_wert:
                    total += len(xi_vals)
                    if j < total:
                        xi_index = count
                        break
                    count += 1
                Q[j].append(y_wert[xi_index][i] / factorial(i))
            else:
                val = (Q[j][i - 1] - Q[j - 1][i - 1]) / (z[j] - z[j - i])
                Q[j].append(val)

    H = Polynom([0])
    basis_polynome = []

    for i in range(n):
        term = Polynom([1])
        for j in range(i):
            term = term * Polynom([-z[j], 1])
        term = term.poly_number_mult(Q[i][i])
        basis_polynome.append(term)
        H = H + term

    return basis_polynome, H, Q  # extra_info = Dividierte-Differenzen-Tabelle
