

from polynom import Polynom
from lagrange import lagrange_basis, lagrange_interpolation
from newton import newton_basis, newton_interpolation
from hermite import hermite_interpolation

    
def test_polynom_mult():
    p1 = Polynom([1, 2])   # 1 + 2x
    p2 = Polynom([3, 4])   # 3 + 4x
    result = p1 * p2       # sollte 3 + 10x + 8x² ergeben
    print(result)
test_polynom_mult()
