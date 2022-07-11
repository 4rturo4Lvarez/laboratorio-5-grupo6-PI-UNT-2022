#======================================================================================================
# Dado un conjunto de pares de valores X1 y X2, donde ambos son valores positivos
# no nulos, desarrolle un programa en Python que determine e imprima:
#  1) El promedio de X1 y X2.
#  2) La media geométrica de X1 y X2, sabiendo que la media geométrica se calcula como (X1*X2)**(1/2).
#  3) Porcentaje de veces que el promedio es menor que la media geométrica.
#  4) El primer par de valores de X1 y X2 donde el promedio es igual a la media
#    geométrica.
#======================================================================================================
import numpy as np

Pares_conj = int(input("Ingrese la cantidad de pares de valores X1 y X2 que se evaluarán: "))

#Creación del array donde se almacenarán los datos usando numpy:
array_a = np.zeros(2*Pares_conj)

v = array_a.reshape(Pares_conj,2)

#Ingreso de datos:
for i in range(Pares_conj):
    print(f"A continuación ingrese los valores del par {i+1}:")

    for j in range(2):
        print(f"El valor de X{j+1}:"); v[i,j] = int(input("----> "))
                
#Cálculo de la media aritmética y geométrica:
med_arit = (v[:,0] + v[:,1])/2

med_geo = (v[:,0] * v[:,1])**(1/2)

#Código para que los datos se muestren en una tabla:
lineas = "+------------+------------+------------+------------+"
print(lineas)
print("|     X1     |     X2     |  P. Arit.  |  P. Geom.  |")
print(lineas)

for i in range(Pares_conj):   
    fila = "|{:^12.2f}|{:^12.2f}|{:^12.2f}|{:^12.2f}|".format(v[i,0], v[i,1], med_arit[i], med_geo[i])
    print(fila)
    print(lineas)

#Cálculo del porcentaje de veces que el promedio es menor que la media geométrica:
contador = 0

for i in range(Pares_conj):
    if med_arit[i] < med_geo[i]:
        contador = contador + 1

porcentaje = (contador/Pares_conj)*100

print(f"El porcentaje de veces que el promedio es menor que la media geométrica será de {porcentaje}%.")

# Uso de las funciones for y while para el item 4)

for i in range(Pares_conj):
    if med_arit[i] == med_geo[i]:
        print(f"El primer par de valores donde el promedio es igual a la media geométrica es X1 = {v[i,0]} y X2 = {v[i,1]}")
        break