import re #la libreria re nos permite compara y manipular texto
repetir = True
while repetir:
    try:
        contrasena = input("Ingresa una contraseña: ")
        contrasena.replace(" ", "")
        
        if len(contrasena) < 10: #len es una función que me dice la longitud de la cadena
            print("Contraseña demasiado corta.\n")

        elif not any(char.isdigit() for char in contrasena):
            print("Debe contener al menos un número.\n")

        elif not re.search(r"[!@#$%^&*(),.?\":{}|<>´¿_\-+~]", contrasena): #busca dentro de contrasena coinsidencias con los carateres
            print("Debe contener al menos un carácter especial.\n")

        else:
            print("Contraseña válida.\n")
    except:
        print("Ocurrio un error")
        
    match input("Ingresa 's' si quieres ingresar otra fecha, si no ingresa 'n': "):
        case 's':
            repetir=True
        case _:
            repetir=False