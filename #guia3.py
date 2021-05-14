#guia3

#ejercicio1

def suma(numero1, numero2):
    return numero1 + numero2

#ejercicio2

def positivo_negativo(num):
    if(num > 0):
        return True
    else:
        return False

#ejercicio3

def areaRectangulo(base, altura):
    return base*altura

#ejericio4

def caracterRepetido(palabra, caracter):
    cont = 0
    for i in range(0, len(palabra)):
        if(palabra[i] == caracter):
            cont += 1
    return cont

#ejercicio5

def palindromo(palabra):
    pal = list(palabra)
    pal.reverse()
    aux = ''
    aux = aux.join(pal)
    if(palabra == aux):
        return True
    else:
        return False

#ejercicio6

def serie(n):
    cuenta = 0

    for i in range(1, n+1):
        cuenta = 1 + 1/i

    return cuenta

#ejercicio7

def calculadora(num1, num2, opt):
    if(opt == '+'):
        return num1 + num2
    elif(opt == '-'):
        return num1 - num2
    elif(opt == '*'):
        return num1 * num2
    elif(opt == '/'):
        return num1 / num2
    elif(opt == '**'):
        return num1 ** num2

#ejercicio8

def esPrimo(numero):
    for n in range(2, numero):
        if numero % n == 0:
            return False
    return True


# 9
def esVocal(letra):
    if(letra in ['a', 'e', 'i', 'o', 'u']):
        return True
    return False


# 10
def mayor(num1, num2):
    if(num1 > num2):
        return num1
    return num2


# 11
def intercambio(a, b):
    x = a
    a = b
    b = x
    return a, b


# 12 
def numeroAleatorio(primero, segundo):
    return randint(primero, segundo)


# 13
def factorial(n):
    factor = 1
    while n > 1:
        factor *= n
        n -= 1
    return factor

# 15
def hipotenusa(cateto1, cateto2):
    return sqrt(cateto1 ** 2 + cateto2 ** 2)


# 16
def alfabeto():
    return list(string.ascii_lowercase)


# 17
def tabla(base):
    for i in range(1, 11):
        multiplicacion = str(i * base)
        print(str(i) + ' * ' + str(base) + ' = ' + multiplicacion)


# 18
def conversorTiempo(tiempo, unidad):
    if(unidad.upper() == 'H'):
        return tiempo * 60 * 60
    elif(unidad.upper() == 'S'):
        return round((tiempo / 60) / 60, 2)


# 19

def reglaTres(magnitud, proporcionX, proporcion):
    """ calcula la regla de tres simple, parametros: magnitud, proporcionX, proporcion"""
    return (magnitud * proporcionX / proporcion)


# 20.

def esPrimo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True


def sumaPrimos(inicio, fin):
    suma = 0
    for i in range(inicio, fin):
        if esPrimo(i) == True:
            suma += i
    return suma