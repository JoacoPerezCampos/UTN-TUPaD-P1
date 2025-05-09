#Programacion I
#Trabajo Práctico 1: Estructuras Secuenciales

#Ejercicio 1
"""Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”"""

print("Hola Mundo!")

#Ejercicio 2
"""Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
realizar la impresión por pantalla."""

print("Hola!")
nombre = input("Por favor, escribe tu nombre: ")

print(f"Hola {nombre}!")

#Ejercicio 3
"""Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
la impresión por pantalla."""

print("Hola!")
nombre = input("Por favor, ingresa tu nombre..")
apellido = input("ahora ingresa tu apellido..")
edad = input("ingresa tu edad..")
pais = input("ingresa en qué país vives..")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {pais}.")

#Ejercicio 4
"""Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
su perímetro."""

radio = float(input("Por favor ingrese el radio del circulo: "))
pi = 3.14159
area = pi * radio * radio
new_area = round(area, 2)
perimetro = 2 * pi * radio
new_perimetro = round(perimetro, 2)

print(f"El área del círculo es: {new_area}; y su circunferencia o perímetro es: {new_perimetro} .")

#Ejercicio 5
"""Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
cuántas horas equivale."""

print("Hola!")
numero = input("Ingrese el número de segundos que desea convertir a horas: ")
segundos = int(numero)
horas = segundos / 3600
print (f"{segundos} segundos son {horas} horas")

#Ejercicio 6
"""Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
multiplicar de dicho número."""

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
"""Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos."""

print("Hola!")
numero1 = int(input("Ingresa un número entero, distinto a 0: "))
numero2 = int(input("Ingresa otro número entero, distinto a 0: "))
print(f"La suma de {numero1} y {numero2} es igual a {numero1 + numero2}")
print(f"La resta entre {numero1} y {numero2} es igual a {numero1 - numero2}")
print(f"El producto entre {numero1} y {numero2} es igual a {numero1 * numero2}") 
print(f"La división entre {numero1} y {numero2} es igual a {numero1/numero2}")

#Ejercicio 8
"""Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
modo: IMC = peso en kg /(altura en m)^2"""

print("Hola!")
altura = float(input("Ingrese su altura (en metros): "))
peso = float(input("Ingrese su peso (en kilogramos): "))
imc = peso / altura**2
new_imc = round(imc, 2)

print(f"Su índice de masa corporal es: {new_imc}")

#Ejercicio 9
"""Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: Temp en F° = 9/5*Temp en C° + 32"""

print("Hola!")
celsius = float(input("Ingrese una temperatura en grados Celsius para su conversión a grados Fahrenheit: "))
fahrenheit = 1.8*celsius + 32
print(f"La temperatura {celsius}°C, convertida a grados Fahrenheit es {fahrenheit}°F")

#Ejercicio 10
"""Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
dichos números."""

print("Hola!")
print("Ingrese 3 números para calcular su promedio: ")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
promedio = float((num1 + num2 + num3)/3)

print(f"El promedio es: {round(promedio,2)}")