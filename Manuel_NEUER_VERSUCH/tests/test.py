

from polynom import Polynom
from lagrange import lagrange_basis, lagrange_interpolation
from newton import newton_basis, newton_interpolation
from hermite import hermite_interpolation


# -----------------------------------------------------------
# 1. Test Polynom-Grundfunktionen
# -----------------------------------------------------------

def test_polynom_addition():
    p = Polynom([1, 2])   # 1 + 2x
    q = Polynom([3, 4])   # 3 + 4x
    r = p + q
    assert r.coeffs == [4, 6]


def test_polynom_multiplikation():
    p = Polynom([1, 1])     # (x + 1)
    q = Polynom([1, -1])    # (x - 1)
    r = p * q               # x^2 - 1
    assert r.coeffs == [-1, 0, 1]


def test_horner():
    p = Polynom([2, 0, 1])   # 2 + x²
    assert p.horner(3) == 11


# -----------------------------------------------------------
# 2. Test Lagrange-Interpolation
# -----------------------------------------------------------

def test_lagrange_basis_simple():
    x = [1, 2]
    L0 = lagrange_basis(x, 0)    # L0(x) = (x - 2)/(1 - 2) = -x + 2
    L1 = lagrange_basis(x, 1)    # L1(x) = (x - 1)/(2 - 1) = x - 1

    assert L0.coeffs == [2, -1]
    assert L1.coeffs == [-1, 1]


def test_lagrange_interpolation_linear():
    x = [1, 3]
    y = [2, 4]  # f(x) = x + 1

    P = lagrange_interpolation(x, y)

    assert P.horner(1) == 2
    assert P.horner(3) == 4
    assert P.horner(2) == 3   # Zwischenwert


# -----------------------------------------------------------
# 3. Test Newton-Interpolation
# -----------------------------------------------------------

def test_newton_basis():
    x = [1, 3]

    N0 = newton_basis(x, 0)
    N1 = newton_basis(x, 1)

    assert N0.coeffs == [1]           # N0(x) = 1
    assert N1.coeffs == [-1, 1]       # (x - 1)


def test_newton_interpolation_linear():
    x = [1, 3]
    y = [2, 4]  # f(x) = x + 1

    P = newton_interpolation(x, y)

    assert P.horner(1) == 2
    assert P.horner(3) == 4
    assert P.horner(2) == 3


# -----------------------------------------------------------
# 4. Test Hermite-Interpolation
# -----------------------------------------------------------

def test_hermite_constant():
    x = [2]
    y = [[5]]  # nur Funktionswert

    H = hermite_interpolation(x, y)

    assert H.horner(2) == 5
    assert H.horner(10) == 5


def test_hermite_first_derivative():
    # f(1) = 2, f'(1) = 3
    x = [1]
    y = [[2, 3]]

    # Hermite: H(x) = 2 + 3(x - 1)
    H = hermite_interpolation(x, y)

    assert H.horner(1) == 2
    assert H.horner(2) == 5  # 2 + 3*(2-1)


def test_hermite_two_points():
    # Punkte: (1,2), (3,4)
    # Ableitung bei x=1: f'(1)=1
    x = [1, 3]
    y = [[2, 1], [4]]  # nur 1 Ableitung bei der ersten Stelle

    H = hermite_interpolation(x, y)

    assert H.horner(1) == 2
    assert H.horner(3) == 4
