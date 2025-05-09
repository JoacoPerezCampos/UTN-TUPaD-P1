# Trabajo Practico N° 3 - Estructuras Repetitivas
# Respuestas

# Ejercicio 1
"""Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea."""

for i in range (101):
    print(i)


# Ejercicio 2
"""Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene."""

print("Hola!")
num = (input("Ingrese un número entero, para determinar cuántos dígitos tiene \n"))

def validar_num(num):
    try:
        int(num)
        return True
    except ValueError:
        return False
    
if validar_num(num):
    num = abs(int(num))
    print(f"El número {num} tiene {len(str(num))} cifras")
else:
    print("Debía ingresarse un número entero")


# Ejercicio 3
"""Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores."""

print("Hola! Vamos a sumar los números comprendidos entre dos enteros (sin incluirlos).")
num1_str = input("Ingrese el primer número entero\n")
num2_str = input("Ingrese el segundo número entero\n")

# Validar si la cadena ingresada representa un entero
def validar_entero(num_str):
    try:
        return int(num_str)
    except ValueError:
        return None

# Sumar los enteros comprendidos entre ambos enteros ingresados
def suma_enteros_entre(a,b):
    inicio = min(a,b) + 1
    fin= max(a,b)
    return sum(range(inicio,fin))

num1 = validar_entero(num1_str)
num2 = validar_entero(num2_str)

if num1 is not None and num2 is not None:
    resultado = suma_enteros_entre(num1, num2)
    print(f"La suma de los enteros entre {num1} y {num2} (excluyédolos) es: {resultado}")


# Ejercicio 4
"""Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0."""

# Validar si la cadena ingresada representa un entero
def validar_entero(num_str):
    try:
        return int(num_str)
    except ValueError:
        return None
    
acum = 0 # Inicializar la sumatoria en 0

print("Hola! Vamos a realizar una sumatoria.")
num_str = input("Ingrese un número entero para iniciar la sumatoria: \n(Para terminar y ver el resultado, ingrese '0')\n")
num = validar_entero(num_str)

# Estructura WHILE que suma el número ingresado al acumulador, muestra el mensaje de ingresar el siguiente, y lo valida.
while num !=0:
    acum += num
    num_str = input("Ingrese el siguiente número entero: \n")
    num = validar_entero(num_str)

# Finalizado el WHILE, mostramos el resultado
print(f"Sumatoria terminada. \nEl resultado es: {acum}")
    

# Ejercicio 5
"""Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número."""

# Importamos la biblioteca RANDOM para generar un número aleatorio
import random 

num_secreto = random.randint(0,9) # Genera y almacena el número aleatorio
intentos = 0 # Inicia la cantidad de intentos en 0
acertado = False # Condición del WHILE: será falsa mientras no haya adivinado el número

print("Hola!\nBienvenido al juego!\nAdivina el número (entre 0 y 9)")

while not acertado:
    intento = input("Ingresa tu intento:\n")

    if not intento.isdigit(): # Valida si la cadena es un dígito
        print("Ingresa un número válido (entre 0 y 9)")
    
    intento = int(intento) # Convierte la cadena a entero

    if intento < 0 or intento > 9: # Valida si el entero está entre 0 y 9
        print("El número debe estar entre 0 y 9")
    
    intentos +=1

    if intento == num_secreto:
        acertado = True
    else:
        print("No adivinaste! Intenta de nuevo!")

print(f"¡Correcto! El número era {num_secreto}.\nLo lograste en {intentos} intento(s).")


# Ejercicio 6
"""Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente."""

for i in range(100,0,-2):
    print(i)


# Ejercicio 7
"""Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario."""

print("Hola! Vamos a calcular la suma de todos los números comprendidos entre un número y cero ")
num = input("Ingrese un número entero positivo \n")
acum = 0 # Iniciar la sumatoria en cero

# Validar si la cadena ingresada representa número entero
def validar_entero(num):
    try:
        return int(num)
    except ValueError:
        return None
    
if validar_entero(num) is not None and int(num) > 0:
    for i in range(0,int(num)): # Recorremos todos los valores entre el número ingresado y cero
        acum += i # Agregamos cada valor a la sumatoria
    print(f"La suma de los valores comprendidos entre 0 y {num} es: {acum}")
else:
    print("Debía ingresar un número entero positivo")


# Ejercicio 8
"""Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio)."""

cant_numeros = 100 # Cambiar este valor dependiendo de la cantidad de números que se quieran trabajar
i = 0 # Variable índice de la estructura While
# Iniciamos las variables contadoras en 0
pares = 0 
impares = 0
positivos = 0
negativos = 0

print("Hola! Vamos a evaluar una lista de números para saber cuántos son pares, cuántos impares, cuántos positivos y cuántos negativos")
print(f"Por favor, ingrese {cant_numeros} números enteros")

while i < cant_numeros: # En este caso no usé una estructura for, ya que avanzaría en los valores de i, aún en los casos de un ingreso no válido
    entrada = input(f"Ingrese el número {i+1}\n")
    if entrada.lstrip('-').isdigit(): # Quita el signo en caso de ser negativo y validamos si la cadena representa un dígito
        numero = int(entrada) # Convierte la cadena a entero y almacena en 'numero' 

        if numero % 2 == 0: # Definimos si es par, para sumar a la cuenta de pares o impares
            pares += 1
        else:
            impares += 1

        if numero > 0: # Definimos si es mayor o menor a 0, para sumar a la cuenta de positivos o negativos
            positivos += 1
        elif numero < 0:
            negativos += 1

        i +=1 # Avanza sólo si la entrada fue válida
    else:
        print("Entrada inválida. Por favor, ingrese un número entero\n")

print("Resultados:")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")


# Ejercicio 9
""") Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor)."""

cant_numeros = 10 # Cambiar este valor dependiendo de la cantidad de números que se quieran trabajar
i = 0 # Variable índice de la estructura While
acum = 0 # Variable acumuladora, para almacenar la sumatoria de los numeros ingresados

print(f"Hola! Vamos a calcular la media entre {cant_numeros} números enteros:")

while i < cant_numeros: # En este caso no usé una estructura for, ya que avanzaría en los valores de i, aún en los casos de un ingreso no válido
    entrada = input(f"Ingrese el número {i+1}:\n")
    if entrada.lstrip('-').isdigit(): # Quita el signo en caso de ser negativo y validamos si la cadena representa un dígito
        numero = int(entrada) # Convierte la cadena a entero y almacena en 'numero'
        acum += numero # El número se suma al acumulador
        i += 1 # Avanza sólo si la entrada fue válida
    else:
        print("Entrada inválida. Por favor, ingrese un número entero\n")

media = acum / cant_numeros
print(f"La media (promedio) de los números ingresados es: {media}")

    
# Ejercicio 10
"""Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745."""

numero = input("Hola! Ingrese un número entero para obtener su inversión: \n")

if numero.startswith('-'):
    invertido = '-' + numero[:0:-1] # Excluye el signo negativo al invertir el número, y lo vuelve a añadir al inicio
else:
    invertido = numero[::-1]

print(f"El número invertido es: {invertido}")
