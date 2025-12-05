#auswertung horner schmea


class Polynom:
    def __init__(self, coeffs):
       
        self.coeffs = coeffs


def horner(poly, x):
    """
    Horner-Schema zur effizienten Auswertung eines Polynoms poly an der Stelle x
    """
    result = 0
    for coef in reversed(poly.coeffs):
        result = result * x + coef
    return result

#test

# Polynom p(x) = 1 + 2x + 3x²
p = Polynom([1, 2, 3])

# Wert an dem ausgewertet werden soll
x = 2



wert = horner(p, x)
print(f"p({x}) = {wert}")
