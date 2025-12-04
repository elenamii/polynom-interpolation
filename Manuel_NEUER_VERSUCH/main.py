from io_input import einlesen_stuetzstellen, horner
from interpolation import interpolate

def menu():
    print("\n--- Polynom-Interpolation ---")
    print("1. Lagrange-Interpolation")
    print("2. Newton-Interpolation")
    print("3. Hermite-Interpolation")
    print("4. Beenden")
    return input("Bitte wählen Sie eine Option (1-4): ")

def main():
    print("Willkommen zur Polynom-Interpolation!")
    while True:
        wahl = menu()
        if wahl == "4":
            break

        x_wert, y_wert = einlesen_stuetzstellen()

        if wahl == "1":
            method = "lagrange"
            y_input = [y[0] for y in y_wert]  # nur Funktionswerte
        elif wahl == "2":
            method = "newton"
            y_input = [y[0] for y in y_wert]
        elif wahl == "3":
            method = "hermite"
            y_input = y_wert
        else:
            print("Ungültige Auswahl. Bitte 1-4 eingeben.")
            continue

        basis, P, extra = interpolate(method, x_wert, y_input)

        print(f"\nInterpolationspolynom P(x) = {P}")
        x_eval = float(input("Polynom an welcher Stelle auswerten? "))
        wert = horner(P, x_eval)
        print(f"P({x_eval}) = {wert}")

if __name__ == "__main__":
    main()
