# Code Dokumentation

In diesem Dokument werden Funktionen, Methoden und andere theoretische Grundlagen erklärt bzw. dokumentiert.

## poly_add Theorie

```text
p = [1,2,3] --> 1*x^0 + 2*x^1 + 3*x^2
q = [5,6]   --> 5*x^0 + 6*x^1

p(x) + q(x) = (1+5)*x^0 + (2+6)*x^1 + (3+0)*x^2
            = (1+5) + (2+6)x + (3+0)x^2
            --> Array aus Koeffizienten: [6, 8, 3]
```

## poly_add Funktion

**INPUT:**
- `p`: Liste von Koeffizienten eines Polynoms
- `q`: Liste von Koeffizienten eines anderen Polynoms

**OUTPUT:**
- Liste von Koeffizienten des Summenpolynoms

**BESONDERHEITEN:**
- Wenn ein Polynom kürzer ist (also kleiner als `max_length`), werden die fehlenden Koeffizienten wie Nullen behandelt.
- `try/except IndexError` wird verwendet, um zu erkennen, dass ein Polynom kürzer ist. Wenn man auf einen nicht vorhandenen Index zugreift, kommt der Fehler „Index out of range“, und in diesem Fall wird der fehlende Koeffizient automatisch auf 0 gesetzt.

---

## poly_mult Theorie

```text
p = [1,2,3] --> 1*x^0 + 2*x^1 + 3*x^2
q = [5,6]   --> 5*x^0 + 6*x^1

p(x) * q(x) = 1*5 + 1*6x + 2x*5 + 2x*6x + 3x^2*5 + 3x^2*6x
            = 1*5 + (1*6 + 2*5)x + (2*6 + 3*5)x^2 + (3*6)x^3
            = 5 + 16x + 27x^2 + 18x^3
            --> Array aus Koeffizienten: [5, 16, 27, 18]
```

## poly_mult Funktion

**INPUT:**
- `p`: Liste von Koeffizienten eines Polynoms
- `q`: Liste von Koeffizienten eines anderen Polynoms

**OUTPUT:**
- Liste von Koeffizienten des Produktpolynoms

**BESONDERHEITEN:**
- Länge des Ergebnisses = `len(p) + len(q) - 1`
- Liste wird erst mit Nullen gefüllt: `result = [0] * (len(p) + len(q) - 1)`
  - Produkte können direkt an Index `i + j` addiert werden.
- Jede Schleife geht durch alle Koeffizienten:
  - Iteration über alle Koeffizienten von `p` und `q`
  - Alle Kombinationen werden multipliziert: `p[i] * q[j]`
- Addieren an der richtigen Position: Index `position = i + j` → Potenz von `x`
- Produkte werden aufaddiert, falls mehrere Terme die gleiche Potenz haben: `result[position] += p[i] * q[j]`

**POLYNOM SCHREIBWEISE**
- das ausgegebene Array muss umgewandelt werden in feste INTEGER -> dann löst sich auch das Problem von negativen Zahlen (funktioniert das mit INT (eig ja))
- je nach Länge des Arrays muss umgekehrt ausgegeben werden
- [i0,i1,i2] usw
- = [1,2,3]
- 1x^0 + 2x^1 (=2x) + 3x^2 usw
- > Ausgabe Polynomschreibweise
- Ausgabe muss umgekehrt werden, i0 kann nicht ^0 sein, weil bei Polynomschreibweise ist das erste dementsprechend, dass höchste HEIßT bei 3 teilen  i0 = ^2
- Ausgabe muss anpassbar sein je nach EIngabe von Stützpunkten (?)
- UM EXPONENT VERÄNDERN ZU KÖNNEN i0 = Anzahl n aller i
HEIßT i1 = ANZAHL i-1
usw

Weietre Hinweise: 
Der Index vom Array ist identisch mit der Potenz von x
        d.h. z. B. [1,2,3] => 1* x^0 + 2*x^1 + 3*x^2
        wobei 1,2,3 die Koeff. und der Index: [i0,i1,i2] (wie @Paula schon erklärt hat)

Des Weitern muss bei der Ausgabe auf folgendes geachtet werden: (details)
        - Vorzeichen müssen beim ersten Koeff. nur angegeben werden wenn es ein minus ist 
            => -2x + 3 , aber nicht +2x + 3
        - Wenn der Koeffizeint 0 ist, sollte der Term nicht aufgelistet werden 
            => 2x^3 + 4x + 2 , aber nicht 2x^3 + 0x^2+ 4x + 2
        - Wenn es x^1 ist sollte es nur x in der Ausgabe sein, genau so sollte x^0, was 1 ergibt, nicht zusätzlich aufgelistet sein 
            => 3x + 2 , aber nicht 3x^1 + 2x^0 


## poly_number_mult Theorie 
```text
p = [1,2,3] --> 1*x^0 + 2*x^1 + 3*x^2
number = 2

p(x) * 2 = 1*2 + 2*2 + 3*2
            = 2 + 4 + 6 
            --> Array aus Koeffizienten: [2, 4, 6]
```

## poly_number_mult Funktion 
**INPUT:**
- `p`: Liste von Koeffizienten eines Polynoms
- `number`: Zahl 

**OUTPUT:**
- Liste von Koeffizienten des Produktpolynoms

**BESONDERHEITEN:**
- Jeder Koeffizient des Polynoms wird iteriert und mit der `number` multipliziert

##to do: dokumentation für poly_number_mult, poly_number_div und lagrange hinzufügen 
