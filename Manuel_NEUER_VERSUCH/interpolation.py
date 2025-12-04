from lagrange import lagrange_interpolation
from newton import newton_interpolation
from hermite import hermite_interpolation

def interpolate(method, x, y):
    """
    Vereinheitlichte Schnittstelle für alle Interpolationsmethoden.
    Rückgabe: basis_polynome, interpolationspolynom, extra_info
    """
    if method == "lagrange":
        return lagrange_interpolation(x, y)
    elif method == "newton":
        return newton_interpolation(x, y)
    elif method == "hermite":
        return hermite_interpolation(x, y)
    else:
        raise ValueError(f"Unbekannte Methode: {method}")
