from io_input import einlesen_stuetzstellen
from lagrange import lagrange_interpolation, lagrange_basis
from newton import newton_interpolation
from hermite import hermite_interpolation

def menu():
    print("\n--- Polynom-Interpolation ---")
    print("1. Lagrange-Interpolation")
    print("2. Newton-Interpolation")
    print("3. Hermite-Interpolation")
    print("4. Beenden")
    return input("Bitte wählen Sie eine Option (1-4): ")

def auswahl_lagrange(x_wert, y_wert):
    print("\n--- Lagrange-Basis-Polynome ---")
    for i in range(len(x_wert)):
        L = lagrange_basis(x_wert, i)
        print(f"L_{i}(x) = {L}")

    print("\n--- Lagrange-Interpolationspolynom ---")
    P = lagrange_interpolation(x_wert, [y[0] for y in y_wert])
    print(f"P(x) = {P}")

    x_eval = float(input("\nPolynom an welcher Stelle auswerten? "))
    wert = P.horner(x_eval)
    print(f"P({x_eval}) = {wert}")

def auswahl_newton(x_wert, y_wert):
    P = newton_interpolation(x_wert, [y[0] for y in y_wert])
    print(f"Newton-Interpolationspolynom: {P}")

    x_eval = float(input("\nPolynom an welcher Stelle auswerten? "))
    wert = P.horner(x_eval)
    print(f"P({x_eval}) = {wert}")

def auswahl_hermite(x_wert, y_wert):
    if not any(len(y) > 1 for y in y_wert):
        print("Keine Ableitungen eingegeben. Hermite entspricht Lagrange.")
    P = hermite_interpolation(x_wert, y_wert)
    print(f"Hermite-Interpolationspolynom: {P}")

    x_eval = float(input("\nPolynom an welcher Stelle auswerten? "))
    wert = P.horner(x_eval)
    print(f"P({x_eval}) = {wert}")

def main():
    print("Willkommen zur Polynom-Interpolation!")
    while True:
        wahl = menu()

        if wahl == "4":
            print("Programm wird beendet.")
            break

        x_wert, y_wert = einlesen_stuetzstellen()

        if wahl == "1":
            auswahl_lagrange(x_wert, y_wert)
        elif wahl == "2":
            auswahl_newton(x_wert, y_wert)
        elif wahl == "3":
            auswahl_hermite(x_wert, y_wert)
        else:
            print("Ungültige Auswahl. Bitte 1-4 eingeben.")

if __name__ == "__main__":
    main()
