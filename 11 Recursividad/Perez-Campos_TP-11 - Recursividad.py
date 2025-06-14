# Trabajo Práctico N° 11 - Aplicación de la Recursividad

# Ejercicio 1
"""Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular 
y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario"""

#funcion
def factorial_recur(num):
    if num == 0:
        return 1
    else:
        return num * factorial_recur(num-1)
    
#main
num = int(input("Ingrese un número entero para calcular su factorial: "))
print(factorial_recur(num))


# Ejercicio 2
"""Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada.
Posteriormente, muestra la serie completa hasta la posición que el usuario especifique."""

#funcion
def fibonacci_recur(pos): #funcion para calcular el número en la posición indicada
    if pos == 0 or pos == 1:
        return pos
    else:
        return fibonacci_recur(pos - 1) + fibonacci_recur(pos - 2)
    
#main
pos = int(input("Ingresa un número entero que indique cuántos elementos de la serie quiere mostrar: "))
print("Serie de Fibonacci:")
for i in range (pos +1):
    print(fibonacci_recur(i), end=" ")


# Ejercicio 3
"""Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, 
utilizando la fórmula 𝑛^𝑚 = 𝑛 ∗ 𝑛^(𝑚−1). Prueba esta función en un algoritmo general."""

#funcion
def potencia_recur(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia_recur(base, exponente -1)

base = int(input("Ingrese un número entero para la base: "))
exponente = int(input("Ingrese un número entero para el exponente: "))

resultado = potencia_recur(base, exponente)
print(f"{base} ^ {exponente} = {resultado}")


# Ejercicio 4
"""Crear una función recursiva en Python que reciba un número entero positivo en base decimal 
y devuelva su representación en binario como una cadena de texto."""

#funcion
def decimal_a_binario_recur(num):
    if num == 0:
        return ""
    else:
        return decimal_a_binario_recur(num//2) + str(num % 2)

#main
num = int(input("Ingrese un número entero positivo para convertir a binario: "))
if num == 0:
    print(f"Cero convertido a binario es cero")
else:
    binario = decimal_a_binario_recur(num)
    print(f"{num} convertido a binario es {binario}")


# Ejercicio 5
"""Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de 
texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es."""

#funcion
def es_palindromo_recur(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo_recur(palabra[1:-1])

#main
palabra = str(input("Ingrese una palabra para evaluar si es un palíndromo: ")).lower().strip(" ")
if es_palindromo_recur(palabra):
    print(f"{palabra} es un palíndromo")
else:
    print(f"{palabra} no es un palíndromo")


# Ejercicio 6
"""Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número 
entero positivo y devuelva la suma de todos sus dígitos."""
#funcion
def suma_digitos_recur(num):
    if num < 10:
        return num
    else: 
        return (num % 10) + suma_digitos_recur(num //10)

#main
num = int(input("Ingrese un número entero positivo para obtener la suma de sus dígitos: "))
print(f"La suma de los dígitos de {num} es: {suma_digitos_recur(num)}")


# Ejercicio 7
"""Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, 
en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con 
un solo bloque. Escribí una función recursiva contar_bloques(n) que reciba el número de bloques 
en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide."""

#funcion
def contar_bloques_recur(num):
    if num == 1:
        return 1
    else:
        return num + contar_bloques_recur(num - 1)

#main
num = int(input("Ingrese la cantidad de bloques en la base de la pirámide: "))
print(f"Para terminar de construir una pirámide con {num} bloques en su base, necesitamos {contar_bloques_recur(num)} bloques más.")


# Ejercicio 8 
"""Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo 
(numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número."""

#funcion
def contar_digito_recur(num, digito):
    if num == 0:
        return 0
    if num % 10 == digito:
        return 1 + contar_digito_recur(num // 10, digito)
    else:
        return contar_digito_recur(num //10, digito)

#main
digito = int(input("Ingrese el dígito que desea buscar en el número: "))
num = int(input("Ingrese el número en el que desea buscar el dígito: "))
print(f"El dígito {digito} aparece {contar_digito_recur(num,digito)} veces en el número {num}")