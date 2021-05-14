#guia_2_segunda_parte

#ejercicio1
"""
numeros = []
multiplos2 = []
multiplos3 = []

for i in range(1, 11):
    num = int(input("Ingrese un numero:"))
    numeros.append(num)
    if(num % 2 == 0):
        multiplos2.append(num)
    if(num % 3 == 0):
        multiplos3.append(num)

print()
print("Numeros ingresados:", numeros)
print()
print("Multiplos de dos:", multiplos2)
print()
print("Multiplos de tres:", multiplos3)


#ejercicio2

personas = {"camilo": 18,"mateo": 22,"joaquin": 17,"enzo": 25,"manuel": 17,"agustin": 9,"roberto": 76,"mariano": 33,"Julian": 6,"norma": 18,"santos": 60,"Luana": 53,"alberto": 56,"martina": 14,"Nidia": 3}

mayores = 0

for persona, edad in personas.items():
    if(edad >= 18):
        mayores += 1

print("Cantidad de personas mayores:", mayores)

#ejercicio3

numero = int(input("Ingrese un numero: "))
print()
for i in range(1, 11):
    cuenta = i * numero
    print(i, "por", numero, "= a", cuenta)
    

#ejercicio4

notas = [4,2,4,6,8,9,5,7,6,10,4,8,6,7,8,9,3,6]

aprobados = 0
desaprobados = 0
nota = 0

for i in notas:
    if(i >= 6):
        aprobados += 1
        nota += i
    else:
        desaprobados += 1

promedio = round(nota / aprobados, 2)

print("Cantidad de aprobados: %s" % aprobados)
print("Cantidad de desaprobados: %s" % desaprobados)
print("Promedio de los aprobados: %s" % promedio)


#ejercicio5

hoy = 2021

for i in range(1, 10):
    nacimiento = int(input("Ingresar año de nacimiento: "))
    edad = hoy - nacimiento
    if(edad >= 18):
        print("El postulante es mayor de edad.")
        print("-------------------------------")
    else:
        print("El postulante es menor de edad")
        print("-------------------------------")
        

#ejercicio6

numeros = [3,2,18,34,345,203,435,54,34,2,435,345,543,435,453 ]
i = 0
mayor = 0

while i < 15:
    if(numeros[i] > mayor):
        mayor = numeros[i]
    i += 1

print("El numero mayor es %s" % mayor)

#ejercicio7

#ejercicio8

print("Números entre 721 y 895: ")

for i in range(721, 896):
    print(i)
    

#ejercicio9

numero = int(input("Ingrese un numero que no sea cero: "))
positivos = 0
negativos = 0

while numero != 0:
    if(numero < 0):
        negativos += 1
    else:
        positivos += 1

    numero = int(input("Ingrese un numero que no sea cero: "))


print("Numeros positivos ", positivos)
print("Numeros negativos ", negativos)
"""


