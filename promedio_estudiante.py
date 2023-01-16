
print("================================")
print("Promedio de Estudiante")
print("================================")

practica1 = float(input('Ingrese el valor de la practica 1: '))
practica2 = float(input('Ingrese el valor de la practica 2: '))
practica3 = float(input('Ingrese el valor de la practica 3: '))

examenParcial = float(input('Ingrese la nota del examen parcial: '))
examenFinal = float(input('Ingrese la nota del examen final: '))


promedioParcial = ((practica1 + practica2 + practica3) / 3)
promedioFinal = ((promedioParcial + (2*examenParcial) + (3 * examenFinal)))/6


print("promedio parcial: ", promedioParcial)
print("promedio Final: ", promedioFinal)
