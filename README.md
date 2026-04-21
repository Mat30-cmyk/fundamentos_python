# 🐍 Fundamentos de Python

Este repositorio contiene el desarrollo de la actividad GA1-220501093-04-AA1-EV01, enfocada en los fundamentos básicos de Python.

El proyecto tiene como objetivo aplicar conceptos esenciales como:
- Uso de la función print()
- Manejo de variables
- Literales y tipos de datos
- Operadores aritméticos y de comparación
- Manipulación básica de cadenas

## 📂 Estructura del proyecto

El repositorio está organizado en secciones, cada una correspondiente a los laboratorios desarrollados:

- **seccion1:** Introducción a Python y uso de print()
- **seccion2:** Literales y cadenas
- **seccion3:** Operadores matemáticos
- **seccion4:** Variables y expresiones
- src: Archivo adicional del proyecto

### Sección 1 – El Programa "¡Hola, Mundo!"

### Ejecución

Para ejecutar los archivos, se utiliza Python desde la terminal:

* Laboratorio: Trabajando con la función print()
```bash
python seccion1/hola_mundo.py
```

* Laboratorio: La función print() y sus argumentos
```bash
python seccion1/print_argumentos.py
```

* Laboratorio: La función print() y sus argumentos
```bash
python seccion1/formato_salida.py  
```

### Laboratorio: Trabajando con la función print()
- codigo:

```bash
# --- PASO 1 y 2: Impresión básica ---

# print(¡Hola, Mundo!) # Esto causaría SyntaxError: invalid character '¡' (U+00A1)
# print "¡Hola, Mundo!" # Esto causaría SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?

print("¡Hola, Mundo!")
print("Mi Nombre Es Mateo Betancur Escobar De la Ficha: 3144585") # Sustituye con tu nombre real

# --- PASO 5: Experimentación ---
# Comillas simples (Funcionan igual que las dobles)
print('Esta es una cadena con comillas simples')

# Múltiples print en la misma línea (Usando punto y coma, aunque no es común en Python)
print("Primera parte"); print("Segunda parte")

# Múltiples argumentos en un solo print
print("Hola,", "esto", "son", "varios", "argumentos", sep="-")
```

##### Análisis de Errores (Pruebas de Resiliencia):

**`Sin comillas:`** Al ejecutar print(Hola Mundo) ¿Qué tipo de error arroja? R/ Python arroja un NameError.

**`Lógica:`** Python intenta interpretar "Hola" como una variable que no ha sido definida.

**`Sin paréntesis:`** Al ejecutar print "¡Hola, Mundo!" ¿Qué tipo de error arroja esta vez? R/ Python arroja un SyntaxError.

**`Lógica:`** En Python 3, print es una función y obligatoriamente requiere paréntesis para contener sus argumentos.

##### Conclusiones de la experimentación:

Las comillas simples ' ' y dobles " " son intercambiables para definir cadenas.

Cada instrucción print() genera automáticamente un salto de línea al final, a menos que se modifique el argumento end.

### Laboratorio: La función print() y sus argumentos

```bash
print("Mi nombre es", "Mateo")

# Primera línea: modificada con sep y end
print("Programming", "Essentials", "in", sep="***", end="...")

# Segunda línea: NO se debe cambiar
print("Python")

print("Hola", "mundo", sep="-")
```

**`Objetivo:`** Manipular la salida estándar mediante argumentos de palabra clave.

**`Desafío:`** Evitar el salto de línea automático y cambiar el espacio por caracteres personalizados.

**`Solución:`** Se utilizó sep="***" para cumplir con el formato entre palabras y end="..." para concatenar la salida del primer print con el segundo sin romper la línea.

### Laboratorio: La función print() y sus argumentos

```bash
print("Flecha de Salida Original")
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

# Versión minimalista de la flecha original
print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")

#Duplicar el tamaño (Manteniendo proporciones)
print("        *")
print("       * *")
# Print("     *     *") # Esto causaría SyntaxError: invalid character '¡' (U+00A1)pPrint("      *   *")
print("     *     *")
# print"    *       *" # Esto causaría SyntaxError: invalid character '¡' (U+00A1)
print("    *       *")
print("   *         *")
# print(  *           *) # Esto causaría SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print("  *           *")
print(" *             *")
print("******     ******")
print("     *     *")
print("     *     *")
print('     *     *')
print("     *******")  

# Ejemplo de las primeras líneas duplicadas
print("    *" * 2)
print("   * *" * 2)
print("  *   *" * 2)
print(" *     *" * 2)
print("***   ***" * 2)
print("  *   *" * 2)
print("  *   *" * 2)
print("  *****" * 2)
```

#### Análisis de errores (Lo que debes documentar)

* **Mayúsculas en Print:** Al cambiarlo, Python arroja un NameError. Conclusión: Python es case-sensitive (distingue mayúsculas de minúsculas). print es la función correcta, Print no existe.

* **Quitar comillas:** Python marca el error, pero a veces el cursor del error aparece un poco después de donde falta la comilla. Conclusión: El intérprete nota que algo anda mal cuando llega al final de la línea sin encontrar el cierre.

* **Comillas vs Apóstrofes:** Python acepta ambos (" o '). Conclusión: Son equivalentes, pero si empiezas con una, debes cerrar con la misma.

* **Quitar paréntesis:** Produce un SyntaxError. Conclusión: En Python 3, los paréntesis son obligatorios porque print es una función, no una palabra clave como en versiones antiguas (Python 2).

## Sección 2 – Literales de Python

### Laboratorio: Literales de Python - Cadenas
* codigo:

```bash
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
```

**El reto:** Imprimir "Estoy" ""aprendiendo"" """Python""" en una sola línea de código usando escapes.

**Solución:**
Para que aparezcan las comillas dobles dentro de una cadena que ya usa comillas dobles, debemos "escaparlas" con la barra invertida (\).

```bash
print("\"Estoy\"\n\"\"aprendiendo\"\"\n\"\"\"Python\"\"\"")
```

#### ¿Por qué funciona?

* \" le dice a Python: "No cierres la cadena, solo imprime una comilla".

* \n crea el salto de línea para que las palabras queden una debajo de otra (según el formato de salida esperado usual en este lab).

### Experimentos con otros Literales
Para demostrar que Domino la sección 2, añado estos ejemplos en mi código:

```bash
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
```

#### Literales de Python
En esta sección exploré cómo Python interpreta los datos según su formato:

+ **Legibilidad:** Utilicé guiones bajos (_) en números grandes, lo cual facilita la lectura sin afectar el valor.

+ **Bases Numéricas:** Implementé literales en Octal y Hexadecimal, observando cómo Python realiza la conversión a base 10 automáticamente en la salida.

+ **Escapado de caracteres:** Resolví el reto de imprimir comillas dobles anidadas usando la barra invertida (\) como carácter de escape.

+ **Precisión:** Diferencié entre 4 (entero) y 4. (flotante), entendiendo que el punto decimal cambia la forma en que la computadora almacena el dato.

## Sección 3 - Operadores - herramientas de manipulación de datos

### Ejercicios de Operadores - Matematicos

+ codigo:

```bash
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
```

**Explicación:** esta explicación esta en el archivo `operadores.md`.