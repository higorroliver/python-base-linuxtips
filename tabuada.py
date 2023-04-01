#!/usr/bin/env python

"""
Imprime a tabuada do 1 ao 10.
"""

__version__ = "0.1.1"
__author__ = "Higor R."

# base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Iterable(percorríveis)
numeros = list(range(1,11))
print(numeros)
print()

#criando a tabuada
for numero in numeros:
    print("{:^18}".format(f"Tabuada do: {numero}"))
    for multiplic in numeros:
        resultado = numero * multiplic
        print("{:^18}".format(f"{numero} x {multiplic} = {resultado}"))
    print("#" * 18)
print("\N{party popper}"*8)