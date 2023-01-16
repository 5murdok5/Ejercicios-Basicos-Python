# if else
edad = int(input('Ingresa tu edad'))


if edad > 18:
    print('Eres mayor de Edad...')
else:
    print('Eres un Menor Alejate...')

# elif
print('----else if--------')
if edad >= 18:
    print('Eres mayor de Edad...')
elif (edad > 15):
    print('te puedo dar un permiso')
elif (edad <= 14):
    print('Estas a limite')
else:
    print('No hay nada para ti aqui')


# COndicionales Anidados

nombre = input('Ingresa tu Usuario: ')

if nombre == 'admin':
    print('Bienvenido Usuari Administrador')
    edad = int(input('Ingresa tu Usuario: '))
    if edad == 18:
        print('Ahora estas listo, pasa!!')
    else:
        print('aun no estas listo, vuelve pronto.')
else:
    print('Tu no eres el admin, que haces aqui!!!')


# Buscando vocales

print('----Buscar Vocal----')

cadena = input('Escribe una cadena: ')

if cadena.lower() == 'a' or cadena.lower() == 'e' or cadena.lower() == 'i' or cadena.lower() == 'o' or cadena.lower() == 'u':
    print('La letra es una VOCAL')
else:
    print('La letra es una CONOSONANTE')

# forma corta
if cadena.lower() in 'aeiou':
    print('La letra es una VOCAL')
else:
    print('La letra es una CONOSONANTE')


# Valores Absolutos

print("-----------VALORES ABSOLUTOS-----------")

num = int(input('Ingresa un Numero:  '))

if num > 0:
    print('valor avsoluto: ', num)
else:
    print('valor avsoluto: ', (num * -1))

# forma corta

print('Valor Absoluto es: ', abs(num))


# Buscando Rimas
'''
    Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas 
    letras tiene que decir que riman. Si coinciden sólo las dos últimas tiene que decir que riman 
    un poco y si no, que no riman.
'''
print('-------------------------------------')
print("-----------Buscando Rimas------------")
print('-------------------------------------')

palabra1 = input('Ingresa una palabra: ')
palabra2 = input('Ingresa otra palabra: ')

if palabra1[-3:].lower() == palabra2[-3:].lower():
    print('Las palabras riman')
elif palabra1[-2:].lower() == palabra2[-2:].lower():
    print('Las palabras riman unpoco')
else:
    print('estas palabras no riman')


print('-------------------------------------')
print("-----------Candidatos------------")
print('-------------------------------------')

candidato = input('Selecciona un candidato (ABC): ')


if candidato.upper() == 'A':
    print('Usted escogio el candidato ROJO')
elif candidato.upper() == 'B':
    print('Usted escogio el candidato AZUL')
elif candidato.upper() == 'C':
    print('Usted escogio el candidato AMRAILLO')
else:
    print('NO EXISTE ESE CANDIDATO !')
