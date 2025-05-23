repetir = True
while repetir:
    cadena = input("Ingresa una cadena de texto: ").replace(" ", "").replace(",","").replace(".","").replace("-","").lower()
    if cadena.isalpha()!=True:
        print("Solo palabras")
    elif cadena == "":
        print("La cadena esta vacia")
    else:
        if cadena == cadena[::-1]:
            print("La cadena es palíndroma.\n")
        else:
            print("La cadena no es palíndroma.\n")
    
    match input("Ingresa 's' si quieres ingresar otra fecha, si no ingresa 'n': "):
        case 's':
            repetir=True
        case _:
            repetir=False