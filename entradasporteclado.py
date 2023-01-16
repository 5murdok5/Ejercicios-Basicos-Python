from math import sqrt

print("================================")
print("Ecuacion general")
print("================================")

A = int(input('ingresa el valor de A: '))
B = int(input('ingresa el valor de B: '))
C = int(input('ingresa el valor de C: '))

x1 = 0
x2 = 0
respSqd = ((B**2) - (4*A*C))
if (respSqd < 0):
    print("no se puede realizar por que es un numero negativo")
else:
    x1 = ((-B + sqrt(respSqd)))/(2*A)
    x2 = ((-B - sqrt(respSqd)))/(2*A)

print('Resultados \n')
print(x1)
print(x2)
