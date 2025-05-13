#Numero de estudiantes a evaluar
estudiantes_evaluados = int(input("Ingrese los estudiantes a calificar: "))

#Seleccionador de estudiantes
for estudiante in range(1, estudiantes_evaluados + 1):
        print(f"\n--- Estudiante #{estudiante} ---")
        promedio_general = 0

#Selector de asignatura
for asignatura in range(1,4):
        print(f"\n Asignatura: {asignatura}")
        suma_notas = 0
        
        #Notas de tareas de la asignatura
        for tarea in range (1, 4):
                sum_nota = 0
                notas = float(input(f"Ingrese la nota de la tarea {tarea}: "))
                sum_nota += notas
        #Nota del examen de la asignatura
        nota_examen = float(input("Ingrese la nota de su examen: "))
        suma_notas += nota_examen
        
        #Promedio total de la asignatura
        promedio_asignatura = suma_notas / 4
        print(f"Promedio de asignatura: {promedio_asignatura:.2f}")
        promedio_general += promedio_asignatura

#Promedio total de todas las asignaturas
promedio_general /= 3
print(f"\nEl promedio general del estudiante es: {promedio_general:.2f}")
