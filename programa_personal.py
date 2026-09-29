# programa_personal.py - v3.0

# Constante global
PUNTOS_POR_SEGUNDO = 1

def validar_tiempo():
    """Función para validar el tiempo. Si es menor a 1, muestra error y repite."""
    while True:
        try:
            segundos = int(input("Introduce los segundos jugados: "))
            # Verificación explícita como pediste
            if segundos < 1:
                print("Error: no se puede poner un número menor que 1.")
            else:
                return segundos
        except ValueError:
            print("Error: Debes ingresar un número entero válido.")

def calcular_puntos(segundos, clase, multiplicador):
    """Función con parámetros y return para calcular los puntos."""
    if clase.lower() == "mago":
        base_clase = 2
    else:
        base_clase = 1
    
    total = segundos * PUNTOS_POR_SEGUNDO * base_clase * multiplicador
    
    # Uso de función built-in max():
    # Asegura que si por algún error el total resulta negativo, devuelva 0.
    return max(0, total)

def mostrar_tienda(dinero_actual):
    """Acción sin return explícito: Muestra la tienda y gestiona la compra."""
    costo = 50
    print(f"\n--- TIENDA ---")
    print(f"Dinero disponible: ${dinero_actual}")
    print(f"Multiplicador x2 cuesta: ${costo}")
    
    opcion = input("¿Comprar multiplicador? (s/n): ").lower()
    
    if opcion == "s":
        if dinero_actual >= costo:
            print("¡Compra exitosa! Multiplicador activo.")
            return dinero_actual - costo, 2 # Retorna dinero restante y nuevo multiplicador
        else:
            print("Fondos insuficientes.")
            
    return dinero_actual, 1 # Si no compra, devuelve lo mismo

def main():
    print("--- Mini Juego: Acumulador de Puntos (v3.0) ---")
    
    nombre_jugador = input("Introduce tu nombre de jugador: ")
    clase_personaje = input("Introduce tu clase (Guerrero/Mago): ")
    
    dinero_total = 0
    multiplicador_activo = 1
    
    while True:
        print(f"\n[Sesión] Jugador: {nombre_jugador} | Clase: {clase_personaje}")
        print(f"Dinero actual: ${dinero_total} | Multiplicador: x{multiplicador_activo}")
        
        print("\nOpciones: 1. Jugar | 2. Tienda | 3. Salir")
        
        eleccion = input("Selecciona una opción: ")
        
        if eleccion == "1":
            segundos = validar_tiempo()
            ganancia = calcular_puntos(segundos, clase_personaje, multiplicador_activo)
            dinero_total += ganancia
            print(f"¡Ganaste ${ganancia} puntos!")
            
        elif eleccion == "2":
            dinero_total, multiplicador_activo = mostrar_tienda(dinero_total)
            
        elif eleccion == "3":
            print(f"\nResumen final: {nombre_jugador}, acumulaste ${dinero_total}.")
            print("¡Gracias por jugar!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
