
conjunto = {1, 2, 3, 4, 5, 6, 7, 6, 6, 6, 65}
conjunto1 = set[(1, 2, 3, 4, 5, 6, 7, 6, 6, 6, 65)]
conjunto3 = set((1, 2, 3, 4, 5, 6, 7, 6, 6, 6, 65))


print(type(conjunto))
print(type(conjunto1))
print(type(conjunto3))


print(conjunto)
# agregar elemento
print('---------------------')
print('Agregando Elemento')
conjunto.add(10)
print(conjunto)

# agregar eiminar
print('---------------------')
print('Eliminar Elemento')
conjunto.discard(6)
print(conjunto)

conjunto.pop()
print(conjunto)

# agregar eiminar
print('---------------------')
print('Actualizar Elemento')
conjunto.update([1, 2, 3])
print(conjunto)

#  vaciar conjunto
print('---------------------')
print('Limpiar Conjunto')
conjunto.clear()
print(conjunto)
