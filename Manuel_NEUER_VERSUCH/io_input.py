from interpolation import interpolate

# Beispiel für Lagrange:
basis, P, extra = interpolate("lagrange", x_wert, [y[0] for y in y_wert])

# Beispiel für Newton:
basis, P, extra = interpolate("newton", x_wert, [y[0] for y in y_wert])

# Beispiel für Hermite:
basis, P, extra = interpolate("hermite", x_wert, y_wert)
