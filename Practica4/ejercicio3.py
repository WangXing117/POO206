# 3. Escribir un programa en el que se pregunte al usuario por una frase y una letra,
# y muestre por pantalla el número de veces que aparece la letra en la frase.

repetir = True
while repetir:
    
    frase = input("Introduce una frase: ")
    letra = input("Introduce una letra: ")

    if len(letra) != 1: #En caso de que introduzca más de una letra
        print("Debes introducir solo una letra.")
    else:
        cantidad = frase.count(letra)# .count cuenta el numero de veces que aparece la letra en frase
        print(f"La letra '{letra}' aparece {cantidad} veces en la frase: {frase}.")
        
    match input("Ingresa 's' si quieres ingresar otro número, si no ingresa 'n': "):
        case 's':
            repetir=True
        case _:
            repetir=False