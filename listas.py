# listaHomogenea = [1, 2, 3, 6, 4, 5, 5, 6, 5,]
# listaHeterogeneas = [1, 'dsa', 3.2, False, 'dat', '5', 5, 6, 5,]

# print('tamanio: ', len(listaHomogenea))
# print('Valor: ', listaHomogenea[3])

# listaHeterogeneas[2] = 'puthon'
# print('Lista Cambiada: ', listaHeterogeneas)

# # debanado de listas
# # Funciona igual de las cadenas


# print('Obtener un valor', listaHeterogeneas[5])
# print('Obtener hasta el 5', listaHeterogeneas[0:5])
# print('Obtener hasta el 5', listaHeterogeneas[:5])
# print('Obtener apartir del 1', listaHeterogeneas[1:])


# # metodos en listas
# lista = [3, 4, 5, 6, 7, 5, 3, 2, 5]

# # agredando datos

# print('Lista completa', lista)

# lista.append(3)
# print('lista con dato agregado: ', lista)

# lista.append(1)
# print('lista con dato agregado: ', lista)

# lista.insert(2, 2)
# print('insertando en la posicion 2: ', lista)

# # OCntar cuantas veces aparece un elemento
# print('aparecen: ', lista.count(5), 'veces')


# # DOnde se encuenta el elemento el primero que encuentre
# print('se encuentra en la posicion: ', lista.index(5))

# # ordenando lista
# lista.sort()
# print('lista ordenada ascendente: ', lista)
# lista.reverse()
# print('lista ordenada descendente: ', lista)

# listaNew = ['animal', 1, '3', 3, 6, 4, 4, 2, 'casa']
# listaNew[0] = 'ANIMAL'
# print(listaNew)

# # Eliminar datos de la lista
# # Elimina el ultimo valor
# listaNew.pop()
# print(listaNew)
# # remover un valor especifico
# listaNew.remove(1)
# print(listaNew)

# listaA = [1, 2, 3]
# listaB = [4, 5, 6]

# listaC = listaA + listaB
# # lista vacia
# listaD = []

# print(listaC)

# listaD.append('new value')
# print(listaD)

'''
    En la siguiente lista, debes hacer un programa que muestre los valores al usuario, 
    a su vez, debe pedir dos datos y esos que sean ingresados 
    deben ser sustituidos en el primer y segundo lugar:
    
    [20, 50, "Curso", 'Python', 3.14]
'''

listex = [20, 50, "Curso", 'Python', 3.14]

fistValue = input('ingresa un valor: ')
secondValue = input('ingresa un valor 2: ')
print('Lista Completa', listex)
print('firstvalue= ', fistValue)
print('secondValue= ', secondValue)

listex[0] = fistValue
listex[1] = secondValue

print('Nueva lista: ', listex)

'''
    Escribe una lista que tenga los números de 1 al 10. Luego, debes hacer que 
    los datos que están en las posiciones 4, 7 y 9 sean multiplicados por 2; 
    por último, mostrar la lista nueva con los nuevos datos

'''
newList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

newList[4] = newList[4] * 2
newList[7] = newList[7] * 2
newList[9] = newList[9] * 2
# FOrma 2
newList[4] *= 2
newList[7] *= 2
newList[9] *= 2

print(newList)
