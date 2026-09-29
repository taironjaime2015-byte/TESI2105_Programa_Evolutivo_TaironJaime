# programa_personal.py - v2.0
PUNTOS_POR_SEGUNDO = 1

print("--- Mini Juego: Acumulador de Puntos (v2.0) ---")

nombre_jugador = input("Introduce tu nombre de jugador: ")
clase_personaje = input("Introduce tu clase (Guerrero/Mago): ")

while True:
    segundos_jugados = int(input("Introduce los segundos jugados: "))
    if segundos_jugados >= 0:
        break
    print("Error: el tiempo no puede ser negativo. Intenta otra vez.")

if clase_personaje.lower() == "mago":
    puntos_totales = segundos_jugados * PUNTOS_POR_SEGUNDO * 2
else:
    puntos_totales = segundos_jugados * PUNTOS_POR_SEGUNDO

print("\n--- Resumen de la Sesión ---")
print(f"Jugador: {nombre_jugador}")
print(f"Clase: {clase_personaje}")
print(f"Segundos jugados: {segundos_jugados}")
print(f"Puntos obtenidos: {puntos_totales}")

print("¡Gracias por jugar!")
