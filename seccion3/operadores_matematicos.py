# GA1-220501093-04-AA1-EV01 - Sección 3: Operadores

print("-" * 40)
print("VALIDACIÓN DE OPERADORES MATEMÁTICOS")
print("-" * 40)

# Ejercicio 1: Multiplicación antes que suma
# 5 + (3 * 2) -> 5 + 6 = 11
print(f"Ejercicio 1: [5 + 3 * 2]    -> Resultado: {5 + 3 * 2}")

# Ejercicio 2: Prioridad de Multiplicación/División sobre Suma
# Proceso: (8 / 2) + (4 * 3) -> 4.0 + 12
print(f"Ejercicio 2:  [8 / 2 + 4 * 3]     -> Resultado: {8 / 2 + 4 * 3}")

# Ejercicio 3: El Paréntesis tiene la prioridad máxima
# Proceso: (10) * 2 - 5 -> 20 - 5
print(f"Ejercicio 3:  [(7 + 3) * 2 - 5]   -> Resultado: {(7 + 3) * 2 - 5}")

# Ejercicio 4: Multiplicación antes que suma/resta
# 10 - 4 + (2 * 3) -> 10 - 4 + 6 = 12
print(f"Ejercicio 4: [10 - 4 + 2 * 3]   -> Resultado: {10 - 4 + 2 * 3}")

# Ejercicio 5: Mezcla de flotantes y enteros
# Proceso: (5.0) * (5) - 4 -> 25.0 - 4 (El resultado es flotante por la división /)
print(f"Ejercicio 5:  [(10/2)*(3+2)-4]    -> Resultado: {(10 / 2) * (3 + 2) - 4}")

# Ejercicio 6: Paréntesis interno primero
# 2 + 3 * (3) -> 2 + 9 = 11
print(f"Ejercicio 6: [2 + 3 * (4 - 1)]    -> Resultado: {2 + 3 * (4 - 1)}")

# Ejercicio 7: La Exponenciación (**) es superior a la Multiplicación
# Proceso: 5 * (2^3) -> 5 * 8
print(f"Ejercicio 7:  [5 * 2 ** 3]        -> Resultado: {5 * 2 ** 3}")

# Ejercicio 8: Exponente -> División -> Suma
# 6 + 4 / (4) -> 6 + 1.0 = 7.0
print(f"Ejercicio 8: [6 + 4 / 2 ** 2]     -> Resultado: {6 + 4 / 2 ** 2}")

# Ejercicio 9: Módulo (%) tiene la misma prioridad que la multiplicación
# Proceso: (10 % 3) + (2 * 5) -> 1 + 10
print(f"Ejercicio 9:  [10 % 3 + 2 * 5]    -> Resultado: {10 % 3 + 2 * 5}")

# Ejercicio 10: Paréntesis -> Exponente -> Multiplicación
# (10) * (3^2) -> 10 * 9 = 90
print(f"Ejercicio 10: (8 + 2) * 3 ** 2    -> Resultado: {(8 + 2) * 3 ** 2}")

# Ejercicio 11: Paréntesis -> Multiplicación -> División -> Suma
# 7 + (2 * 8) / 4 -> 7 + 16 / 4 -> 7 + 4.0 = 11.0
print(f"Ejercicio 11: [7 + 2 * (3 + 5) / 4]   -> Resultado: {7 + 2 * (3 + 5) / 4}")

# Ejercicio 12: Enlazado de izquierda a derecha (Misma prioridad)
# Proceso: ((2^3) * 4) / 2 -> (8 * 4) / 2 -> 32 / 2
print(f"Ejercicio 12: [2 ** 3 * 4 / 2]    -> Resultado: {2 ** 3 * 4 / 2}")

# Ejercicio 13: Exponente -> Suma/Resta
# 9 - 6 + (9) -> 12
print(f"Ejercicio 13: [9 - 6 + 3 ** 2]    -> Resultado: {9 - 6 + 3 ** 2}")

# Ejercicio 14: Paréntesis y Exponente -> Multiplicación -> Suma
# (5 * 5) + 9 -> 25 + 9 = 34
print(f"Ejercicio 14: [(7 - 2) * 5 + 3 ** 2]  -> Resultado: {(7 - 2) * 5 + 3 ** 2}")

# Ejercicio 15: Operación compleja combinada
# Proceso: (4 * (2^3) / 8) + 1 -> (4 * 8 / 8) + 1 -> (32 / 8) + 1 -> 4.0 + 1
print(f"Ejercicio 15: [4 * 2 ** 3 / 8 + 1]-> Resultado: {4 * 2 ** 3 / 8 + 1}")

print("-" * 40)
print("Nota: Los resultados con '.0' indican que el tipo de dato es FLOAT.") 