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

