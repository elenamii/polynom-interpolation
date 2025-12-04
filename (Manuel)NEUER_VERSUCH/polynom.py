# Polynomklasse + Operationen (add, mult, horner, pretty-print)

class Polynom:
    def __init__(self, coeffs: list[float]):
        self.coeffs = coeffs  # Koeffizientenliste

    def __add__(self, other):  # Polynom + Polynom
        result = []
        max_len = max(len(self.coeffs), len(other.coeffs))
        for i in range(max_len):
            a = self.coeffs[i] if i < len(self.coeffs) else 0
            b = other.coeffs[i] if i < len(other.coeffs) else 0
            result.append(a + b)
        return Polynom(result)

    def __mul__(self, other):  # Zahl oder Polynom
        result_len = len(self.coeffs) + len(other.coeffs) - 1
        result = [0] * result_len
        for i in range(len(self.coeffs)):
            for j in range(len(other.coeffs)):
                self_coeffs = self.coeffs[i]
                other_coeffs = other.coeffs[j]
                
                product = self_coeffs * other_coeffs
                
                position = i + j
                
                result[position] = result[position] + product
        return Polynom(result)
    
    def poly_number_mul(self, number: float) -> 'Polynom': #erwarteter Rückgabetyp ist Polynom
        result = []
        for coeff in self.coeffs:
            result.append(coeff * number)
        return Polynom(result)

    def horner(self, x: float) -> float:
        # Placeholder: implement Horner-Schema later
        pass

    def degree(self) -> int:
        # Placeholder: return the degree of the polynomial
        pass

    def __str__(self) -> str:
        # Placeholder: return polynomial as string
        pass





