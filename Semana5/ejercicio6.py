"""
Ejercicio 6:
Una tienda registra sus ventas diarias en una lista de números. Cada número representa el monto de ventas de un día.
Se solicita calcular el total de ventas acumuladas.

Debe implementar dos funciones:
1. Una usando iteración (for o while)
2. Una usando recursividad
"""
ventas = [1000, 2500, 1800, 3200]
def total_ventas_ciclo(ventas):
    """
    Retorna el total de ventas usando ciclos.
    """
    suma = 0
    for i in ventas:
        suma += i
    print(suma)

def total_ventas_recursivo(ventas):
    """
    Retorna el total de ventas usando recursividad.
    """
    if len(ventas) == 0: return 0
    else: return ventas[0] + total_ventas_recursivo(ventas[1:])