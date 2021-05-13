# ejercicio 1
# base = float (input ('ingrese el valor de la base'))
# altura = float (input ('ingrese el valor de la altura'))

# area = base * altura

# print ('el area del rectangulo es:', round (area, 2), 'cm')

# # print ('el area del rectangulo es:', base * altura, 'cm')

# # ejercicio 2
# valor_producto = float (input ('ingrese el valor de la maquina dolares'))
# valor_dolar = float (input ('ingrese el valor del dolar en pesos'))

# print ('el valor de la maquina es pesos es', valor_producto * valor_dolar)

# # ejercicio 3
# anio_actual = 2021
# anio_nacimineto = int (input ('ingrese el año de nacimiento'))

# print ('la edad de la persona es', anio_actual - anio_nacimineto)

# # ejercicio 4

#print ("CALCULAR EL AREA DE UN TRIANGULO")
#base=input("CUAL ES LA BASE: ")
#altura=input("CUAL ES LA ALTURA: ")
#area=int (base) * int (altura) / 2.0
#print ("el resultado es: ",area)

# # ejercicio 5
#precioxhora = int(input("ingrese el precio por hora "))
#horasestacionadas = int(input("ingrese la cantidad de horas estacionadas "))
#print("es resultado es: ", precioxhora * horasestacionadas)

# ejercicio 6
#cantidad_m2  =  int ( input ( "ingrese la cantidad de m2 a pintar" ))
#costo_litro_pintura  =  float ( input ( "costo del litro de pintura" ))

#total_pintura  =  cantidad_m2  *  costo_litro_pintura
#mano_obra  =   total_pintura *  0.45
#total  =  total_pintura  +  mano_obra

#print ( 'el monto total es' , total )

# ejercicio 7
# de la raíz cuadrada de importación matemática

# lado_a = int (input ('ingrese el valor del lado a'))
# lado_b = int (input ('ingrese el valor del lado b'))

# # calcula la hipotenusa
# diagonal = int (sqrt (lado_a ** 2 + lado_b ** 2)) # calcula la hipotenusa

# print ('la distancia en diagonal', diagonal)

#ejercicio 8

#cantidad_de_tiros = int(input("ingrese la cantidad de tiros "))
#cantidad_de_aciertos = int(input("ingrese la cantidad de aciertos"))
#print ("la eficacia es de: ",cantidad_de_tiros * 100 / cantidad_de_aciertos, "%")

#ejercicio 9

#cantidad_de_kilometros = int(input("ingrese la cantidad de kilometros recorrido "))
#precio_por_kilometros = int(input("ingrese el precio por kilometros "))
#print ("el precio es de: ", cantidad_de_kilometros * precio_por_kilometros)

#ejercicio 10
#print ("la bicicleta se mueve a 10KM/H")
#velocidad = 10
#cantidad_de_kilometro_recorridos = int(input("ingrese la cantidad de kilometros recorridos "))
#print (("el tiempo que demora es de: ",cantidad_de_kilometro_recorridos/velocidad),"horas: ")

# ejercicio 11
#minutos  =  int ( input ( 'ingrese duracion de la llamada en minutos' ))
#costo_minuto  =  int ( input ( 'ingrese costo del minuto de llamada' ))

#total_llamada  =  minutos  *  costo_minuto
#adicional  =  5  *  total_llamada  /  100

#total  =  total_llamada  +  adicional
#print (total)

#ejercicio 12

#precio_KW = 10
#consumo = int(input("ingrese la cantidad de KW consumido "))
#print("es costro total es de: ",round(((precio_KW * consumo) * 1.0021)/ 1.037,2 ))

#ejercicio 13

#valor_producto = float(input("ingrese el precio del producto: "))
#ganancia  =  27

#precioFinal  =  round (( valor_producto  *  1.27 ), 2 )

#print ( "El precio final del producto es:$ " , precioFinal )

#ejercicio 14

#primer_parcial = int(input("ingrese la nota del primer parcial: "))
#segundo_parcial = int(input("ingrese la nota del segundo parcial: "))
#tercer_parcial = int(input("ingrese la nota del tercer parcial: "))
#cuarto_parcial = int(input("ingrese la nota del cuarto parcial: "))

#nota_promedio = round((primer_parcial + segundo_parcial + tercer_parcial + cuarto_parcial) /4,)
#print ("el promedio final es de:",nota_promedio)

#ejercicio 15

#importe = float(input("Ingrese el importe a pagar: "))

#ivan = round((importe * 0.40), 2)
#german = round((importe * 0.33), 2)
#esteban = round((ivan * 0.55), 2)
#hernan = round((importe - ivan - german - esteban), 2)

#print("Ivan debe pagar: ", ivan)
#print("German debe pagar: ", german)
#print("Esteban debe pagar: ", esteban)
#print("Hernan debe pagar: ", hernan)

#ejercicio 16 

#from statistics import mean

#lunes_temperatura = float(input("ingrese la temperatura del dia lunes: "))
#martes_temperatura = float(input("ingrese la temperatura del dia martes: "))
#miercoles_temperatura = float(input("ingrese la temperatura del dia miercoles: "))
#jueves_temperatura = float(input("ingrese la temperatura del dia jueves: "))
#viernes_temperatura = float(input("ingrese la temperatura del dia viernes: "))
#sabado_temperatura = float(input("ingrese la temperatura del dia sabado: "))
#domingo_temperatura = float(input("ingrese la temperatura del dia domingo: "))

#presion_lunes = float(input("ingrese la presion del dia lunes: "))
#presion_martes = float(input("ingrese la presion del dia martes: "))
#presion_miercoles = float(input("ingrese la presion del dia miercoles: "))
#presion_jueves = float(input("ingrese la presion del dia jueves: "))
#presion_viernes = float(input("ingrese la presion del dia viernes: "))
#presion_sabado = float(input("ingrese la presion del dia sabado: "))
#presion_domingo = float(input("ingrese la presion del dia domingo: "))

#data1 = [lunes_temperatura, martes_temperatura, miercoles_temperatura, jueves_temperatura, viernes_temperatura, sabado_temperatura, domingo_temperatura]

#data2 = [presion_lunes, presion_martes, presion_miercoles, presion_jueves, presion_viernes, presion_sabado, presion_domingo]

#print("la temperatura promedio de la semana es de: ", mean(data1))
#print ("la presion promedio de la semana es de: ", mean(data2))

#ejercicio 17 

#horas = int(input("ingrese la cantidad de horas: "))

#segundos = horas * 60 * 60

#print ("la cantidad de segundos es de: ", segundos,)

#ejercicio 18

#medicion1 = float(input("Ingrese primera medicion: "))
#medicion2 = float(input("Ingrese segunda medicion: "))
#medicion3 = float(input("Ingrese tercera medicion: "))

#milimetros = medicion1 + medicion2 + medicion3

#print("Hoy llovió:", milimetros)