print(input("Gebe etwas ein: "))

def avg(x_array):
    return (sum(x_array) / len(x_array))

x_array = input("Gebe mehrere Zahlen durch Komma getrennt ein: ").split(",")
x_array = [int(x) for x in x_array]
print(x_array)
print(x_array[0])

print("Durchschnitt:", avg(x_array))

# for x in range(1000):
    # print(x)

class Auto:
    def __init__(self, marke, baujahr):
        self.marke = marke
        self.baujahr = baujahr
        self.kilometerstand = 0
        self.tankinhalt = 0
        self.verbrauch = 7.5  # Liter pro 100 km

    def starten(self):
        print(f"Das Auto der Marke {self.marke} aus dem Jahr {self.baujahr} startet.")

    def stoppen(self):
        print(f"Das Auto der Marke {self.marke} aus dem Jahr {self.baujahr} stoppt.")
    
    def fahren(self, kilometer):
        benoetigter_treibstoff = (self.verbrauch / 100) * kilometer
        if benoetigter_treibstoff <= self.tankinhalt:
            self.kilometerstand += kilometer
            self.tankinhalt -= benoetigter_treibstoff
            print(f"Das Auto ist {kilometer} km gefahren.")
        else:
            print(f"Nicht genug Treibstoff zum Fahren. Sie müssen {benoetigter_treibstoff - self.tankinhalt:.2f} Liter mehr tanken.")

    def tanken(self, liter):
        self.tankinhalt += liter
        print(f"Das Auto wurde mit {liter} Litern getankt.")

    def status_anzeigen(self):
        print(f"Marke: {self.marke}, Baujahr: {self.baujahr}, Kilometerstand: {self.kilometerstand} km, Tankinhalt: {self.tankinhalt} L")

neuesAuto = Auto("BMW", 1995)
neuesAuto.starten()
neuesAuto.tanken(900)
neuesAuto.fahren(10000)
neuesAuto.status_anzeigen()

def fakultaet(n):
    if n < 0:
        return "Ungültige Eingabe"
    elif n == 0:
        return 1
    else:
        return n * fakultaet(n - 1)
    
# print("Fakultät von 5:", fakultaet(1))
# for i in range(-5, 5):
    # print(f'Fakultät von {i}:', fakultaet(i))