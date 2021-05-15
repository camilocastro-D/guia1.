#parcial_programacion
#Castro_camilo

#ejercicio1

import json
import requests
import random

def get_carter_by_id(id):
    respuesta = requests.get('https://swapi.dev/api/people/'+str(id))
    if respuesta.status_code == 200:
        dic = json.loads(respuesta.text)
        return dic


def obtener_personaje():
    personaje_al_azar = random.rango(1, 82, 2)
    character = get_carter_by_id(personaje_al_azar)
    return character

def main():
    personaje1 = obtener_personaje()
    personaje2 = obtener_personaje()


    tallespersonaje = personaje1 if personaje1['altura'] > personaje2['altura'] else personaje2

    pesopersonaje = personaje1 if personaje1['masa'] > personaje2['masa'] else personaje2

    participacion_en_peliculas = personaje1 if len(personaje1['films']) > len(personaje2['films']) else personaje2

    print(str(personaje1['nombre']) + ' vs ' + str(personaje2['nombre']))

    print('El mas alto es: ' + str(tallespersonaje.get('nombre')))

    print('El mas pesado es: ' + str(pesopersonaje.get('nombre')))

    print('El que estuvo en mas peliculas es: ' + str(participacion_en_peliculas.get('nombre')))
    
    main()


#ejercicio3

#A
from random import randint
lista = []
for i in range (77):
    num= randint (0,10000)
    print (num)
    lista.append(num)

lista.sort()

print ("El menor es ",lista[0])

from random import randint
lista = []
for i in range (77):
    num= randint (0,10000)
    print (num)
    lista.append(num)

lista.sort()

print ("El mayor es ",lista[10000])

if (lista % 2==0):
        print(lista)


