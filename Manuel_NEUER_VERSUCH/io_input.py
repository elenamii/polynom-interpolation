from polynom import Polynom

def horner(poly: Polynom, x: float) -> float:
    return poly.horner(x)

def einlesen_stuetzstellen():
    print("Geben Sie die Stützstellen und Stützwerte ein.")
    print("Für Hermite-Interpolation geben Sie gleiche x-Werte mehrfach ein.")
    print("Die zugehörigen y-Werte werden als f(x), f'(x), f''(x) usw. interpretiert.")
    print("Geben Sie 'q' als x-Wert ein, um die Eingabe zu beenden.")

    data = {} # Dictionary to store x -> list of y values
    order = [] # To preserve order of first insertion of x

    while True:
        x_input = input("x-Wert: ")
        if x_input.lower() == 'q':
            break
        
        try:
            x = float(x_input)
        except ValueError:
            print("Ungültige Eingabe. Bitte eine Zahl eingeben.")
            continue

        y_input = input(f"y-Wert für x={x}: ")
        try:
            y = float(y_input)
        except ValueError:
            print("Ungültige Eingabe. Bitte eine Zahl eingeben.")
            continue

        if x not in data:
            data[x] = []
            order.append(x)
        
        data[x].append(y)

    x_wert = order
    y_wert = [data[x] for x in order]

    return x_wert, y_wert
