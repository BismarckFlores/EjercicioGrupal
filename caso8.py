""" Caso 8: Registro de consumo eléctrico por edificio en la UAM
Desarrolle un programa que permita registrar el consumo eléctrico de cinco edificios del campus
UAM (como aulas, biblioteca, administración, laboratorios y cafetería) durante tres turnos del
día (mañana, tarde y noche), por una semana. El programa debe mostrar el consumo por edificio
y el total general semanal """

edificios = ["Aulas", "Biblioteca", "Administración", "Laboratorios", "Cafetería"]
turnos = ["Matutino", "Tarde", "Noche"]
dias = 7

# Inicializar acumuladores
consumo_edificio = [0] * len(edificios)
consumo_total = 0

for i in range(len(edificios)):
    print(f"\n{'*' * 50}\nRegistro para edificio: {edificios[i]}")
    consumo_semanal_edificio = 0
    
    
    
    
    # Registro del consumo eléctrico por día
    for dia in range(dias):
        print(f"\n{'*' * 50}\nDía {dia + 1}")
        
        # Registro del consumo por turno
        for turno in range(len(turnos)):
            while True:
                try:
                    consumo = float(input(f"Ingrese el consumo eléctrico en {turnos[turno]}: "))
                    if consumo < 0:
                        print("El consumo no puede ser negativo, inténtelo de nuevo.")
                    else:
                        break
                except ValueError:
                    print("Ingrese un número válido.")

            consumo_semanal_edificio += consumo

    # Guardar el consumo semanal por edificio
    consumo_edificio[i] = consumo_semanal_edificio
    consumo_total += consumo_semanal_edificio

# Resultados
print("\nRESUMEN SEMANAL DE CONSUMO ELÉCTRICO")
print("-" * 50)
for i in range(len(edificios)):
    print(f"Edificio {edificios[i]}: {consumo_edificio[i]:.2f} W")
print(f"\nTOTAL GENERAL SEMANAL: {consumo_total:.2f} W")
