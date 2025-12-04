class Polynom:
    def __init__(self, coeffs: list[float]):
        self.coeffs = coeffs

    def __add__(self, other):
        result = []
        max_len = max(len(self.coeffs), len(other.coeffs))
        for i in range(max_len):
            a = self.coeffs[i] if i < len(self.coeffs) else 0
            b = other.coeffs[i] if i < len(other.coeffs) else 0
            result.append(a + b)
        return Polynom(result)

    def __mul__(self, other):
        if isinstance(other, Polynom):
            result_len = len(self.coeffs) + len(other.coeffs) - 1
            result = [0] * result_len
            for i in range(len(self.coeffs)):
                for j in range(len(other.coeffs)):
                    result[i + j] += self.coeffs[i] * other.coeffs[j]
            return Polynom(result)
        else:
            return self.poly_number_mult(other)

    def __rmul__(self, number):
        return self.poly_number_mult(number)

    def poly_number_mult(self, number: float):
        return Polynom([c * number for c in self.coeffs])

    def poly_number_div(self, number: float):
        if number == 0:
            raise ValueError("Division durch Null nicht erlaubt.")
        return Polynom([c / number for c in self.coeffs])

    def horner(self, x: float):
        result = 0
        for coeff in reversed(self.coeffs):
            result = result * x + coeff
        return result

    def degree(self):
        return len(self.coeffs) - 1

    def __str__(self):
        terms = []
        for i, c in enumerate(self.coeffs):
            if c == 0:
                continue
            if i == 0:
                terms.append(f"{c}")
            elif i == 1:
                terms.append(f"{c}x")
            else:
                terms.append(f"{c}x^{i}")

        return " + ".join(terms) if terms else "0"
