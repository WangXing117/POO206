# Crea un programa que solicite un número par commprendido entre 200 y 400
# y nos muestre todos los números paren en la serie entre el número y 400
#

repetir = True

while repetir:
    try:
        numeroBase = int( input("Ingresa un número entre 200 y 400:" ))
        if numeroBase <200 or numeroBase > 400:
            print(f"Error: {numeroBase} no esta entre el rango de 200 y 400")
        else:
            listaNum = [i for i in range(numeroBase,401) if i%2 == 0]
            print(listaNum)
    except (ValueError):
        print("Se tiene que ingresar un número")
    except:
        print("Ha habido un error reintente por favor")
        
    match input("Ingresa 's' si quieres reintentar si no cualquier otra cosa: "):
        case 's':
            repetir = True
        case _:
            repetir = False