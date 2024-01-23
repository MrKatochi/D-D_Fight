import random

def tirar_dado(tipo_dado):
    if tipo_dado == "D6":
        return random.randint(1, 6)
    elif tipo_dado == "D20":
        return random.randint(1, 20)

def turno_jugador(vida_jugador, vida_jefe, umbral_jefe):
    print("\n--- ¡Turno del jugador! ---")

    accion = input("¿Qué deseas hacer? (atacar/curar): ").lower()

    if accion == "atacar":
        ataque_jugador = tirar_dado("D20")

        if ataque_jugador == 1:
            print("¡Has sacado un 1! Te has herido a ti mismo.")
            vida_jugador -= 1
        elif ataque_jugador > umbral_jefe:
            danio = ataque_jugador
            print(f"Has infligido {danio} de daño al jefe.")
            vida_jefe -= danio
        else:
            print("Has fallado tu ataque.")
    elif accion == "curar":
        curacion_d6 = tirar_dado("D6")
        if curacion_d6 != 1:
            curacion_d20 = tirar_dado("D20")
            vida_jugador += curacion_d20
            vida_jugador = min(vida_jugador, 100)  # No superar el máximo de vida
            print(f"Te has curado {curacion_d20} puntos de vida.")
        else:
            print("Has intentado curarte, pero no has tenido éxito.")
    else:
        print("Acción no válida. Se considerará como un turno de ataque.")

    return vida_jugador, vida_jefe

def turno_jefe(vida_jugador, vida_jefe, umbral_jefe):
    print("\n--- ¡Turno del jefe! ---")
    ataque_jefe = tirar_dado("D20")

    if ataque_jefe > umbral_jefe:
        danio = ataque_jefe
        print(f"El jefe te ha infligido {danio} de daño.")
        vida_jugador -= danio
    else:
        print("El jefe ha fallado su ataque.")

    return vida_jugador, vida_jefe

def estado_juego(vida_jugador, vida_jefe):
    print(f"Vida del jugador: {vida_jugador}")
    print(f"Vida del jefe: {vida_jefe}")

def jugar():
    print("¡Comienza el combate!")
    vida_jugador = 100
    vida_jefe = 100
    umbral_jefe = 13

    turno = 0

    while vida_jugador > 0 and vida_jefe > 0:
        turno += 1
        print("\n***** Comienzo de Turno Número", turno, "*****")

        vida_jugador, vida_jefe = turno_jugador(vida_jugador, vida_jefe, umbral_jefe)
        estado_juego(vida_jugador, vida_jefe)

        if vida_jefe <= 0:
            print("¡Has derrotado al jefe! ¡Felicidades!")
            break

        vida_jugador, vida_jefe = turno_jefe(vida_jugador, vida_jefe, umbral_jefe)
        estado_juego(vida_jugador, vida_jefe)

        if vida_jugador <= 0:
            print("¡El jefe te ha derrotado! ¡Mejor suerte la próxima vez!")
            break

# Iniciar el juego
jugar()
