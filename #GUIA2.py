#GUIA2

#ejercicio1

#numero = float(input("Ingrese un numero: "))

#if(numero < 19):
#    print(numero, " es menor que 19")

#ejercicio2

#numero = float(input("Ingrese un numero: "))

#if(numero > 0):
 #   print(numero, " es positivo.")
#elif(numero == 0):
 #   print("Ingresaste un cero.")
#else:
 #   print(numero, " es negativo.")

#ejercicio3 

#numero = float(input("Ingrese un numero: "))

#if(numero % 2 == 0):
 #   print(numero, " es par.")
#else:
 #   print(numero, " es impar.")

 #ejercicio4

#primer_parcial = int(input("ingrese la nota del primer parcial: "))
#segundo_parcial = int(input("ingrese la nota del segundo parcial: "))
#tercer_parcial = int(input("ingrese la nota del tercer parcial: "))

#nota_promedio = round((primer_parcial + segundo_parcial + tercer_parcial) /3,)

#if(nota_promedio >= 6):
 #   print("Alumno aprobado con promedio ", nota_promedio)
#else:
 #   print("Alumno desaprobado con promedio ", nota_promedio)

 #ejercicio 5

#hoy = 2021 

#nacimiento = int(input("Ingresar año de nacimiento: "))

#edad = hoy - nacimiento

#if(edad >= 18):
 #   print("El postulante es mayor de edad.")
#else:
 #   print("El postulante es menor de edad")

#ejercicio 6 

#numero1 = int(input("ingrese un primer numero: "))

#numero2 = int(input("ingrese un segundo numero:"))

#numero_final = numero1 - numero2

#if (numero_final < 0):
 #   print("el segundo numero es el mayor")
#else:
 #   print("el primer numero ingresado es el mayor")

#ejercicio7 



#costo_producto = int(input("ingrese el valor del producto"))

#tarjeta = int(input("Ingrese 1 para tarjeta visa, 2 para mastercard: "))

#visa = round(costo_producto * 1.07, 2)
#master = round(costo_producto * 1.11, 2)

#if(tarjeta == 1):
 #   print("Monto a cobrar con visa: ", visa)
#elif(tarjeta == 2):
 #   print("Monto a cobrar con master: ", master)
#else:
 #   print("Tarjeta incorrecta.")

 #EJERcicio8

#costo_producto = float(input("ingrese el valor del producto: "))
#cuotas = int(input("ingrese la cantidad de cuotas que desea pagar: "))
#tarjeta = int(input("Ingrese 1 para tarjeta visa, 2 para mastercard: "))

#visa = round(costo_producto * 1.07, 2)
#master = round(costo_producto * 1.11, 2)

#if(tarjeta == 1):
 #   print("Monto a cobrar con visa: ", visa)
#elif(tarjeta == 2):
 #   print("Monto a cobrar con master: ", master)
#else:
 #   print("Tarjeta incorrecta.")

#if(cuotas == 1):
 #   print("Cobrar sin recargos: ", visa)
#elif(cuotas == 3):
 #   recargo = visa * 1.03
  #  print("Cobrar con 3 % de recargos: ", recargo)
#elif(cuotas == 8):
 #   recargo = master * 1.17
  #  print("Cobrar con 17 % de recargos: ", recargo)
#elif(cuotas == 12):
 #   recargo = master * 1.32
  #  print("Cobrar con 32 % de recargos: ", recargo)
#else:
 #   print("Cuotas incorrectas.")

#ejercicio9

#personas = 1

#while personas <= 3:
 #   nombreApellido = input("Ingrese nombre y apellido: ")
  #  nacimiento = int(input("Ingresar año de nacimiento: "))
   # edad = 2021 - nacimiento
    #if(edad >= 18):
     #   print("=================================")
      #  print("La persona ", nombreApellido, "es mayor de edad.")
       # print("=================================")
    #personas += 1

#ejercicio10

#numero = int(input("ingresar un numero: "))
#cubo = numero ** 3

#if(numero % 2 == 0 or numero % 5 == 0):
 #   if(numero % 2 == 0 and numero % 5 == 0):
  #      print(numero, "es multiplo de 2 y 5")
   #     print(numero, "elevado al cubo es ", cubo)
    #elif(numero % 2 == 0):
     #   print(numero, "es multiplo de 2")
      #  print(numero, "al cubo es ", cubo)
    #else:
     #   print(numero, "es multiplo de 5")
      #  print(numero, "al cubo es ", cubo)
#else:
 #   print("El numero no es multiplo de 2 ni de 5.")

#ejercicio11

#numero = float(input("ingrese un numero: "))

#if(numero >= -15 and numero <=81):
 #   print("el numero: ", "se encuentra dentro del rango requerido")
#else:
 #   print("el numero: ","no se encuentra dentro del rango requerido")

#ejercicio12

#mes = int(input("Ingrese numero de mes (1 a 12): "))

#if(mes >= 1 and mes <= 12):
 #   if mes in [4, 6, 9, 11]:
  #      print("El mes ingresado tiene 30 dias.")
   # elif(mes == 2):
    #    print("El mes ingresado tiene 28 dias.")
    #else:
     #   print("El mes ingresado tiene 31 dias.")
#else:
 #   print("Mes incorrecto.")


#ejercicio13

#numeros = 1
#lista = []
#while numeros < 4:
 #   numero1 = float(input("Ingrese un numero: "))
  #  lista.append(numero1)
   # numeros += 1

#maximo = max(lista, key=float)
#print("El numero mayor de los ingresados es:", maximo)

#ejercicio14

#fecha = input("Ingrese fecha en formato dd/mm: ")
#largo = len(fecha)

#if(largo != 5):
 #   print("fecha incorrecta.")
#else:
 #   dia = int(fecha[0:2])
  #  mes = int(fecha[3:5])
   # if((dia >= 1 and dia <= 31) and (mes > 0 and mes < 13)):
    #    print("¡¡Fecha correcta!!")
    #else:
     #   print("Fecha incorrecta :(")

     #ejercicio15

#temp = float(input("Ingrese la temperatura: "))
#escala = input("Ingrese la escala de la temperatura,(C o F): ")

#Fahrenheit = round((temp * 9/5) + 32, 2)
#celsios = round((temp - 32) * 5/9, 2)

#if(escala.upper() == "F"):
 #   print("La temperatura en escala Fahrenheit es: ", Fahrenheit)
#elif(escala.upper() == "C"):
 #   print("La temperatura en escala Celsius es", celsios)
#else:
 #   print("Escala incorrecta.")

#ejercicio16
#ejercicio17

#ejercicio18

#reparto = ["primera", "segunda", "tercera"]
#repar = [0, 1, 2]
#palos = [1, 2, 3, 4]

#palo = []
#cartas = []

#puntos = []


#def barajar():
 #   for item in repar:
  #      carta = int(input("Ingrese %s carta: " % reparto[item]))

   #     if(carta not in [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]):
    #        print("Carta invalida. Saliendo del programa.")
     #       break
      #  else:
       #     cartas.append(carta)
        #    pal = int(
         #       input("Ingrese palo(1:Espada, 2:Basto, 3:Oro, 4:Copas):"))
          #  palo.append(pal)


#def tieneEnvido(palo, palos):
 #   for item in palos:
  #      repite = palo.count(item)

   #     if(repite == 2):
    #        return (palo)


#def puntos(palo, cartas, palos):
 #   envido = []
  #  palito = tieneEnvido(palo, palos)
   # for item in range(0, 3):
    #    if(palo[item] == palito):
     #       x = cartas[item]
      #      envido.append(x)
    #if((envido[0] or envido[1]) >= 10):
     #   tantos = 20
    #elif((envido[0] and envido[1]) < 9):
     #   tantos = 20 + envido[0] + envido[1]
    #else:
     #   tantos = 20 + int(min(envido))
    #print("-------------------------------------------")
    #print("¡El jugador tiene %s puntos para el envido!" % tantos)
    #print("-------------------------------------------")


#def iniciar():
 #   barajar()
  #  if((palo[0] and palo[1] and palo[2]) == palo[0]):
   #     print("----------------------------")
    #    print("¡El jugador tiene flor!")
     #   print("----------------------------")
    #else:
     #   puntos(palo, cartas, palos)


#iniciar()








