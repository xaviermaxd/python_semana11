alumnos = {
    'alumno1' : 'Rosa Maria',
    'alumno2' : 'Ernesto Castillo',
    'alumno3' : 'Jose Torres',
    'alumno4' : 'Yessenia Sanchez',
    'alumno5' : 'Khaty Perez',
}

# pregunta A
print(alumnos)
print("-"*30)

# pregunta B
print("El número de alumnos es: ",len(alumnos))
print("-"*30)

# pregunta C
print(alumnos.keys())
print("-"*30)

# pregunta D
print(alumnos.values())
print("-"*30)

# prengunta E
for key in alumnos.keys():
    print(alumnos[key])
print("-"*30)

# pregunta F
alumnos['alumno6'] = 'Jordan Gala'

# pregunta G
print(alumnos)
print("-"*30)

# pregunat H
alumnos_nuevos = {
    'alumno7' : 'Jimmy Tinoco'
}
alumnos.update(alumnos_nuevos)
print(alumnos)
print("-"*30)

# pregunta I
del alumnos['alumno5']
print(alumnos)
print("-"*30)

# pregunta J
alumnos_copia = alumnos.copy()
print(alumnos_copia)
print("-"*30)

# pregunta K
alumnos.clear()
print(alumnos)
print(alumnos_copia)
print("-"*30)

# pregunta I
print(alumnos_copia.items())
print("-"*30)

# pregunta M y N
alumnos_2 = {
    'alumno8' : 'Jorge Mamani',
    'alumno9' : 'Joan Arroyo',
    'alumna10' : 'Adriana Reyes'
}
alumnos_copia.update(alumnos_2)
print(alumnos_copia)
print("-"*30)