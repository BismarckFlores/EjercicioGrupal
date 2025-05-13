#lista de las facultad y sus carreras
facultades = {"Ingeniería": ["Sistemas", "Industrial"],"Ciencias Sociales": ["Psicología", "Sociología"],"Ciencias Económicas": ["Economía", "Administración"]}
#lista de miedos de transporte validos
medios_transporte = ["bus", "motocicleta", "taxi", "bicicleta", "caminar"]
#inicializacion de conteos por facultad de los medios de transporte
conteo_facultades = {
    facultad: {medio: 0 for medio in medios_transporte}
    for facultad in facultades}
#inializacion de la encuesta
for facultad, carreras in facultades.items():
    print(f"\nFacultad de {facultad}")
    for carrera in carreras:
        print(f"  Carrera de {carrera}")
        for i in range(1, 6):  # 5 estudiantes por carrera
            while True:
                medio = input(f"    Estudiante {i}: ¿Qué medio de transporte utiliza? (bus/motocicleta/taxi/bicicleta/caminar): ").lower()
                if medio in medios_transporte:
                    conteo_facultades[facultad][medio] += 1
                    break
                else:
                    print("    Medio no válido. Intente de nuevo.")
#se muestran los recultados de la encuesta por facultad
print("\n--- Resultados por Facultad ---")
#inializacion para llevar el total general
total_general = {medio: 0 for medio in medios_transporte}
#se recorre cada falcultad y sus conteos
for facultad, conteo in conteo_facultades.items():
    print(f"\nFacultad de {facultad}:")
    for medio, cantidad in conteo.items():
        print(f"  {medio.capitalize()}: {cantidad}")
        total_general[medio] += cantidad
#muestra el total final de las encuesta
print("\n--- Total General ---")
for medio, total in total_general.items():
    print(f"{medio.capitalize()}: {total}")
    