"""
Condicionales 
codigo que se ejecuta o no dependiendo de la expresion boleana que tengamos 
"""
if True:
  print('deber­a ejecutarse')

if False:
  print('nunca se ejecuta')

'''
pet = input('Â¿CuÃ¡l es tu mascota favorita? ')

if pet == 'perro':
  print('genial tienes buen gusto')
elif pet == 'gato':
  print('espero tengas suerte')
elif pet == 'pez':
  print('eres lo maximo')
else:
  print('no tienes ninguna mascota interesante')


stock = int(input('Digita el stock => '))

if stock >= 100 and stock <= 1000:
  print('el stock es correcto')
else:
  print('el stock es incorrecto')
'''


number = int(input('Ingrese un numero => '))
result = number % 2
if result == 0:
	print('Es par')
else:
	print('Es impar')
 
number2 = '10'
print(number)
number=int(number2)

# Escribe tu solución 👇
print("Es par" if number2%2== 0 else "Es impar")