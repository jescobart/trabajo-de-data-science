Estudiantes = [
    {"Nombre": "Paula", "Notas": [3.6, 4.8, 6.6]},
    {"Nombre": "Juan", "Notas": [4.0, 5.5, 3.8]},
    {"Nombre": "María", "Notas": [6.2, 2.8, 4.5]},
    {"Nombre": "Pedro", "Notas": [5.0, 3.6, 1.2]},
    {"Nombre": "Carla", "Notas": [2.5, 6.8, 4.9]},
    {"Nombre": "Andrés", "Notas": [3.1, 4.0, 6.7]},
    {"Nombre": "Valentina", "Notas": [5.9, 2.4, 3.3]},
    {"Nombre": "Matías", "Notas": [6.5, 4.2, 2.0]},
    {"Nombre": "Camila", "Notas": [1.8, 5.6, 6.4]},
    {"Nombre": "Diego", "Notas": [3.7, 4.9, 2.1]},
    {"Nombre": "Fernanda", "Notas": [6.9, 5.1, 4.0]},
    {"Nombre": "Rodrigo", "Notas": [2.2, 6.7, 3.6]},
    {"Nombre": "Isabel", "Notas": [4.3, 5.5, 2.7]},
    {"Nombre": "Tomás", "Notas": [3.9, 1.5, 6.8]},
    {"Nombre": "Constanza", "Notas": [5.4, 4.1, 2.9]},
    {"Nombre": "Felipe", "Notas": [6.0, 3.3, 5.8]},
    {"Nombre": "Josefa", "Notas": [2.1, 4.6, 6.4]},
    {"Nombre": "Sebastián", "Notas": [3.0, 6.7, 5.2]},
    {"Nombre": "Antonella", "Notas": [1.9, 4.4, 6.1]},
    {"Nombre": "Cristóbal", "Notas": [5.6, 2.3, 3.7]},
    {"Nombre": "Gabriela", "Notas": [6.8, 3.5, 4.2]},
    {"Nombre": "Ignacio", "Notas": [2.6, 5.7, 6.9]},
    {"Nombre": "Alejandra", "Notas": [3.2, 1.8, 4.7]},
    {"Nombre": "Vicente", "Notas": [5.0, 6.3, 2.2]},
    {"Nombre": "Francisca", "Notas": [4.9, 3.7, 6.1]},
    {"Nombre": "Javier", "Notas": [2.4, 4.8, 5.6]},
    {"Nombre": "Daniela", "Notas": [3.6, 6.5, 2.0]},
    {"Nombre": "Mauricio", "Notas": [6.7, 4.4, 3.3]},
    {"Nombre": "Beatriz", "Notas": [2.8, 5.9, 1.7]},
    {"Nombre": "Patricio", "Notas": [4.2, 6.6, 3.1]}
]

import statistics  # se usa esta librería para calcular medidas estadísticas como moda, promedio, mediana, etc.

def promedios_estudiantes(estudiantes):
    promedios = []
 # Revisar si la lista de estudiantes está vacía
    if not estudiantes:
        print("La lista de estudiantes está vacía.")
        return  # salir de la función

    # 1) Calcular promedios
    for est in estudiantes:
        promedio = sum(est["Notas"]) / len(est["Notas"])
        promedios.append((est["Nombre"], promedio))

    # Mejor y peor promedio
    mejor = max(promedios, key=lambda x: x[1])
    peor = min(promedios, key=lambda x: x[1])

    print(f"Mejor promedio: {mejor[0]} con {mejor[1]:.2f}")
    print(f"Peor promedio: {peor[0]} con {peor[1]:.2f}")

    #2) Estudiantes aprobados (promedio >= 4)
    aprobados = []
    for estudiante_promedio in promedios:
        if estudiante_promedio[1] >= 4.0:
            aprobados.append({"Nombre": estudiante_promedio[0], "Promedio": round(estudiante_promedio[1], 2)})

    # Imprimir aprobados
    print("\nEstudiantes aprobados:")
    for estu in aprobados:
        print(f"- {estu['Nombre']} con promedio {estu['Promedio']:.2f}")

    # 3) Calcular nota más frecuente (moda)
    todas_notas = []
    for est in estudiantes:
        todas_notas.extend(est["Notas"])  # juntamos todas las notas
    try:
        moda = statistics.mode(todas_notas)
        print(f"\nLa nota más frecuente (moda) es: {moda}")
    except statistics.StatisticsError:
        print("\nNo hay una moda única (varias notas con la misma frecuencia).")

    # 4)porcentaje de estudiantes reprobados(<4.0)
    reprobados = [est for est in promedios if est[1] < 4.0]
    porcentaje_reprobados = (len(reprobados) / len(estudiantes)) * 100

    print(f"\nPorcentaje de estudiantes reprobados: {porcentaje_reprobados:.2f}%")
    
    
    # 5) Listado de estudiantes de mayor a menor promedio
    ordenados = sorted(promedios, key=lambda x: x[1], reverse=True)  # Orden descendente por promedio
    print("\nEstudiantes ordenados de mayor a menor promedio:")
    for est in ordenados:
        print(f"- {est[0]} con promedio {est[1]:.2f}")

# Llamada a la función
promedios_estudiantes(Estudiantes)

