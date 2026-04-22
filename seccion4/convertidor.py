# GA1-220501093-04-AA1-EV01 - Sección 4: Variables

# Escenario: Convertidor de Millas a Kilómetros y viceversa

# -- Variables de entrada
kilometers = 12.25   # cantidad en kilómetros
miles = 7.38         # cantidad en millas

# -- Conversión de millas a kilómetros
# Sabemos que: 1 milla = 1.61 kilómetros
# Entonces multiplicamos las millas por 1.61
miles_to_kilometers = miles * 1.61

# -- Conversión de kilómetros a millas
# Para convertir al revés, dividimos entre 1.61
kilometers_to_miles = kilometers / 1.61

# -- Mostrar resultados en pantalla
# round(valor, 2) redondea el resultado a 2 decimales

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
# Ejemplo: 7.38 millas → 11.88 km

print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")
# Ejemplo: 12.25 km → 7.61 millas