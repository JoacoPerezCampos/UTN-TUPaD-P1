#Programacion I
#Trabajo Práctico 1: Estructuras Secuenciales

#Ejercicio 1
print("Hola Mundo!")

#Ejercicio 2
print("Hola!")
nombre = input("Por favor, escribe tu nombre: ")

print(f"Hola {nombre}!")

#Ejercicio 3
print("Hola!")
nombre = input("Por favor, ingresa tu nombre..")
apellido = input("ahora ingresa tu apellido..")
edad = input("ingresa tu edad..")
pais = input("ingresa en qué país vives..")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {pais}.")

#Ejercicio 4
radio = float(input("Por favor ingrese el radio del circulo: "))
pi = 3.14159
area = pi * radio * radio
new_area = round(area, 2)
perimetro = 2 * pi * radio
new_perimetro = round(perimetro, 2)

print(f"El área del círculo es: {new_area}; y su circunferencia o perímetro es: {new_perimetro} .")

#Ejercicio 5
print("Hola!")
numero = input("Ingrese el número de segundos que desea convertir a horas: ")
segundos = int(numero)
horas = segundos / 3600
print (f"{segundos} segundos son {horas} horas")

#Ejercicio 6
print("Hola!")
numero = int(input("Ingresa un número entero: "))
print (f"{numero} x 1 = {numero * 1}")
print (f"{numero} x 2 = {numero * 2}")
print (f"{numero} x 3 = {numero * 3}")
print (f"{numero} x 4 = {numero * 4}")
print (f"{numero} x 5 = {numero * 5}")
print (f"{numero} x 6 = {numero * 6}")
print (f"{numero} x 7 = {numero * 7}")
print (f"{numero} x 8 = {numero * 8}")
print (f"{numero} x 9 = {numero * 9}")
print (f"{numero} x 10 = {numero * 10}")

#Ejercicio 7
print("Hola!")
numero1 = int(input("Ingresa un número entero, distinto a 0: "))
numero2 = int(input("Ingresa otro número entero, distinto a 0: "))
print(f"La suma de {numero1} y {numero2} es igual a {numero1 + numero2}")
print(f"La resta entre {numero1} y {numero2} es igual a {numero1 - numero2}")
print(f"El producto entre {numero1} y {numero2} es igual a {numero1 * numero2}") 
print(f"La división entre {numero1} y {numero2} es igual a {numero1/numero2}")

#Ejercicio 8
print("Hola!")
altura = float(input("Ingrese su altura (en metros): "))
peso = float(input("Ingrese su peso (en kilogramos): "))
imc = peso / altura**2
new_imc = round(imc, 2)

print(f"Su índice de masa corporal es: {new_imc}")

#Ejercicio 9
print("Hola!")
celsius = float(input("Ingrese una temperatura en grados Celsius para su conversión a grados Fahrenheit: "))
fahrenheit = 1.8*celsius + 32
print(f"La temperatura {celsius}°C, convertida a grados Fahrenheit es {fahrenheit}°F")

#Ejercicio 10
print("Hola!")
print("Ingrese 3 números para calcular su promedio: ")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
promedio = float((num1 + num2 + num3)/3)

print(f"El promedio es: {round(promedio,2)}")