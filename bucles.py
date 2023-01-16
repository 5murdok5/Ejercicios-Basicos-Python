# actualizar variables

x = 0
x += 1  # ? aumenta el valor a 1
print(x)


# WHILE

n = 5
print('----------------------------------------------------------------')
while n > 0:
    print(n)
    n = n-1

print('DESPEGUEN!!')


# FOR
print('------------------------Imprimiendo Valores de Lista------------')
LIST = [1, 2, 3, 6, 5]
for vl in LIST:
    print(vl)

print('----------------------------------------------------------------')

iterador = 0

while iterador < 10:
    iterador += 1
    print('{} entro'.format(iterador))
