from datetime import datetime

try:
    año_nacimiento = int(input("Ingresa tu año de nacimiento (YYYY): "))
    año_actual = datetime.now().year
    edad = año_actual - año_nacimiento
    print(f"Tienes aproximadamente {edad} años.")
except ValueError:
    print("Por favor, ingresa un año válido (solo números).")
finally:
    print("Gracias por usar la calculadora de edad.")
