#!/usr/bin/env python

"""
Imprime a tabuada do 1 ao 10.
"""

__version__ = "0.1.0"
__author__ = "Higor R."

# base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1,11))

print(numeros)


#Iterable(percorríveis)

for numero in numeros:
    print("Tabuada do: {}".format(numero))
    for multiplic in numeros:
        print(numero * multiplic)
    print("-" * 12)     