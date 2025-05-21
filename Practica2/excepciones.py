try:
    numero = int(input("Introduce un número :) "))
    resultado = 10/numero

    print("Resultado:", resultado)

except ValueError:
    print("Error: Se ingreso algo que no es un número entero.")
except ZeroDivisionError:
    print("Error: Estas intentando dividir entre 0")