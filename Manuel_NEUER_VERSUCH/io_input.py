# io_input.py
"""
Dieses Modul kümmert sich um:
- Einlesen von Stützstellen und Stützwerten/Ableitungen
- Hilfsfunktionen wie Horner-Schema und Multiplizieren von Linearfaktoren
"""

from polynom import Polynom
from typing import List, Tuple

def einlesen_stuetzstellen() -> Tuple[List[float], List[List[float]]]:
    """
    Liest beliebige Anzahl Stützstellen mit Funktionswerten und Ableitungen ein.
    - x-Werte: Liste der Stützstellen
    - y-Werte: Liste der Listen: [y, y', y'', ...] bei Hermite
    """
    n = int(input("Wie viele Stützstellen möchten Sie eingeben? "))
    x_wert: List[float] = []
    y_wert: List[List[float]] = []

    print("Hinweis: Für Hermite-Interpolation geben Sie mehrere Werte durch Komma getrennt ein.")
    print("Beispiel: Funktionswert, 1. Ableitung, 2. Ableitung ...")

    for i in range(n):
        x = float(input(f"x_{i} = "))
        x_wert.append(x)

        y_eingabe = input(f"y_{i} oder y_{i}, y'_{i}, ... bei Ableitungen: ")
        y_liste = [float(val) for val in y_eingabe.split(",")]
        y_wert.append(y_liste)

    return x_wert, y_wert

#def horner(poly: Polynom, x: float) -> float:
    """
    Horner-Schema zur effizienten Auswertung eines Polynoms poly an der Stelle x.
    """
    result = 0
    for coef in reversed(poly.coeffs):
        result = result * x + coef
    return result

def ausmultiplizieren_linearfaktoren(faktoren: List[Polynom]) -> Polynom:
    """
    Multipliziert eine Liste von Linearfaktoren (Polynomen) aus.
    faktoren: Liste von Polynom-Instanzen
    """
    P = Polynom([1])
    for f in faktoren:
        P = P * f
    return P
