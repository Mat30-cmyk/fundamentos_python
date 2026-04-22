# GA1-220501093-04-AA1-EV01 - Sección 4: Variables

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