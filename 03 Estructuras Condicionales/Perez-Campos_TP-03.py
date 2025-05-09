# Trabajo Practico N° 3 - Estructuras Condicionales
# Respuestas


from statistics import mode, median, mean #Utilizado en Ej 6
import random #Utilizado en Ej 6
import string #Utilizado en Ej 7

# Ejercicio 1
""" Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”."""

print ("Hola!")
edad = int(input("Por favor, ingresa tu edad: \n"))

if edad >= 18:
    print ("Es mayor de edad")

    
# Ejercicio 2
"""Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
mensaje “Desaprobado”."""

print ("Hola!")
nota = float(input("Por favor, ingresa tu nota: \n"))

if nota >=6:
    print ("Aprobado")
else:
    print ("Desaprobado")

    
# Ejercicio 3
"""Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
operador de módulo (%) en Python para evaluar si un número es par o impar."""

print ("Hola!")
num = float(input("Ingrese un número par: \n"))

if num % 2 == 0:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par. ")

    
# Ejercicio 4
""") Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
siguientes categorías pertenece:
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
● Adulto/a: mayor o igual que 30 años."""

print ("Hola!")
edad = int(input("Por favor, ingresa tu edad: \n"))

if edad < 12:
    print("Categoría: Niño/a")
elif edad >= 12 and edad < 18:
    print("Categoría: Adolescente")
elif edad >= 18 and edad < 30:
    print("Categoría: Adulto/a jóven")
elif edad >= 30:
    print("Categoría: Adulto/a")

    
# Ejercicio 5
"""Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
como una lista o un string."""

print ("Hola!")
password = str(input("Ingrese su contraseña: (debe tener entre 8 y 14 caracteres)\n"))
length = len(password)

if length >= 8 and length <=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

    
# Ejercicio 6
"""Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla."""

lista = [random.randint(1,100) for i in range(50)]
media = mean(lista)
mediana = median(lista)
moda = mode(lista)

if media > mediana and mediana > moda:
    print("Hay sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Hay sesgo negativo o a la izquierda")
elif media == mediana == moda:
    print("No hay sesgo")
else:
    print("No ocurre ninguno de los casos anteriores")


# Ejercicio 7
"""Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
pantalla."""

print ("Hola!")
texto = input("Ingrese una frase o palabra: \n")

# Elimina espacios finales y signos de puntuación al final.
texto_limpio = texto.rstrip().rstrip(string.punctuation + " ")

if texto_limpio[-1].lower() in "aeiou":
    texto_limpio += "!"

print ("Resultado: ", texto_limpio)


# Ejercicio 8 
"""Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
lower() y title() de Python para convertir entre mayúsculas y minúsculas."""

print ("Hola!")
nombre = str(input("Por favor, ingrese su nombre: \n"))
resp = input("Indique cómo desea imprimir su nombre: \n1. Si quiere su nombre en mayúsculas \n2. Si quiere su nombre en minúsculas \n3. Si quiere su nombre sólo con la primera letra mayúscula\n")

if resp == "1":
    print(nombre.upper())
elif resp == "2":
    print(nombre.lower())
elif resp == "3":
    print(nombre.title())
else:
    print("Eligió una opción no esperada")


# Ejercicio 9
"""Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
por pantalla:
● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala)."""

print("Hola!")
magnitud = float(input("Por favor, ingrerse la magnitud del terremoto: \n"))

if magnitud < 3:
    print(magnitud, ": Muy leve")
elif magnitud >=3 and magnitud <4:
    print(magnitud, ": Leve")
elif magnitud >=4 and magnitud <5:
    print(magnitud, ": Moderada")
elif magnitud >=5 and magnitud <6:
    print(magnitud, ": Fuerte")
elif magnitud >=6 and magnitud <7:
    print(magnitud, ": Muy fuerte")
else:
    print(magnitud, ": Extremo")


# Ejercicio 10
"""Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
si el usuario se encuentra en otoño, invierno, primavera o verano."""

hemisferio = input("¿En qué hemisferio estás? (N/S): ")
mes = int(input("¿Qué mes es?: (Ingrese el número de mes) "))
dia = int(input("¿Qué día es?: "))

def obtener_estacion(hemisferio, mes, dia):
    
    # Validamos que el mes exista
    if mes <1 or mes>12:
        return "Mes inválido."
    
    # Conformamos la fecha
    fecha = (mes, dia)

    if hemisferio.upper() == 'N': #Convertimos la respuesta a mayúsculas
        if (3, 21) <= fecha <= (6, 20):
            return "Primavera"
        elif (6, 21) <= fecha <= (9, 22):
            return "Verano"
        elif (9, 23) <= fecha <= (12, 20):
            return "Otoño"
        else:
            return "Invierno"
    elif hemisferio.upper() == 'S': #Convertimos la respuesta a mayúsculas
        if (3, 21) <= fecha <= (6, 20):
            return "Otoño"
        elif (6, 21) <= fecha <= (9, 22):
            return "Invierno"
        elif (9, 23) <= fecha <= (12, 20):
            return "Primavera"
        else:
            return "Verano"
    else:
        return "Hemisferio inválido." #Si se ingresa una respuesta no esperada
    
estacion = obtener_estacion(hemisferio, mes, dia)
print("Estás en:", estacion)