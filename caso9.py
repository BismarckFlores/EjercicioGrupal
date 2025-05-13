"""Caso 9: Evaluación del acceso a internet en hogares de estudiantes
Implemente un programa que simule una encuesta realizada a estudiantes de la UAM para
conocer su acceso a internet en casa. Se trabajará con tres carreras, cada una con tres grupos,
y se entrevistará a cinco estudiantes por grupo. Se debe registrar si el estudiante tiene acceso
estable, intermitente o no tiene internet. Al final, mostrar un conteo de cada tipo de acceso por
carrera y el total general."""

total_estable_general = 0
total_interm_general = 0
total_no_general = 0

carreras = ["Administración", "Ingenieria", "Medicina"]

for carrera in carreras:
    print(f"\nCarrera: {carrera}")

    estable_carrera = 0
    interm_carrera = 0
    no_carrera = 0

    for grupo in range(1, 4):
        print(f"\nGrupo #{grupo}")

        for estudiante in range(1, 6):
            print(f"\nEstudiante #{estudiante}")
            while True:
                print("1. Acceso estable")
                print("2. Acceso intermitente")
                print("3. No tiene acceso a internet")

                try:
                    opcion = int(input("Seleccione una opción: "))

                    match opcion:
                        case 1:
                            estable_carrera += 1
                            total_estable_general += 1
                            break
                        case 2:
                            interm_carrera += 1
                            total_interm_general += 1
                            break
                        case 3:
                            no_carrera += 1
                            total_no_general += 1
                            break
                        case _:
                            print("\nOpción inválida, por favor intente de nuevo.\n")
                except ValueError:
                    print("\nError. Ingrese un valor valido [1 - 3]\n")

    print(f"\nResultados de {carrera}:")
    print(f"Acceso estable: {estable_carrera}")
    print(f"Acceso intermitente: {interm_carrera}")
    print(f"No tiene internet: {no_carrera}")
    input("\nPresione enter enter para continuar...")

print("\n===== Totales Generales =====")
print(f"Acceso estable general: {total_estable_general}")
print(f"Acceso intermitente general: {total_interm_general}")
print(f"No tiene internet general: {total_no_general}")