# 1. Escribir un programa que pida al usuario un número entero positivo mayor de 10 y
# que muestre como resultado todos los números impares desde 2 hasta ese número
# separados por comas.
repetir = True
while repetir:
    try:
        numero = int(input("Ingresa un número entero mayor que 10: "))
        if numero <=10:
            print("EL número debe de ser entero mayor a 10")
        else:
            #por medio de list comprehension se guarda en numerosImpares el numeroImpar obtenido del arreglo
            #que va de 2 hasta numero+1 solo si el residuo de numeroImpar/2 es diferente de 0
            numerosImpares = [str(numeroImpar) for numeroImpar in range(2,numero+1) if numeroImpar % 2 != 0]
            print(", ".join(numerosImpares))
            
    except ValueError:
         print("Ingrese un número entero por favor \n")
         repetir=False

    match input("Ingresa 's' si quieres ingresar otro número, si no ingresa 'n': "):
        case 's':
            repetir=True
        case _:
            repetir=False