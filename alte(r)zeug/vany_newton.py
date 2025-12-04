# ich will das newton polynom machen
# ich hoffe der code funktioniert :D
#funktioniert nur wenn man erstmal sympy mit pip inytall sympy runterlädt
import sympy as sympy
from sympy import symbols, simplify

# wie viele punkte?
n = int(input("Wie viele Punkte hast du? "))

# listen für x und y
x = []
y = []

# punkte eingeben
print("Bitte die Punkte eingeben:")
for i in range(n):
    xi = float(input("x" + str(i) + ": "))
    yi = float(input("y" + str(i) + ": "))
    x.append(xi)
    y.append(yi)


a = y.copy()


for k in range(1, n):
    for i in range(n-1, k-1, -1):
        a[i] = (a[i] - a[i-1]) / (x[i] - x[i-1]) #division durch null geht nicht !! 

# jetzt das polynom machen
X = symbols("x")
p = 0

for i in range(n):
    t = a[i]
    for j in range(i):
        t = t * (X - x[j])
    p = p + t

p = simplify(p)

print("Das Newton-Polynom ist:")
print(p)