cadenna = "Commodo quis cupidatat mollit labore consectetur reprehenderit commodo consequat sit."


print('Tananio cadena:', len(cadenna))
print(cadenna[0:10])


# metodos de cadenas
print('lower: ', cadenna.lower())
print('Upper: ', cadenna.upper())
print('Upper: ', cadenna.title())
print('Upper: ', cadenna.capitalize())
# cambia mayusculas por minusculas y viceversa
print('Upper: ', cadenna.swapcase())


cadenaNueva = 'Te quiero solo como amigo'

print('cadena Nueva', cadenaNueva[0:2])
print('cadena tres ultimos', cadenaNueva[-3:])
print('Cada dos Caracteres', cadenaNueva[:: 2])
print('cadena al reves', cadenaNueva[:: -1])
print(cadenaNueva, '-', cadenaNueva[:: -1])

cadenaB = 'separado'

print(cadenaB.replace('', ','))
