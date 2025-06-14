# Trabajo Práctico N° 6 - Funciones
# Respuestas

# Ejercicio 1
"""Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal."""

def imprimir_hola_mundo():
    return print("Hola Mundo!")

imprimir_hola_mundo()


# Ejercicio 2
"""Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario."""

def saludar_usuario(nombre):
    return print(f"Hola {nombre}!")

nombre = str(input("Ingrese su nombre:\n"))
saludar_usuario(nombre)


# Ejercicio 3
"""Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados."""

def informacion_personal(nombre, apellido, edad, residencia):
    return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

def pedir_informacion():
    nombre = str(input("Ingrese su nombre:\n"))
    apellido = str(input("Ingrese su apellido:\n"))
    edad = int(input("Ingrese su edad:\n"))
    residencia = str(input("Ingrese su residencia:\n"))
    return nombre, apellido, edad, residencia

nombre, apellido, edad, residencia = pedir_informacion()
informacion_personal(nombre, apellido, edad, residencia)


# Ejercicio 4
"""Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo, y calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados."""

def calcular_area_circulo(radio):
    area = 3.14 * (radio ** 2)
    return print(f"El área del círculo es: {area}")

def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.14 * radio
    return print(f"El perímetro del círculo es: {perimetro}")

radio = float(input("Ingrese el radio del círculo:\n"))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

# Ejercicio 5
"""Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función."""

def segundos_a_horas(segundos):
    minutos = segundos // 60
    horas = minutos // 60
    resto_segundos = segundos % 60
    resto_minutos = minutos % 60
    return print(f"{segundos} segundo/s son {horas} hora/s, {resto_minutos} minuto/s y {resto_segundos} segundo/s")

segundos = int(input("Ingrese la cantidad de segundos:\n"))
segundos_a_horas(segundos)


# Ejercicio 6
"""Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función."""

def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar de {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
        i += 1

numero = int(input("Ingrese un número:\n"))
tabla_multiplicar(numero)


# Ejercicio 7
"""Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara."""

def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "No se puede dividir por cero"
        
    return (suma, resta, multiplicacion, division)

def mostrar_resultados(resultados):
    print(f"Suma: {resultados[0]}")
    print(f"Resta: {resultados[1]}")
    print(f"Multiplicación: {resultados[2]}")
    print(f"División: {resultados[3]}")

a = float(input("Ingrese el primer número:\n"))
b = float(input("Ingrese el segundo número:\n"))
resultados = operaciones_basicas(a,b)
mostrar_resultados(resultados)


# Ejercicio 8
"""Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales."""

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return print(f"Su IMC es: {imc:.2f}")

peso = float(input("Ingrese su peso en kg:\n"))
altura = float(input("Ingrese su altura en metros:\n"))
calcular_imc(peso,altura)


# Ejercicio 9
"""Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función."""

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return print(f"{celsius}°C son {fahrenheit}°F")

celsius = float(input("Ingrese la temperatura en grados Celsius:\n"))
celsius_a_fahrenheit(celsius)


# Ejercicio 10
"""Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función."""

def calcular_promedio(a,b,c):
    promedio = (a + b + c) / 3
    return print(f"El promedio de {a}, {b} y {c} es: {promedio:.2f}")

def pedir_notas():
    a = float(input("Ingrese la primera nota:\n"))
    b = float(input("Ingrese la segunda nota:\n"))
    c = float(input("Ingrese la tercera nota:\n"))
    return a, b, c

a, b, c = pedir_notas()
calcular_promedio(a,b,c)