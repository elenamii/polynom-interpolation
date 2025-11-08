
#stützstellen und -werte werden abgefragt und gespeichert 
anzahl = int(input("Gewünschte ANZAHL Stützstellen eingeben: ")) #0 handeling fehlt
x_wert = []
y_wert = []

print("Bitte geben Sie ihre gewünschten Stützstellen mit ihren Stützwerten an.")

for i in range(anzahl):
    x= float(input("x[i]: ")) # andere schreibweise für index !!
    y= float(input("y(i): "))
    x_wert.append(x)
    y_wert.append(y)


#polynom adition
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

#test poy_add mit bsp-polynomen 
p = [1,2,3]
q = [5,6]	
print(poly_add(p,q)) #expect: [6, 8, 3]






