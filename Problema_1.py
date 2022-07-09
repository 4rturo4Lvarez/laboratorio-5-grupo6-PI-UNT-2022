#==============================================================================
# Dado un conjunto A que contiene N valores, positivos, negativos o nulos,
# desarrolle un programa en Python que determine e imprima:
# 1) La sumatoria de los valores negativos no nulos de A
# 2) El producto de los valores positivos no nulos
# 3) Porcentaje de valores de A nulos.
#==============================================================================

Cant_num, Cant_nulos, Sum_negat, Num, Prod_posit = 0, 0, 0, 0, 1

Cant_num = int(input("Ingrese la cantidad de números del conjunto A: "))

for i in range (1, Cant_num + 1):
    print("Ingrese el número ", i, ": "); Num = int(input("----> "))
    
    while Num < 0:
        Sum_negat = Num + Sum_negat
        break
    while Num > 0:
        Prod_posit = Num * Prod_posit
        break
    while Num == 0:
        Cant_nulos = Cant_nulos + 1
        break

print("1) La sumatoria de los valores negativos no nulos de A es: ", Sum_negat)
print("2) El producto de los valores positivos no nulos es: ", Prod_posit)
print("3) Porcentaje de valores de A nulos es: ", int(Cant_nulos/Cant_num*100), "%")