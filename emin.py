import os
clear = lambda: os.system('cls')
clear()

#Aufgabe: Eine Funktion die Ableitungen von Polynomen berechnet.

class MathWithPolynomials:

    def poly_dervitive(coeffs):

        grad = len(coeffs) #höhste potenz von polynom
        result_coeffs = [] #leeres arry für ergebnis

        for i in range(1, grad, +1): #für itteration aber dekrementierend
            result_coeffs.append(coeffs[i] * i)#den coeff mal den index [potenz] ergbit neuen coeff

        return result_coeffs

    #UNITTESTS :)
    def unit_tests(p, expected): 
        result = MathWithPolynomials.poly_dervitive(p)#GUYS WIESO IST HEIR DER KLASSENNAME NOCHMAL NÖTIG??? Python is fucked up
        if result == expected:#vergleich für console output
            print(f"Test Passed: {MathWithPolynomials.print_poly(result)} == {MathWithPolynomials.print_poly(expected)}")
        else:
            print(f"Test Failed: {MathWithPolynomials.print_poly(result)} != {MathWithPolynomials.print_poly(expected)}")

    #Mathematische Schriebeweise
    def print_poly(coeffs):
        if not coeffs:
            return "0"

        result = []

        for grad, coeff in enumerate(coeffs):
            if coeff != 0:
                if grad == 0:
                    term = f"{coeff}"
                else:
                    power = MathWithPolynomials.superscript(grad)
                    term = f"{coeff}x{power}"

                result.insert(0, term)

        return " + ".join(result)
    
    def superscript(n):
        table = {
            "0": "", "1": "", "2": "²", "3": "³", "4": "⁴",
            "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹"
        }
        return "".join(table[d] for d in str(n))


# print("UNITTESTS")

# # TEST 1 
# polynom = [1, 2, 3]  # 1 + 2x + 3x^2 => [1, 2, 3]
# expected = [2, 6]  # 2 + 6x => [2, 6]
# MathWithPolynomials.unit_tests(polynom, expected)

# # TEST 2
# polynom = [0, 0, 5, 0, 1] # 0 + 0x + 5x^2 + 0x^3 + 1x^4 => [0, 0, 5, 0, 1]
# expected = [0, 10, 0, 4] # 10x + 0x^2 + 4x^3 => [0, 10, 0, 4]
# MathWithPolynomials.unit_tests(polynom, expected)

# # TEST 3
# polynom = [7]  # 7 => [7]
# expected = []  # 0 => []
# MathWithPolynomials.unit_tests(polynom, expected)

# # TEST 4
# polynom = [3, -4, 0, 2]  # 3 - 4x + 0x^2 + 2x^3 => [3, -4, 0, 2]
# expected = [-4, 0, 6]  # -4 + 0x + 6x^2 => [-4, 0, 6]
# MathWithPolynomials.unit_tests(polynom, expected)

# # TEST 5
# polynom = [0.5, 1.5, -2.5]  # 0.5 + 1.5x - 2.5x^2 => [0.5, 1.5, -2.5]
# expected = [1.5, -5.0]  # 1.5 - 5.0x => [1.5, -5.0]
# MathWithPolynomials.unit_tests(polynom, expected)


# print("END UNITTESTS")
