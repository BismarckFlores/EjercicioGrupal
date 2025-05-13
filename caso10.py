"""Caso 10: Control de préstamos en la biblioteca de la UAM
Desarrolle un programa que permita registrar los préstamos de libros en la biblioteca de la UAM.
Se trabajará con cuatro categorías de libros (ingeniería, salud, derecho y literatura), cada una
con tres subcategorías. Por cada subcategoría se registrarán los préstamos de cinco días. El
sistema debe mostrar el total de préstamos por subcategoría, categoría y el total general
semanal."""

total_general = 0 # Inicialización del total general de préstamos de la semana

categorias = ["Ingeniería", "Salud", "Derecho", "Literatura"] # Lista de categorías de libros

# Bucle principal para recorrer cada categoría
for categoria in categorias:
    print(f"\nCategoría: {categoria}")
    total_categoria = 0 # Inicialización del total por categoría

    # Bucle para recorrer las 3 subcategorías de cada categoría
    for subcat in range(1, 4):
        print(f"\nSubcategoría: {subcat}")
        total_subcat = 0 # Inicialización del total por subcategoría

        # Bucle para registrar préstamos durante 5 días (lunes a viernes)
        for dia in range(1, 6):

            # Uso de match-case para mostrar el día correspondiente
            match dia:
                case 1:
                    print("\nPréstamos del Lunes")
                case 2:
                    print("\nPréstamos del Martes")
                case 3:
                    print("\nPréstamos del Miércoles")
                case 4:
                    print("\nPréstamos del Jueves")
                case 5:
                    print("\nPréstamos del Viernes")

            # Bucle para validar que el usuario ingrese un número entero positivo
            while True:
                try:
                    prestamos = int(input(f"Ingrese la cantidad de préstamos: "))
                    if prestamos >= 0:
                        total_subcat += prestamos
                        break
                    else:
                        print("\nIngrese un número positivo.\n")
                except ValueError:
                    print("\nError. Ingrese un número entero.\n")

        # Mostrar el total de préstamos por subcategoría
        print(f"\nTotal de prestamos en subcategoría #{subcat}: {total_subcat}")
        if subcat != 3:
            input("\nPresione enter enter para continuar...")
        total_categoria += total_subcat # Acumular el total de préstamos por subcategoría al total de la categoría

    # Mostrar el total de préstamos por categoría
    print(f"\nTotal de préstamos en la categoría {categoria}: {total_categoria}")
    input("\nPresione enter enter para continuar...")
    total_general += total_categoria # Acumular el total de la categoría al total general

# Mostrar el total general de préstamos de la semana
print(f"\n===== Total de préstamos de la semana: {total_general} =====")