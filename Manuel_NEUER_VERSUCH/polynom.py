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
        if isinstance(other, Polynom):
            result_len = len(self.coeffs) + len(other.coeffs) - 1
        result = [0] * result_len
        for i in range(len(self.coeffs)):
            for j in range(len(other.coeffs)):
                result[i + j] += self.coeffs[i] * other.coeffs[j]
                return Polynom(result)
            else: #Zahl
                return self.poly_number_mul(other)
            
    def __rmul__(self, number):  # Zahl * Polynom
        return self.poly_number_mul(number)
    
    def poly_number_mul(self, number: float) -> 'Polynom': #erwarteter Rückgabetyp ist Polynom
        result = []
        for coeff in self.coeffs:
            result.append(coeff * number)
        return Polynom(result)
    
    def poly_number_div(self, number: float) -> 'Polynom':
        if number == 0:
            raise ValueError("Division durch Null ist nicht erlaubt.")
        result = [c/number for c in self.coeffs]
        return Polynom(result)

    def horner(self, x: float) -> float:
        result = 0
        for coeff in reversed(self.coeffs):
            result = result * x + coeff
        return result

    def degree(self) -> int:
        """Gibt den Grad des Polynoms zurück."""
        return len(self.coeffs) - 1

    def __str__(self) -> str:
       """Gibt das Polynom als formatierten String zurück, z.B. -2x^2 + x + 3"""
       coeffs = self.coeffs
       if not coeffs:
            return "0"
       degree = len(coeffs) - 1
       parts = []
       for i, coeff in enumerate(coeffs):
            if coeff == 0:
                continue
            current_degree = degree - i
            sign = '+' if coeff > 0 else '-'
            a = abs(coeff)
            if current_degree == 0:
                term = f"{a:g}"
            elif current_degree == 1:
                term = "x" if a == 1 else f"{a:g}x"
            else:
                term = f"x^{current_degree}" if a == 1 else f"{a:g}x^{current_degree}"
            parts.append((sign, term))
            if not parts:
                return "0"
            first_sign, first_term = parts[0]
            s = ('' if first_sign == '+' else '-') + first_term
            for sign, term in parts[1:]:
                s += f" {sign} {term}"
                return s





