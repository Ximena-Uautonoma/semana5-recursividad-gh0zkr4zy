"""
Ejercicio 5:
Calcular la potencia de una base elevada a un exponente entero positivo.
"""

def potencia_ciclo(base, exponente):
    potencia = 1
    for i in range(exponente):
        potencia = potencia * base
    print(potencia)


def potencia_recursiva(base, exponente):
    if exponente == 1: return base
    else: return potencia_recursiva(base, exponente - 1) * base