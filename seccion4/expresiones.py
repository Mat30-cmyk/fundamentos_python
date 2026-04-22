# GA1-220501093-04-AA1-EV01 - Sección 4: Variables

# Escenario: Evaluar un polinomio para un valor de x dado

# -- Variable de entrada
#x = float(input("Ingrese valor de x: ")) Esta Linea de codigo es para facilitarlo y solo poner el numero que quiero en la misma terminal.
x = -1  # Puedes cambiar este valor (ej: 0, 1, -1)

# -- Convertimos a tipo flotante (decimal)
# Esto asegura que el resultado tenga decimales si es necesario
x = float(x)

# -- Polinomio: 3x^3 - 2x^2 + 3x - 1
# ** significa potencia
# x**3 = x elevado a la 3
# x**2 = x elevado a la 2

y = 3 * x**3 - 2 * x**2 + 3 * x - 1

# -- Mostrar resultado
print("y =", y)