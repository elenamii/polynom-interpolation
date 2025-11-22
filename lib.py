#polynom addition
def poly_add(p,q):
	result=[]
	max_length= max(len(p), len(q))
	for i in range(max_length):
		try:
			a = p[i]
		except IndexError:
			a = 0
		try: 
			b= q[i]
		except IndexError:
			b = 0
			
		result.append(a+b)
			
	return result

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