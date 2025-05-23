repetir = True
while repetir:
    try:
        anio = int(input("Ingresa un año, ejemplo 2025: "))
        if anio<0 or anio==0:
            print("Ingresa valores positivos")
        else:
            if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
                print(f"{anio} es un año bisiesto.\n")
            else:
                print(f"{anio} no es un año bisiesto.\n")  
    except ValueError:
        print("Por favor, ingresa un número válido para el año.")
    
    match input("Ingresa 's' si quieres ingresar otra fecha, si no ingresa 'n': "):
        case 's':
            repetir=True
        case _:
            repetir=False
            
