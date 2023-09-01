person = {
    'name': 'nico',
    'last_name': 'molina',
    'langs': ['python', 'javascript'],
    'age': 99
}

print(person)

person['name'] = 'santi'
person['age'] -= 50
person['langs'].append('rust')
print(person)

# Dos formas de eliminar llave valor
del person['last_name']
person.pop('age')

print(person)

# Convierte las llave-valor en tuplas
print('items')
print(person.items())
# nos devuelve las llaves
print('keys')
print(person.keys())
# nos devuelve los valores
print('values')
print(person.values())
pedro = {
    'name': 'Pedro',
    'last_name': 'Cordero',
    'langs': ['pythonhola', 'javascript'],
    'age': 99
}
print("convertir a lista")
print(pedro.values())
print(type(pedro.values()))

guardar = list(pedro.values())
print(guardar)
print("conversion de valores", type(guardar))

# sin conversion
sinconversion = pedro.values()

print("Sin conversion")

print(sinconversion)
print(type(sinconversion))
