num1 = 2
num2 = 3
num3 = 2

cadena1 = 'Adipisicing enim esse voluptate dolore amet laborum amet.'
cadena2 = 'Adipisicing enim esse voluptate dolore amet laborum amet.'

# COmparacion de numeros tambien aplicable a strings
print('Mayor que', num2 > num3)
print('Menor que que', num1 < num2)
print('Mayor o Igual', num1 >= num3)
print('Menor o Igual', num1 <= num3)
print('Igualdad', num1 == num3)
print('Diferente a', num2 != num3)

print('Igualdad', cadena1 == cadena2)
print('Diferente a', cadena1 != cadena2)


# Operadores Logicos
# AND
print('AND OPERATOR', num1 > num2 and num1 < num3)
print('OR OPERATOR', num1 > num2 or num1 < num3)
print('Negacion', not (num1 > num2))
print('Negacion', not (num1 > num2 or num1 < num3))


# Metodos BOLEANOS
cadena3 = input('Ingresa una cadena: ')
verificador = input('Ingresa una letra: ')

print('La cadena empieza por: ', cadena3.startswith(verificador))
print('La cadena termina por: ', cadena3.endswith(verificador))
print('La Cadena esta en Mayusculas?: ', cadena3.isupper())
print('La Cadena esta en Minuscula?: ', cadena3.islower())
