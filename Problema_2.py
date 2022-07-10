#======================================================================================================
#Dado un conjunto de pares de valores X1 y X2, donde ambos son valores positivos
#no nulos, desarrolle un programa en Python que determine e imprima:
# 1) El promedio de X1 y X2
# 2) La media geométrica de X1 y X2, sabiendo que la media geométrica se calcula como (X1*X2)**(1/2)
# 3) Porcentaje de veces que el promedio es menor que la media geométrica
#======================================================================================================
import numpy as np

Pares_conj = int(input("Ingrese la cantidad de pares de valores X1 y X2 que se evaluarán: "))

array_a = np.zeros(2*Pares_conj)

v = array_a.reshape(Pares_conj,2)

for i in range(Pares_conj):

    print(f"A continuación ingrese los valores del par {i+1}:")

    for j in range(2):
        print(f"El valor de X{j+1}:"); v[i,j] = int(input("----> "))
                
med_arit = (v[:,0] + v[:,1])/2

med_geo = (v[:,0] * v[:,1])**(1/2)

array_b = np.zeros(3*Pares_conj)

u = array_b.reshape(Pares_conj,4)