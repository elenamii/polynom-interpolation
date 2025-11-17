#import numpy as np #Benötigt für numerische Berechnungen
# import matplotlib.pyplot as plt #Benötigt für Plotten von Graphen aber glaube das brauchen wir nicht

#plt.style.use('seaborn-poster')

# KLASSE FÜR POLYNOM SCHREIBWEISE (notation)

class Polynom:
    def __init__(self, *coeffcients):
        """input: Koeffizienten in der Form a_n, ..., a_0"""
        self.coeffiecients = list(coeffcients)

    def __repr__(self):
        return "Polynom" + str(tuple(self.coeffiecients))

    def __str__(self):
        """Gibt das Polynom als formatierten String zurück, z.B. -2x^2 + x + 3"""
        coeffs = self.coeffiecients
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

# test Klasse Polynom
polys = [Polynom(1, 0, -4, 3, 0),
         Polynom(2, 0),
         Polynom(4, 1, -1), 
         Polynom(3, 0, -5, 2, 7),
         Polynom(-42)]

for count, poly in enumerate(polys):
    print(f"$p_{count} = {str(poly)}$")

#ausgabe polyschreibweise
print(f"in polynomschreibweise: {Polynom}")

#stützstellen und -werte werden abgefragt und gespeichert 
anzahl = int(input("Gewünschte ANZAHL Stützstellen eingeben: ")) 
x_wert = []
y_wert = []

print("Bitte geben Sie ihre gewünschten Stützstellen mit ihren Stützwerten an.")

for i in range(anzahl):
    x= float(input(f"x({i}): ")) 
    y= float(input(f"y({i}): "))
    x_wert.append(x)
    y_wert.append(y)


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

#test poly_add mit bsp-polynomen 
p = [1,2,3]
q = [5,6]	
print(poly_add(p,q)) #expect: [6, 8, 3]

#polynom multiplication
def poly_mult(p,q):
	result_length = len(p) + len(q) -1
	result =[0] * result_length 

	for i in range (len(p)):
		for j in range (len(q)):
			p_koeff = p[i]
			q_koeff = q[j]

			product = p_koeff * q_koeff #12

			position = i+j # 2

			result[position] = result[position] + product
			#[0,0,12,0]

	return result

# test poly_mult mit bsp-polynomen 
print(poly_mult(p,q)) # expect [5, 16, 27, 18]


# funktion zum multiplizieren von polynom mit zahl DOKU FEHLT 
def poly_number_mult(p,number):
	result = []
	for coeff in p:
		result.append(coeff * number) #jeden koeff multiplizieren
	return result 

# test poly_number_mult 
number = 2
p = [2,4,6]
print(f"das ergebnis ist: {poly_number_mult(p,number)}") #expect [2,8,12]

#funktion zum dividieren von polynom und zahl DOKU FEHLT
def poly_number_div(p, number):
	result= []

	for coeff in p:
		print(f"coeff: {coeff}, number: {number}, type of number: {type(number)}")
		if number != 0:
			result.append(coeff / number)
	return result 

#test poly_number_div
print(f"das ergebnis von der div ist: {poly_number_div(p,number)}") #expect [1,2,3] --> tatsächlich [1.0,2.0.3.0] evtl change??

#poly_to_str funktion muss noch geschrieben werden -> polynom als string ausgeben (schön)

# lagrange 
def lagrange (x_wert,y_wert):
	
	P = [0] # endpolynom zum auffüllen

	for i in range (anzahl): #anzahl wird am anfang abgefragt 

		L = [1] # konstantes Lagrange polynom 

		for j in range (anzahl):
			if j != i:
				factor = [- x_wert[j], 1] 
				L = poly_mult(L, factor)
				print(f"x_wert: {x_wert}, y_wert: {y_wert}")
				denominator = x_wert[i] - (x_wert[j])
				print(f"L: {L}, denominator: {denominator}, type of denominator: {type(denominator)}")

				L = poly_number_div (L, denominator)
	
		L = poly_number_mult (L, y_wert[i])
		print(f"das ergebnis ist L(x) = {L}")

		P = poly_add(L, P)

	print(f"das Lagrange Polynom lautet: P(x)={P}")
	return P


lagrange(x_wert,y_wert)













#Beide Polynombasenbitte in ausmultiplizierter Form (Normalform des Polynoms…)

#Das Programm soll in der Lage sein die Lagrange-Polynome (-Basis) auszugeben.




#Des Weiteren soll die Newton-Basis ausgegeben werden.
def newton(x,y):
	n = len(y)
#plt.show() zeigt Plots an falls wir die Polynome auslesen wollen / visualisieren wollen

