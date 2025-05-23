repetir = True
while repetir:
    try:
        anio = int(input("Ingresa un año, ejemplo 2025: "))
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            print(f"{anio} es un año bisiesto.\n")
        else:
            print(f"{anio} no es un año bisiesto.\n")  
    except ValueError:
        print("Por favor, ingresa un número válido para el año.")
    
    match input("Ingresa 's' si quieres ingresar otra fecha, si no ingres 'n': "):
        case 's':
            repetir=True
        case _:
            repetir=False
            
