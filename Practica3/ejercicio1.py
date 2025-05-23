#1.pide al usuario un número entero y muestra por pantalla si es par o no
repetir = True

while True:
    numero = 0
    repetir = True
    try:
        numero = int(input("Ingresa un número entero: "))
    except ValueError:
         print("Ingrese un número entero por favor \n")
         repetir=False
         
    if repetir==True:
        if numero % 2 == 0:
            print(f"El número {numero} es par")
        else:
            print(f"El número {numero} es impar")
            
    opcion = input("Ingres 's' si quires ingresar otro número y 'n' si ya no: ")
    if opcion!="s":
        break
        


