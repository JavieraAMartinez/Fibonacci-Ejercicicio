def fibonacciR(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacciR(n-1) + fibonacciR(n-2)

try:
    num = int(input("Dame el número de la serie: "))
    print("Los primeros", num, "números de la serie de Fibonacci son:")
    for i in range(num):
        print(fibonacciR(i))
except ValueError:
    print("Error: Por favor, ingrese un número entero válido para el número de la serie.")

