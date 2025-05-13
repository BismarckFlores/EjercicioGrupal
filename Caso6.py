# damos el precio de cada nacatamal
precio_nacatamal = 30
# Inicializamos el total mensual vendido
total_mensual = 0
# un bucle principal para los 4 domingos
for domingo in range(1, 5):
    print(f"\nDomingo {domingo}")
    # Pedimos la cantidad de clientes de ese domingo
    num_clientes = int(input("Ingrese la cantidad de clientes: "))
    total_domingo = 0
    # Bucle para cada cliente
    for cliente in range(1, num_clientes + 1):
        cantidad = int(input(f"Cliente {cliente}, ¿cuántos nacatamales compró?: "))
        # Calculamos el total de este cliente
        total_cliente = cantidad * precio_nacatamal
        total_domingo += total_cliente
    # Mostramos total vendido ese domingo
    print(f"Total vendido el Domingo {domingo}: C$ {total_domingo}")
    total_mensual += total_domingo
# Mostramos el total vendido en el mes
print(f"\nTotal vendido en el mes: C$ {total_mensual}")
