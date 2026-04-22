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

## Ejecución Proyecto:

+ Abrir CMD y Pegar:

```bash
git clone https://github.com/Mat30-cmyk/fundamentos_python.git
```

+ luego ingresamos al repositorio:

```bash
cd fundamentos_python
```

### Sección 1 – El Programa "¡Hola, Mundo!"

### Ejecución

Para ejecutar los archivos, se utiliza Python desde la terminal:

* **Laboratorio:** Trabajando con la función print()
```bash
python seccion1/hola_mundo.py
```

* **Laboratorio:** La función print() y sus argumentos
```bash
python seccion1/print_argumentos.py
```

* **Laboratorio:** La función print() y sus argumentos
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
<img width="1434" height="110" alt="Captura de pantalla 2026-04-21 153558" src="https://github.com/user-attachments/assets/d0f3e419-adaa-4261-a292-4c5388fd6686" />

**`Lógica:`** Python intenta interpretar "Hola" como una variable que no ha sido definida.

**`Sin paréntesis:`** Al ejecutar print "¡Hola, Mundo!" ¿Qué tipo de error arroja esta vez? R/ Python arroja un SyntaxError.
<img width="1436" height="114" alt="Captura de pantalla 2026-04-21 153625" src="https://github.com/user-attachments/assets/5673df4a-5471-452c-8bc7-9619f331bd93" />

**`Lógica:`** En Python 3, print es una función y obligatoriamente requiere paréntesis para contener sus argumentos.

##### Conclusiones de la experimentación:

Las comillas simples ' ' y dobles " " son intercambiables para definir cadenas.

Cada instrucción print() genera automáticamente un salto de línea al final, a menos que se modifique el argumento end.

### Laboratorio: La función print() y sus argumentos

- codigo:

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

- codigo:

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
<img width="1455" height="113" alt="Captura de pantalla 2026-04-21 222712" src="https://github.com/user-attachments/assets/7dc6a10a-e78f-4caf-a8ca-629ae34aa480" />

* **Quitar comillas:** Python marca el error, pero a veces el cursor del error aparece un poco después de donde falta la comilla. Conclusión: El intérprete nota que algo anda mal cuando llega al final de la línea sin encontrar el cierre.
<img width="1473" height="137" alt="Captura de pantalla 2026-04-21 222842" src="https://github.com/user-attachments/assets/79d4e9b0-e7af-47ef-905c-2112d38889a0" />

* **Comillas vs Apóstrofes:** Python acepta ambos (" o '). Conclusión: Son equivalentes, pero si empiezas con una, debes cerrar con la misma.
<img width="1420" height="745" alt="Captura de pantalla 2026-04-21 223102" src="https://github.com/user-attachments/assets/ad0b96d7-636c-408d-9c1e-432559233321" />

* **Quitar paréntesis:** Produce un SyntaxError. Conclusión: En Python 3, los paréntesis son obligatorios porque print es una función, no una palabra clave como en versiones antiguas (Python 2).
<img width="1463" height="134" alt="Captura de pantalla 2026-04-21 155930" src="https://github.com/user-attachments/assets/ae86e74e-a175-4d53-900c-eeee3ff8e906" />

## Sección 2 – Literales de Python

### Ejecución

Para ejecutar los archivos, se utiliza Python desde la terminal:

* **Laboratorio:** Literales de Python - Cadenas
```bash
python seccion2/literales.py
```

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

### Ejecución

Para ejecutar los archivos, se utiliza Python desde la terminal:

* Ejercicios de Operadores - Matematicos:
```bash
python seccion3/operadores_matematicos.py
```

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

## Sección 4 – Variables y Expresiones

### Ejecución
Para ejecutar los archivos, se utiliza Python desde la terminal:

+ **Laboratorio:** Convertidor de Millas a Kilómetros

```Bash
python seccion4/convertidor.py
```
+ **Laboratorio:** Operadores y expresiones (Polinomio)

```Bash
python seccion4/expresiones.py
```

+ **Laboratorio:** Ejercicios de Algoritmos (Gameplay)

```Bash
python seccion4/variables.py
```

### Laboratorio: Variables - Un convertidor simple

+ Codigo:

```bash
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
```

#### Análisis:

* **Variables como contenedores:** Se utilizaron nombres descriptivos (miles, kilometers) para almacenar valores numéricos.

* **Función round():** Se implementó para limitar la salida a 2 decimales, mejorando la legibilidad del resultado final.

### Laboratorio: Operadores y expresiones

+ Codigo:

```bash
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
```

### Ejemplos con (1, 0, -1)
<img width="1395" height="331" alt="Captura de pantalla 2026-04-21 223446" src="https://github.com/user-attachments/assets/8a7b350c-cb1a-436d-885c-3d0cffc8f33c" />

#### Lógica Aplicada:
Para resolver el polinomio, se respetó la jerarquía de operadores:

1. Exponenciación (``**``): Se eleva x a las potencias indicadas antes de multiplicar.

2. Multiplicación (``*``): Se aplican los coeficientes (3, -2, 3).

3. Suma/Resta: Se ejecutan al final de la expresión.

### Laboratorio: Ejercicios de Algoritmos de Gameplay
En este laboratorio final, desarrollé un sistema interactivo que permite al usuario elegir entre 16 cálculos diferentes basados en mecánicas de videojuegos.

+ Codigo:

```bash
# LAB - Ejercicios de Algoritmos 🎮

# Este programa usa un menú interactivo que se repite indefinidamente
# hasta que el usuario elija la opción 17 (Salir)

while True:  # Bucle infinito para mostrar el menú siempre
    print("\n===== MENU DE EJERCICIOS =====")
    print("1. Puntaje total jugador")
    print("2. Tiempo total en segundos")
    print("3. Daño total")
    print("4. Experiencia total")
    print("5. Porcentaje de vida")
    print("6. Oro total")
    print("7. Velocidad promedio")
    print("8. Costo total mejoras")
    print("9. Tiempo restante misión")
    print("10. Nivel promedio equipo")
    print("11. Daño crítico")
    print("12. Tiempo en horas y minutos")
    print("13. Porcentaje misiones completadas")
    print("14. Costo total tienda")
    print("15. Tiempo promedio partidas")
    print("16. Porcentaje enemigos derrotados")
    print("17. Salir ❌")

    # Se pide al usuario elegir una opción
    opcion = int(input("Elige una opción: "))

    # ================= OPCIÓN 1 =================
    if opcion == 1:
        # Se piden los puntos de 3 niveles
        n1 = int(input("Nivel 1: "))
        n2 = int(input("Nivel 2: "))
        n3 = int(input("Nivel 3: "))
        # Se suman todos los valores
        print("Total:", n1 + n2 + n3)

    # ================= OPCIÓN 2 =================
    elif opcion == 2:
        # Se ingresan horas, minutos y segundos
        h = int(input("Horas: "))
        m = int(input("Minutos: "))
        s = int(input("Segundos: "))
        # Conversión total a segundos
        print("Total en segundos:", h*3600 + m*60 + s)

    # ================= OPCIÓN 3 =================
    elif opcion == 3:
        # Daño de 3 ataques
        a1 = int(input("Ataque 1: "))
        a2 = int(input("Ataque 2: "))
        a3 = int(input("Ataque 3: "))
        print("Daño total:", a1 + a2 + a3)

    # ================= OPCIÓN 4 =================
    elif opcion == 4:
        # Experiencia de 3 misiones
        e1 = int(input("Misión 1: "))
        e2 = int(input("Misión 2: "))
        e3 = int(input("Misión 3: "))
        print("Experiencia total:", e1 + e2 + e3)

    # ================= OPCIÓN 5 =================
    elif opcion == 5:
        # Vida máxima y actual
        max_vida = float(input("Vida máxima: "))
        actual = float(input("Vida actual: "))
        # Fórmula de porcentaje
        print("Porcentaje:", (actual / max_vida) * 100, "%")

    # ================= OPCIÓN 6 =================
    elif opcion == 6:
        # Oro recolectado en 3 misiones
        o1 = int(input("Misión 1: "))
        o2 = int(input("Misión 2: "))
        o3 = int(input("Misión 3: "))
        print("Oro total:", o1 + o2 + o3)

    # ================= OPCIÓN 7 =================
    elif opcion == 7:
        # Velocidad = distancia / tiempo
        d = float(input("Distancia: "))
        t = float(input("Tiempo: "))
        print("Velocidad promedio:", d / t)

    # ================= OPCIÓN 8 =================
    elif opcion == 8:
        # Costos de mejoras
        c1 = float(input("Mejora 1: "))
        c2 = float(input("Mejora 2: "))
        c3 = float(input("Mejora 3: "))
        print("Costo total:", c1 + c2 + c3)

    # ================= OPCIÓN 9 =================
    elif opcion == 9:
        # Tiempo restante = total - transcurrido
        total = int(input("Tiempo total: "))
        trans = int(input("Tiempo transcurrido: "))
        print("Restante:", total - trans)

    # ================= OPCIÓN 10 =================
    elif opcion == 10:
        # Promedio de niveles
        n1 = int(input("Jugador 1: "))
        n2 = int(input("Jugador 2: "))
        n3 = int(input("Jugador 3: "))
        print("Promedio:", (n1 + n2 + n3) / 3)

    # ================= OPCIÓN 11 =================
    elif opcion == 11:
        # Daño crítico = daño base * multiplicador
        base = float(input("Daño base: "))
        multi = float(input("Multiplicador: "))
        print("Daño crítico:", base * multi)

    # ================= OPCIÓN 12 =================
    elif opcion == 12:
        # Convertir minutos a horas y minutos
        minutos = int(input("Minutos: "))
        print("Horas:", minutos // 60, "Minutos:", minutos % 60)

    # ================= OPCIÓN 13 =================
    elif opcion == 13:
        # Porcentaje de misiones completadas
        total = int(input("Total misiones: "))
        comp = int(input("Completadas: "))
        print("Porcentaje:", (comp / total) * 100, "%")

    # ================= OPCIÓN 14 =================
    elif opcion == 14:
        # Suma de objetos comprados
        o1 = float(input("Objeto 1: "))
        o2 = float(input("Objeto 2: "))
        o3 = float(input("Objeto 3: "))
        print("Total:", o1 + o2 + o3)

    # ================= OPCIÓN 15 =================
    elif opcion == 15:
        # Promedio de tiempo de partidas
        t1 = float(input("Partida 1: "))
        t2 = float(input("Partida 2: "))
        t3 = float(input("Partida 3: "))
        print("Promedio:", (t1 + t2 + t3) / 3)

    # ================= OPCIÓN 16 =================
    elif opcion == 16:
        # Porcentaje de enemigos derrotados
        total = int(input("Total enemigos: "))
        der = int(input("Derrotados: "))
        print("Porcentaje:", (der / total) * 100, "%")

    # ================= OPCIÓN 17 =================
    elif opcion == 17:
        # Finaliza el programa
        print("Saliendo... 🚪")
        break  # Rompe el bucle while y termina

    # ================= OPCIÓN INVÁLIDA =================
    else:
        # Si el usuario escribe algo fuera del rango
        print("Opción inválida 💀")
```

### Análisis y Conclusiones de la Sección 4:
+ **Entrada de Datos (``input``):** Implementé la captura de datos desde el teclado, asegurando la conversión de tipos con int() y float() según la necesidad del cálculo (ej. puntos vs. porcentajes).

+ **Control de Flujo:** El uso de un bucle while y condicionales if-elif-else permite que el programa sea resiliente y funcional, gestionando incluso opciones inválidas ingresadas por el usuario.

+ **División Entera y Módulo:** En el ejercicio de conversión de tiempo (Opción 12), apliqué // para obtener las horas enteras y % para obtener los minutos sobrantes, demostrando la aplicación práctica de los operadores de la Sección 3.

+ **Nomenclatura:** Se mantuvo un esquema de nombres de variables conciso y funcional para facilitar la rapidez del desarrollo de los 16 algoritmos.
