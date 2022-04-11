asignaturas=["Literatura", "Matemtatica", "Quimica"]
print(asignaturas)
print(type(asignaturas))
print('Yo estudio' +" "+ asignaturas[0])
print('Yo estudio' +" "+ asignaturas[1])
print('Yo estudio' +" "+ asignaturas[2])

notasL=input('Cuanto sacaste en Literatura?')
notasM=input('Cuanto sacaste en Matematica?')
notasQ=input('Cuanto sacaste en Quimica?')

print('En:' + asignaturas[0] + " " + 'has sacado' + " "+ "{0}".format(notasL))