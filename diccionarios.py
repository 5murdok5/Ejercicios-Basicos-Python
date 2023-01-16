# diccionario = {
#     'nombre': 'Santiago',
#     'edad': 20,
#     'estatura': 170.20

# }
# # Obtener solo llaves
# print('Llaves:', diccionario.keys())
# # obtener valores
# print('Valor: ', diccionario.values())

# # obtener u valor
# print('valor de clave: ', diccionario['nombre'])
# # agregando nuevo valor
# print('add valor')
# diccionario['peso'] = 18.5
# print(diccionario)


# # modificando valor
# print('Update valor')
# diccionario['nombre'] = 'Santiago Moreno'
# print(diccionario)


# # eliminar valor
# print('delete valor')
# diccionario.pop('peso')
# print(diccionario)


# # obtener el valor
# print('obtener dato valor')
# valor = diccionario.get('nombre')
# print(valor)


# # agregar nuevo
# print('Agregadno Valores nuevos: ')
# diccionario.setdefault('edades_Casa', 55)
# print(diccionario)


# # agregar nuevo
# print('Actualizar diccionario: ')
# dic2 = {'clase': 'anatomia', 'grado': 2}
# diccionario.update(dic2)
# print(diccionario)

# # Generar copia copia de diccionario
# print('Generar Copia Diccionario')
# diccionario.copy()
# print(diccionario)

'''
    En el siguiente diccionario se encuentran capitales de los paises 
    en el mundo, debes realizar un programa que pida un pais al usuario, 
    y muestre la capital de ese pais, en dado caso el pais no este en el 
    diccionario, se debe mostrar un mensaje diciendo que ese pais no se 
    encuentra.
'''

pais = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras", "Nicaragua": "Managua",
        "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

resp = input('Ingresa tu pais: ')
vl = pais.get(resp.title())
if vl == None:
    print('No se encontro ese pais')
else:
    print('su capital es: ', pais[resp.title()])
