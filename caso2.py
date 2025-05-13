"""Caso 2: Registro semanal de gastos de estudiantes UAM
Cree un programa que simule el control de gastos semanales de un grupo de estudiantes de
primer año de la UAM. El sistema debe procesar datos de 4 semanas, y por cada semana,
ingresar el gasto realizado cada día (7 días por semana). El programa debe calcular el total
gastado por semana y el total acumulado del mes. Utilice bucles anidados para recorrer
semanas y días"""

gastos_mes = 0

for sem in range(4):
    print(f"\nSemana #{sem + 1}")
    gastos_sem = 0
    for dia in range(7):
        match dia:
            case 0:
                print("\nGastos del Lunes")
            case 1:
                print("\nGastos del Martes")
            case 2:
                print("\nGastos del Miércoles")
            case 3:
                print("\nGastos del Jueves")
            case 4:
                print("\nGastos del Viernes")
            case 5:
                print("\nGastos del Sábado")
            case 6:
                print("\nGastos del Domingo")
        gastos_diarios = float(input("Ingrese lo que se gasto en el dia: "))
        gastos_sem += gastos_diarios
    print(f"Gastos de la semana {sem + 1}: C${gastos_sem}")
    gastos_mes += gastos_sem
print(f"Gastos del mes: C${gastos_mes}")