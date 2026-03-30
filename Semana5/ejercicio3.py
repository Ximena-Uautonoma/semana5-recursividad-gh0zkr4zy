"""
Ejercicio 3:
Dado un número entero positivo N, calcular su factorial.

Debe implementar una versión iterativa y una recursiva.
"""

def factorial_ciclo(n):
    fact = 1
    for i in range(n):
        fact = fact * (i+1)
    print(fact)

def factorial_recursivo(n):
    if n == 1: return 1
    else: return factorial_recursivo(n-1) * n