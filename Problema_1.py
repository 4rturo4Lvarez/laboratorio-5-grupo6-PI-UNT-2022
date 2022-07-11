#==============================================================================
# Dado un conjunto A que contiene N valores, positivos, negativos o nulos,
# desarrolle un programa en Python que determine e imprima:
#  1) La sumatoria de los valores negativos no nulos de A
#  2) El producto de los valores positivos no nulos
#  3) Porcentaje de valores de A nulos.
#==============================================================================

Cant_nulos, Sum_negat, Prod_posit = 0, 0, 1

Cant_nums = int(input("Ingrese la cantidad de números del conjunto A: "))

for i in range (Cant_nums):
    print(f"Ingrese el número {int(i + 1)}: "); Num = int(input("----> "))
    
    if Num < 0:
        Sum_negat = Num + Sum_negat
    
    elif Num > 0:
        Prod_posit = Num * Prod_posit
    
    else:
        Cant_nulos = Cant_nulos + 1

print("\n")

print(f"1) La sumatoria de los valores negativos no nulos de A es {Sum_negat}.")
print(f"2) El producto de los valores positivos no nulos es {Prod_posit}.")
print(f"3) Porcentaje de valores de A nulos es: {int(Cant_nulos/Cant_nums*100)}%.")