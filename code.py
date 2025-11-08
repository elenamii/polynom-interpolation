

# anzahl = int(input("Gewünschte ANZAHL Stützstellen eingeben: ")) #0 handeling
# x_wert = []
# y_wert = []

# print("Bitte geben Sie ihre gewünschten Stützstellen mit ihren Stützwerten an.")

# for i in range(anzahl):
#     x= float(input("x[i]: ")) # andere schreibweise für index !!
#     y= float(input("y(i): "))
#     x_wert.append(x)
#     y_wert.append(y)

#polynom adition
#def polynom_add(p,q):
    #max_length= max(len(p),len(q))
    #result = [0] * max_length
    
    # for i in range(max_length):
        #if i < len(p):
            #result[i]+= p[i]
        #if i < len(q):
            #result[i] += q[i]
    #return result

        #a = p[i] if i < len(p) else 0
        #b = q[i] if i < len(q) else 0
        #result = a+b

p=[1,2,3]
q=[5,6]
def add(p,q):
	ergebnis=[]
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
			
		ergebnis.append(a+b)
			
	return ergebnis


	
print(add(p,q))







# p = [1,2,3]
# q = [5,6]

#print(polynom_add(p,q)) #expect: [6, 8, 3]




# p= [1,2,3,4] --> 1*x^0 + 2*x^1 + 3*x^2 + 4*x^3
# q = [0,9,8] --> 0*x^0 + 9x^1 + 8*x^2

# p(x) + q(x) = (1+0)*x^0 + (2+9)*x^1 + (3+8)*x^2 + (4+7)*x^3
#             = (1+0) + (2+9)x + (3+8)x^2 + (4+7)x^3
