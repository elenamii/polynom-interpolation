#this file contains the functions from code.py (coffee and pasta)

def poly_add(p,q):
	p=[int(element) for element in p]
	q=[int(element) for element in q]
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