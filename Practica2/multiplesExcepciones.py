try:
    numero = int(input("Ingresa un número entero: "))
    resultado = 10 / numero
except (ValueError, ZeroDivisionError) as e:
    print("Ocurrió el error: ",e)
