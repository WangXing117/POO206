def dividir(a, b):
    if b == 0:
        #Se indica que no se puede dividir entre cero
        raise ValueError("No se puede dividir entre cero.")
    return a / b

try:
    numerador = int(input("Para realizar una división\nIntroduce un numerador : "))
    denominador = int(input("Introduce el denominador : "))
    resultado = dividir(numerador, denominador)
    print("El resultado es: ",resultado)
except ValueError as e:
    #Se muestra la excepcción
    print(f"Error: {e}")
