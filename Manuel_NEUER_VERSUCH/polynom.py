class Polynom:
    def __init__(self, coeffs: list[float]):
        self.coeffs = coeffs[:]
        self.trim()

    def trim(self):
        while len(self.coeffs) > 1 and abs(self.coeffs[-1]) < 1e-12:
            self.coeffs.pop()

    def __add__(self, other):
        max_len = max(len(self.coeffs), len(other.coeffs))
        result = [0]*max_len
        for i in range(max_len):
            a = self.coeffs[i] if i < len(self.coeffs) else 0
            b = other.coeffs[i] if i < len(other.coeffs) else 0
            result[i] = a + b
        return Polynom(result)

    def __mul__(self, other):
        if isinstance(other, Polynom):
            r = [0]*(len(self.coeffs)+len(other.coeffs)-1)
            for i in range(len(self.coeffs)):
                for j in range(len(other.coeffs)):
                    r[i+j] += self.coeffs[i]*other.coeffs[j]
            return Polynom(r)
        else:
            return Polynom([c*other for c in self.coeffs])

    def __rmul__(self, number):
        return self*number

    def poly_number_div(self, number):
        if number == 0:
            raise ValueError("Division durch Null!")
        return Polynom([c/number for c in self.coeffs])

    def horner(self, x):
        result = 0
        for c in reversed(self.coeffs):
            result = result*x + c
        return result

    def degree(self):
        return len(self.coeffs)-1

    def __str__(self):
        if not self.coeffs:
            return "0"

        parts = []
        degree = len(self.coeffs) - 1
        for i, coeff in enumerate(self.coeffs):
            if abs(coeff) < 1e-12:
                continue

            deg = degree - i
            c = coeff
            # Ganze Zahl als int anzeigen
            c_str = str(int(c)) if c.is_integer() else f"{c:.4f}"

            if deg == 0:
                term = f"{c_str}"
            elif deg == 1:
                term = f"{'' if c==1 else '-' if c==-1 else c_str}x"
            else:
                term = f"{'' if c==1 else '-' if c==-1 else c_str}x^{deg}"

            parts.append(term)

        if not parts:
            return "0"

        s = parts[0]
        for t in parts[1:]:
            if t.startswith('-'):
                s += ' - ' + t[1:]
            else:
                s += ' + ' + t
        return s

