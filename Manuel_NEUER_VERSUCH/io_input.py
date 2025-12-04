from polynom import Polynom

def einlesen_stuetzstellen():
    n = int(input("Wie viele Stützstellen möchten Sie eingeben? "))
    x_wert = []
    y_wert = []
    for i in range(n):
        x = float(input(f"x_{i} = "))
        x_wert.append(x)
        y_eingabe = input(f"y_{i} oder y_{i}, y'_{i}, ... bei Ableitungen: ")
        y_liste = [float(val) for val in y_eingabe.split(",")]
        y_wert.append(y_liste)
    return x_wert, y_wert

def horner(poly: Polynom, x: float) -> float:
    result = 0
    for coef in reversed(poly.coeffs):
        result = result * x + coef
    return result

def ausmultiplizieren_linearfaktoren(faktoren: list[Polynom]) -> Polynom:
    P = Polynom([1])
    for f in faktoren:
        P = P * f
    return P
