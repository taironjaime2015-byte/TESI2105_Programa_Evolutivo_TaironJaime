# programa_personal.py - v4.0 - TESI2105_Laboratorio_5

PUNTOS_POR_SEGUNDO = 1

def ejecutar_ejercicios_lab5():
    """Ejecuta los ejercicios solicitados en el Laboratorio 5."""
    print("\n--- INICIO DEMOSTRACIÓN LABORATORIO 5 ---")
    
    # 2. ARREGLO UNIDIMENSIONAL
    niveles_dificultad = ["Facil", "Normal", "Dificil"]
    print(f"2. Arreglo Unidimensional: {niveles_dificultad}")
    # Modificación solicitada
    niveles_dificultad[0] = "Principiante"
    print("   Recorrido del arreglo (modificado):")
    for nivel in niveles_dificultad:
        print(f"   - {nivel}")

    # 3. ARREGLO MULTIDIMENSIONAL
    inventario = [
        ["Poción", "Consumible", 5],
        ["Espada", "Arma", 1]
    ]
    print("\n3. Arreglo Multidimensional (Inventario):")
    for fila in inventario:
        print(f"   Ítem: {fila[0]} | Tipo: {fila[1]} | Cantidad: {fila[2]}")

    # 4. CADENAS DE CARACTERES
    mi_cadena = "Tyrone, my hot cup"
    print(f"\n4. Cadenas de Caracteres (Texto: '{mi_cadena}'):")
    print(f"   Longitud: {len(mi_cadena)}")
    print(f"   Acceso al primer carácter (índice 0): {mi_cadena[0]}")
    print(f"   Búsqueda de 'y': {'y' in mi_cadena}")
    print(f"   Transformación a MAYÚSCULAS: {mi_cadena.upper()}")
    print("--- FIN DEMOSTRACIÓN LABORATORIO 5 ---\n")

def validar_tiempo():
    while True:
        try:
            segundos = int(input("Introduce los segundos jugados: "))
            if segundos < 1:
                print("Error: El número debe ser mayor a 0.")
            else:
                return segundos
        except ValueError:
            print("Error: Debes ingresar un número entero válido.")

def calcular_puntos(segundos, clase, multiplicador, dificultad):
    """Calcula puntos basados en clase, multiplicador y dificultad."""
    # Factor según dificultad elegida
    factores = {"Facil": 0.5, "Normal": 1.0, "Dificil": 1.5, "Principiante": 0.5}
    base_clase = 2 if clase.lower() == "mago" else 1
    
    factor_dif = factores.get(dificultad, 1.0)
    total = segundos * PUNTOS_POR_SEGUNDO * base_clase * multiplicador * factor_dif
    return int(max(0, total))

def mostrar_tienda(dinero_actual):
    costo = 50
    print(f"\n--- TIENDA (Dinero: ${dinero_actual}) ---")
    opcion = input("¿Comprar multiplicador x2 por $50? (s/n): ").lower()
    if opcion == "s":
        if dinero_actual >= costo:
            print("¡Compra exitosa! Multiplicador activo.")
            return dinero_actual - costo, 2
        else:
            print("Fondos insuficientes.")
    return dinero_actual, 1

def main():
    # 1. Ejecutar la demo del Laboratorio 5 primero
    ejecutar_ejercicios_lab5()
    
    # 2. Selección de dificultad
    niveles = ["Facil", "Normal", "Dificil"]
    print("--- Configuración de Dificultad ---")
    for i, nivel in enumerate(niveles):
        print(f"{i+1}. {nivel}")
    
    dificultad_elegida = ""
    while True:
        try:
            sel = int(input("Selecciona un número de dificultad (1-3): ")) - 1
            if 0 <= sel < len(niveles):
                dificultad_elegida = niveles[sel]
                break
            else: print("Error: Número fuera de rango.")
        except ValueError: print("Error: Por favor ingresa un número.")

    # 3. Iniciar Juego
    print(f"\n¡Has elegido dificultad: {dificultad_elegida}!")
    nombre_jugador = input("Introduce tu nombre de jugador: ")
    clase_personaje = input("Introduce tu clase (Guerrero/Mago): ")
    
    dinero_total = 0
    multiplicador_activo = 1
    
    while True:
        print(f"\n[Sesión] {nombre_jugador} | Dif: {dificultad_elegida} | $:{dinero_total} | Mult: x{multiplicador_activo}")
        print("1. Jugar | 2. Tienda | 3. Salir")
        eleccion = input("Selecciona una opción: ")
        
        if eleccion == "1":
            segundos = validar_tiempo()
            ganancia = calcular_puntos(segundos, clase_personaje, multiplicador_activo, dificultad_elegida)
            dinero_total += ganancia
            print(f"¡Ganaste ${ganancia} puntos!")
        elif eleccion == "2":
            dinero_total, multiplicador_activo = mostrar_tienda(dinero_total)
        elif eleccion == "3":
            print(f"¡Gracias por jugar, {nombre_jugador}!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
