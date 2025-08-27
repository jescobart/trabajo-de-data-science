#Lista de Estudiantes 
Estudiantes = [
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

