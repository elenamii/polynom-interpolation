

from polynom import Polynom
from lagrange import lagrange_basis, lagrange_interpolation
from newton import newton_basis, newton_interpolation
from hermite import hermite_interpolation

    
def test_polynom_mult():
    p1 = Polynom([2, 3])   # 1 + 2x
    p2 = Polynom([-3, 1])   # 3 + 4x
    result = p1 * p2       # sollte 3 + 10x + 8x² ergeben
    print(result)
test_polynom_mult()


#zum eigenständigen testen der multiplikationsfunktion (muss man händisch im code eingeben)
from polynom import MathWithPolynomials  


p = [2, 3, 1]      
q = [-3, 1]         

result = MathWithPolynomials.poly_mul(p, q)

print("p =", MathWithPolynomials.print_poly_schoen(p))
print("q =", MathWithPolynomials.print_poly_schoen(q))
print("p * q =", MathWithPolynomials.print_poly_schoen(result))
