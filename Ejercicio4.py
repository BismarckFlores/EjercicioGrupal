#Carreras definidas
carreras = ["Sistemas", "Marketing", "Derecho"]

#Variable del total general
total_general = 0

#Recorrer carreras para sacar los valores
for carrera in carreras:
    print(f"\nCarrera: {carrera}")
    total_carrera = 0
    #Años de duración de cada carrera
    for año in range (1,4):
        print(f"Año: {año}")
        #Participaciones de estudiantes en cada sección por año de carrera
        for seccion in range(1,3):
            participantes = int(input(f"Ingrese el número de estudiantes que partcipan en sección {seccion}: "))
        total_carrera += participantes
    #Participación total en toda la carrera
    print(f"\n Total de participantes en {carrera}\n")
    #Acumulación de particpaciones entre las 3 carreras
    total_general += total_carrera
    
#Mostrar el total de participaciones en todas las carreras
print(f"\nTotal general de estudiantes participantes: {total_general}")