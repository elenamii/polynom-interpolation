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


import math

class MathWithPolynomials:
    """
    Stellt nützliche, generische Funktionen zur Manipulation und 
    formatierten Ausgabe von Polynomen bereit.
    Polynome werden als Liste von Koeffizienten dargestellt, 
    beginnend mit dem Grad 0.
    Beispiel: [1, 2, 3] entspricht P(x) = 1 + 2x + 3x^2
    """
    
    @staticmethod
    def superscript(n):
        """Konvertiert eine Zahl in hochgestellte Zeichen für Exponenten."""
        # Da wir nur bis Grad 3 gehen (für Hermite), sind dies die wichtigsten
        table = {
            "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴",
            "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹"
        }
        # Für den Grad 1 (x) oder Grad 0 (Konstante) wird kein Hochzeichen benötigt.
        if n <= 1:
            return "" 
            
        return "".join(table.get(d, '') for d in str(n))

    @staticmethod
    def poly_mul(p, q):
        """Multipliziert zwei Polynome p und q."""
        r = [0.0] * (len(p) + len(q) - 1)
        for i in range(len(p)):
            for j in range(len(q)):
                r[i+j] += p[i] * q[j]
        return r

    @staticmethod
    def poly_add(p, q):
        """Addiert zwei Polynome p und q."""
        n = max(len(p), len(q))
        r = [0.0]*n
        for i in range(n):
            if i < len(p): r[i] += p[i]
            if i < len(q): r[i] += q[i]
        return r
    
    @staticmethod
    def print_poly_schoen(coeffs, digits=6, zero_threshold=1e-10):
        """
        Gibt ein Polynom in mathematisch schöner, absteigender Schreibweise (x^n...x^0) aus.
        
        Args:
            coeffs (list): Liste der Koeffizienten [a0, a1, a2, ...]
            digits (int): Anzahl der Nachkommastellen für die Rundung.
            zero_threshold (float): Koeffizienten, die kleiner als dieser 
                                    Schwellenwert sind, werden ignoriert.
        
        Returns:
            str: Die formatierte Zeichenkette des Polynoms.
        """
        # Kopie der Liste
        current_coeffs = list(coeffs) 
        
        # 1(Bereinigung)
        while current_coeffs and abs(current_coeffs[-1]) < zero_threshold:
            current_coeffs.pop()
            
        if not current_coeffs:
            return "0"

        result_terms = []
        
        # Durchlaufe Koeffizienten vom höchsten Grad abwärts 
        for grad in range(len(current_coeffs) - 1, -1, -1):
            coeff = current_coeffs[grad]
            
            # Ignoriere Terme unter  Schwellenwert
            if abs(coeff) < zero_threshold:
                continue
                
            # Runden des Koeffizienten für Anzeige
            coeff_val = round(coeff, digits)

            # Wenn der Koeffizient nach dem Runden Null ist, überspringen
            if abs(coeff_val) < 1e-9:
                continue

            abs_coeff = abs(coeff_val)

            # 3. Formatierung der Zahl (Vermeidung von 'e' und unnötigen Nullen)
            if abs(abs_coeff - round(abs_coeff)) < 1e-9:
                # Fast ganzzahlig
                formatted_coeff = str(round(abs_coeff))
            else:
                # Float-Formatierung mit dynamischer Kürzung der Nullen am Ende
                formatted_coeff = f"{abs_coeff:.{digits}f}".rstrip('0').rstrip('.')
            
            # 4. Verknüpfung und Vorzeichen
            sign = ""
            if result_terms: 
                # Fügt '+ ' oder ' - ' hinzu, wenn es nicht der erste Term ist
                sign = " + " if coeff_val > 0 else " - "
            elif coeff_val < 0:
                # Fügt '-' am Anfang hinzu, wenn der erste Term negativ ist
                sign = "-"
                
            # 5. Term-Erstellung (Sonderbehandlung für Koeffizient 1)
            term = ""
            is_one = (formatted_coeff == "1")

            if grad == 0:
                # Term x^0 (Konstante)
                term = formatted_coeff
            elif grad == 1:
                # Term x^1
                term = "x" if is_one else f"{formatted_coeff}x"
            else:
                # Term x^n
                power = MathWithPolynomials.superscript(grad)
                term = f"x{power}" if is_one else f"{formatted_coeff}x{power}"
                    
            result_terms.append(sign + term)

        return "".join(result_terms)