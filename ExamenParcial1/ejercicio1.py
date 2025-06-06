# Escriba un programa que pida al usuario dos palabras, y que indique cuál de ellas es la más
# larga y por cuántas letras lo es
repetir = True
while repetir:
    palabra1 = input("Ingresa la primera palabra: ")
    palabra2= input("Ingresa la segunda palabra: ")

    try:
        contadorP1 = 0;
        contadorP2 = 0;
        
        for i in palabra1:
            if i == " ":
                raise ValueError
            
            contadorP1 = contadorP1 + 1
        for i in palabra2:
            if i == " ":
                raise ValueError
            
            contadorP2 = contadorP2 +1

        if contadorP1<contadorP2:
            print(f"La segunda palabra  '{palabra2}' es {contadorP2-contadorP1} letras más grande")
        elif contadorP1==contadorP2:
            print(f"Ambas palabras son igual de largas")
        else:
            print(f" La primera palabra '{palabra1}' es {contadorP1-contadorP2} letras más grande")
            
    except (ValueError):
        print("Debe de ser solo palabras espacios")
        
    match input("Ingresa 's' si quieres reintentar si no cualquier otra cosa: "):
        case 's':
            repetir = True
        case _:
            repetir = False