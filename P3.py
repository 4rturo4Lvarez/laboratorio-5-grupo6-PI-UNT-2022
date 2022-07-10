#===========================================================================#
#   Se tienen los nombres de los N alumnos de una escuela, además de su     #
#   promedio general. Realice un algoritmo para capturar esta información,  #
#   la cual se debe almacenar en arreglos, un vector para el nombre y otro  #
#   para el promedio, después de capturar la información se debe ordenar    #
#   con base en su promedio, de menor a mayor, los nombres deben            #
#   corresponder con los promedios. Realice un programa en Python.          #
#===========================================================================#

alumnos=int(input('Ingresar cantidad de alumnos: '))
N=[]
P=[]

#Se almacenan los datos
for n in range(alumnos):
    nombre=input(f'Ingresar nombre de alumno {n+1}: ')
    promedio=int(input(f'Ingresar promedio de {nombre}: '))
    N.append(nombre)
    P.append(promedio)

#~~~~ORDENACION POR BURBUJA~~~~
    #Bucle a reorrer
for i in range(0, alumnos-1):
    #comparaciones e intercambios
    for j in range(0, alumnos-1):
        if P[j] > P[j+1]:
            #orden del promedio de menor a mayor
            temporal = P[j]
            P[j] = P[j+1]
            P[j+1] = temporal
               
            #orden del nombre segun el promedio
            temp = N[j]
            N[j] = N[j+1]
            N[j+1] = temp

#codigo para mostrar los datos en una tabla
lineas='+-----------------------------------------------+'
print(lineas)
print('|{:^5}|{:^25}|{:^15}|'.format('N','ALUMNO','PROMEDIO'))
print(lineas)

for n in range(alumnos): 
    fila = ('|{:^5}|{:^25}|{:^15.2f}|'.format(n+1,N[n], P[n]))
    print(fila)
    print(lineas)