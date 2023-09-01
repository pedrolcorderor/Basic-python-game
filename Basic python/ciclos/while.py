#while: cuando no nonozcas la cantidad de elementos a recorrer o la cantidad de iteraciones a realizar.

'''
while True:
  print('se ejecuto')


counter = 0

while counter < 10:
  counter += 1
  print(counter)


counter = 0

while counter < 20:
  counter += 1
  if counter == 15:
    break
  print(counter)
'''

counter = 0

while counter < 20:
  counter += 1
  if counter < 15:
    continue
  print(counter)
  #el continuo  no ejecuta el codigo que le sigue si se cumple la condicion 
  # pero si ejecuta las siguientes itearaciones