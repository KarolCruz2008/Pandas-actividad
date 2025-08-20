import pandas as pd

def menu():
    print("\n", "1. Introduce el resultado de un partido")
    print("2. Muestra la tabla del grupo")
    print("3. Primero del grupo")
    print("4. Estadisticas")
    print("5. Salir")
    entrada = input("Introduce la opción a escoger: ")
    return entrada

entrada = 0
datos = pd.DataFrame({
    'Pais': ['España', 'Japon', 'Alemania', 'CostaRica'],
    'P': [0, 0, 0, 0],
    'PJ': [0, 0, 0, 0],
    'PG': [0, 0, 0, 0],
    'PE': [0, 0, 0, 0],
    'GF': [0, 0, 0, 0],
    'GC': [0, 0, 0, 0],
    'GD': [0, 0, 0, 0],
})

print("\n", datos)
entrada = 0
while entrada != "5":
    entrada = menu()

    if entrada == "5":
        print("Ha sido un honor atenderte. Saliendo del programa.....")

    if entrada == "1":
        equipo1 = input("Ingresa el equipo 1 del juego terminado: ")
        equipo2 = input("Ingresa el equipo 2 del juego terminado: ")
        resultado1 = int(input("Ingrese el marcador de goles del equipo 1: "))
        resultado2 = int(input("Ingrese el marcador de goles del equipo 2: "))

        # Actualizar partidos jugados
        datos.loc[datos['Pais'] == equipo1, 'PJ'] += 1
        datos.loc[datos['Pais'] == equipo2, 'PJ'] += 1

        # Actualizar goles
        datos.loc[datos['Pais'] == equipo1, 'GF'] += resultado1
        datos.loc[datos['Pais'] == equipo1, 'GC'] += resultado2
        datos.loc[datos['Pais'] == equipo2, 'GF'] += resultado2
        datos.loc[datos['Pais'] == equipo2, 'GC'] += resultado1

        # Actualizar diferencia de goles
        datos['GD'] = datos['GF'] - datos['GC']

        # Resultado del partido
        if resultado1 > resultado2:  # Gana equipo1
            datos.loc[datos['Pais'] == equipo1, 'P'] += 3
            datos.loc[datos['Pais'] == equipo1, 'PG'] += 1
            print("Ganador:", equipo1)

        if resultado1 < resultado2:  # Gana equipo2
            datos.loc[datos['Pais'] == equipo2, 'P'] += 3
            datos.loc[datos['Pais'] == equipo2, 'PG'] += 1
            print("Ganador:", equipo2)

        if resultado1 == resultado2:  # Empate
            datos.loc[datos['Pais'] == equipo1, 'P'] += 1
            datos.loc[datos['Pais'] == equipo2, 'P'] += 1
            datos.loc[datos['Pais'] == equipo1, 'PE'] += 1
            datos.loc[datos['Pais'] == equipo2, 'PE'] += 1
            print("Empate entre", equipo1, "y", equipo2)

        print("\n", datos)

    if entrada == "2":
        print("\nTabla del grupo:")
        print(datos.sort_values(by=["P", "GD", "GF"]))

    if entrada == "3":
        primero = datos.sort_values(by=["P", "GD", "GF"]).iloc[-1]
        print("\nEl primero del grupo es:", primero["Pais"])

    if entrada == "4":
        print("\nEstadísticas del grupo:")
        print(datos)
