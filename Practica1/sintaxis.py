#1 Comentarios

"""
Comentarios de mas de una linea
"""

#2 String
print("Hola soy una cadena")
print("Yo soy otra")

variable1="hola soy una cadena"
print(len(variable1)) #len da el total de caracteres incluyendo espacios
print(variable1[2:5]) #te da los caractes correspondientes del 2 al 5
print(variable1[2:])
print(variable1[:5])

#3 Variables, siempre toma el último valor asignado

x = "juan"
x = 4
x = 5.76
print(x)

#Para forzar que todo sea de un tipo
x= int(3)
y= float(3)
z=str(3)

print(x,y,z)
print(type(x))#nos dice cual es el tipo del dato
print(type(y))
print(type(z))

#3 solicitud de datos

#dato_solicitado = input("Introduce un dato: ")
#dato_solicitadoI = int(input("Introduce un numero entero: "))
#dato_solicitadoF= float(input("Introduce un número decimal: "))

#4 boolean, comparacion y logicos
print(10>9) #mayor que 
print(10<9)
print(10==9)
print(10>=9)
print(10<=9)
print(10!=9)

x=1
print(x<5 and x<10)
print(x<5 or x<10)
print(not(x<5 and x<10))