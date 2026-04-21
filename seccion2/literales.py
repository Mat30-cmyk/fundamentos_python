# GA1-220501093-04-AA1-EV01 - Sección 2: Literales

# --- LAB: Literales de Python - Cadenas ---
# Objetivo: Imprimir comillas triples y múltiples usando escapes y saltos de línea
print("\"Estoy\"\n\"\"aprendiendo\"\"\n\"\"\"Python\"\"\"")

print("\n--- Experimentos con otros Literales ---")

# Cadenas vs números: Se ven igual, pero se procesan distinto
print("2")   # Tipo: str (string)
print(2)     # Tipo: int (integer)

# Enteros: Uso de guiones bajos (Python 3.6+) para legibilidad en números grandes
print(11_111_111)

# Octal (0o) y Hexadecimal (0x): Conversión automática a decimal
print(0o123) # Resultado: 83
print(0x123) # Resultado: 291

# Flotantes: El punto decimal define el tipo de dato
print(.4)    # Equivalente a 0.4
print(4.)    # Equivalente a 4.0

# Notación científica: Para números muy grandes o muy pequeños
print(3E8)         # Velocidad de la luz aprox.
print(6.62607E-34) # Constante de Planck

# Booleanos: Python los evalúa internamente como 1 (True) y 0 (False)
print("¿Es True mayor que False?", True > False)

# None: Representa la ausencia de valor
print(None)