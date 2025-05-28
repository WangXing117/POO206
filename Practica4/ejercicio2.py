# 2. Escribir un programa que pida al usuario un número entero positivo y muestre
# por pantalla la cuenta atrás desde ese número hasta cero separados por comas
repetir = True
while repetir:
    try:
        numero = int(input("Ingresa un número entero positivo: "))
        if numero <=0:
            print("EL número debe de ser entero positivo")
        else:
            cuenta = [cuentaAtras for cuentaAtras in range(numero, -1, -1)]
            print(", ".join(cuenta))
            
    except ValueError:
        print("Ingrese un número entero por favor \n")
        repetir=False
         
    match input("Ingresa 's' si quieres ingresar otro número, si no ingresa 'n': "):
        case 's':
            repetir=True
        case _:
            repetir=False