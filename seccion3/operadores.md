# 🧮 Resolución de Ejercicios: Operadores Matemáticos

Este documento contiene la resolución manual de los ejercicios propuestos en la **Sección 3**, validando la jerarquía de operadores (PEMDAS) y el comportamiento de los tipos de datos en Python.

---

## 📋 Tabla de Resultados Rápidos

| Ejercicio | Expresión | Resultado esperado | Tipo de dato |
| :---: | :--- | :---: | :---: |
| 1 | `5 + 3 * 2` | **11** | Entero |
| 2 | `8 / 2 + 4 * 3` | **16.0** | Flotante |
| 3 | `(7 + 3) * 2 - 5` | **15** | Entero |
| 4 | `10 - 4 + 2 * 3` | **12** | Entero |
| 5 | `(10 / 2) * (3 + 2) - 4` | **21.0** | Flotante |
| 6 | `2 + 3 * (4 - 1)` | **11** | Entero |
| 7 | `5 * 2 ** 3` | **40** | Entero |
| 8 | `6 + 4 / 2 ** 2` | **7.0** | Flotante |
| 9 | `10 % 3 + 2 * 5` | **11** | Entero |
| 10 | `(8 + 2) * 3 ** 2` | **90** | Entero |
| 11 | `7 + 2 * (3 + 5) / 4` | **11.0** | Flotante |
| 12 | `2 ** 3 * 4 / 2` | **16.0** | Flotante |
| 13 | `9 - 6 + 3 ** 2` | **12** | Entero |
| 14 | `(7 - 2) * 5 + 3 ** 2` | **34** | Entero |
| 15 | `4 * 2 ** 3 / 8 + 1` | **5.0** | Flotante |

---

## 🧠 Explicación Paso a Paso (Lógica Aplicada)

A continuación, se detalla la lógica de los ejercicios más complejos para demostrar el dominio de la jerarquía:

### Ejercicio 1: `5 + 3 * 2`
1. **Multiplicación:** `3 * 2 = 6`
2. **Suma:** `5 + 6 = 11`
* **Resultado:** `11` (La multiplicación tiene prioridad sobre la suma).

### Ejercicio 2: `8 / 2 + 4 * 3`
1. **División:** `8 / 2 = 4.0`
2. **Multiplicación:** `4 * 3 = 12`
3. **Suma:** `4.0 + 12 = 16.0`
* **Resultado:** `16.0` (El uso de `/` convierte el resultado en flotante).

### Ejercicio 3: `(7 + 3) * 2 - 5`
1. **Paréntesis:** `7 + 3 = 10`
2. **Multiplicación:** `10 * 2 = 20`
3. **Resta:** `20 - 5 = 15`
* **Resultado:** `15` (El paréntesis obliga a sumar primero).

### Ejercicio 4: `10 - 4 + 2 * 3`
1. **Multiplicación:** `2 * 3 = 6`
2. **Suma/Resta:** `10 - 4 = 6` -> `6 + 6 = 12`
* **Resultado:** `12` (Se resuelve de izquierda a derecha tras la multiplicación).

### Ejercicio 5: `(10 / 2) * (3 + 2) - 4`
1. **Paréntesis 1:** `10 / 2 = 5.0`
2. **Paréntesis 2:** `3 + 2 = 5`
3. **Multiplicación:** `5.0 * 5 = 25.0`
4. **Resta:** `25.0 - 4 = 21.0`
* **Resultado:** `21.0`

### Ejercicio 6: `2 + 3 * (4 - 1)`
1. **Paréntesis:** `4 - 1 = 3`
2. **Multiplicación:** `3 * 3 = 9`
3. **Suma:** `2 + 9 = 11`
* **Resultado:** `11`

### Ejercicio 7: `5 * 2 ** 3`
1. **Exponente:** `2 ** 3 = 8`
2. **Multiplicación:** `5 * 8 = 40`
* **Resultado:** `40` (El exponente tiene mayor prioridad que la multiplicación).

### Ejercicio 8: `6 + 4 / 2 ** 2`
1. **Exponente:** `2 ** 2 = 4`
2. **División:** `4 / 4 = 1.0`
3. **Suma:** `6 + 1.0 = 7.0`
* **Resultado:** `7.0`

### Ejercicio 9: `10 % 3 + 2 * 5`
1. **Módulo:** `10 % 3 = 1` (Residuo de dividir 10 entre 3).
2. **Multiplicación:** `2 * 5 = 10`
3. **Suma:** `1 + 10 = 11`
* **Resultado:** `11`

### Ejercicio 10: `(8 + 2) * 3 ** 2`
1. **Paréntesis:** `8 + 2 = 10`
2. **Exponente:** `3 ** 2 = 9`
3. **Multiplicación:** `10 * 9 = 90`
* **Resultado:** `90`

### Ejercicio 11: `7 + 2 * (3 + 5) / 4`
1. **Paréntesis:** `3 + 5 = 8`
2. **Multiplicación:** `2 * 8 = 16`
3. **División:** `16 / 4 = 4.0`
4. **Suma:** `7 + 4.0 = 11.0`
* **Resultado:** `11.0`

### Ejercicio 12: `2 ** 3 * 4 / 2`
1. **Exponente:** `2 ** 3 = 8`
2. **Multiplicación:** `8 * 4 = 32`
3. **División:** `32 / 2 = 16.0`
* **Resultado:** `16.0`

### Ejercicio 13: `9 - 6 + 3 ** 2`
1. **Exponente:** `3 ** 2 = 9`
2. **Suma/Resta:** `9 - 6 = 3` -> `3 + 9 = 12`
* **Resultado:** `12`

### Ejercicio 14: `(7 - 2) * 5 + 3 ** 2`
1. **Paréntesis:** `7 - 2 = 5`
2. **Exponente:** `3 ** 2 = 9`
3. **Multiplicación:** `5 * 5 = 25`
4. **Suma:** `25 + 9 = 34`
* **Resultado:** `34`

### Ejercicio 15: `4 * 2 ** 3 / 8 + 1`
1. **Exponente:** `2 ** 3 = 8`
2. **Multiplicación:** `4 * 8 = 32`
3. **División:** `32 / 8 = 4.0`
4. **Suma:** `4.0 + 1 = 5.0`
* **Resultado:** `5.0`
---

## Conclusión sobre Jerarquía de Operadores
Durante este laboratorio se confirmó que Python sigue el estándar matemático **PEMDAS**:
1.  **P**aréntesis.
2.  **E**xponentes.
3.  **M**ultiplicación / **D**ivisión / **M**ódulo (misma prioridad).
4.  **A**dición / **S**ustracción.

*Nota: La presencia de un solo operador de división `/` convierte el resultado de la expresión en un número de punto flotante.*