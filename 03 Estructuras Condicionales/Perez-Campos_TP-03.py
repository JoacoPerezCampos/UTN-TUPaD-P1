# Trabajo Practico N° 3 - Estructuras Condicionales
# Respuestas


from statistics import mode, median, mean #Utilizado en Ej 6
import random #Utilizado en Ej 6
import string #Utilizado en Ej 7

# Ejercicio 1
print ("Hola!")
edad = int(input("Por favor, ingresa tu edad: \n"))

if edad >= 18:
    print ("Es mayor de edad")

    
# Ejercicio 2
print ("Hola!")
nota = float(input("Por favor, ingresa tu nota: \n"))

if nota >=6:
    print ("Aprobado")
else:
    print ("Desaprobado")

    
# Ejercicio 3
print ("Hola!")
num = float(input("Ingrese un número par: \n"))

if num % 2 == 0:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par. ")

    
# Ejercicio 4
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
print ("Hola!")
password = str(input("Ingrese su contraseña: (debe tener entre 8 y 14 caracteres)\n"))
length = len(password)

if length >= 8 and length <=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

    
# Ejercicio 6

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

print ("Hola!")
texto = input("Ingrese una frase o palabra: \n")

# Elimina espacios finales y signos de puntuación al final.
texto_limpio = texto.rstrip().rstrip(string.punctuation + " ")

if texto_limpio[-1].lower() in "aeiou":
    texto_limpio += "!"

print ("Resultado: ", texto_limpio)


# Ejercicio 8 

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