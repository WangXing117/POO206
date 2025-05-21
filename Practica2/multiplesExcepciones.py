try:
    numero = int(input("Ingresa un número entero: "))
    resultado = 10 / numero
#Se puede hacer que except maneje mas de una excepción
#colocandolas entre parentesis y dividiendolas con una coma
except (ValueError, ZeroDivisionError) as e:
    print("Ocurrió el error: ",e)
