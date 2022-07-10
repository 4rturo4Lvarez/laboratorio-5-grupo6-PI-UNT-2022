n = int(input("Ingrese el número de término de Tribonacci que desea conocer: "))
def tribonacci(n):
    if n <= 1:
        return n
    elif n == 2:
        return 1
    else:
        return tribonacci(n-3) + tribonacci(n-2) + tribonacci(n-1)
print("El número es: ", tribonacci(n))