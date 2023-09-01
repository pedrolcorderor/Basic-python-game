print("Hola Mundo ; re virgo haciendo esto ,pero bueno da igual :")
"""
hola mundo
"""
#hola bb
variables ="hola"
print(variables)

#input 
my_name=input("Cual es tu nombre ")
print("Usando input",my_name)
my_age=input("Cual es tu edad ")
print("tu edad es ",my_age)
print("El input convierte el numero en str:",type(my_age))

"""
boleano 
"""
is_single=False
print('is_single=>', is_single, "es de tipo ",type(is_single))

pepito2="I'm Nicolas"
print(pepito2)

"""
Metodo Format . de strings
"""
template= "Hola mi nombre es {} y edad es {}".format(my_name,my_age)
print(template)
#existe otra forma

template= f"Hola mi nombre es {my_name} y edad es {my_age}"
print(template)
"""
Y las palabras usadas son :Por otro lado los placeholders, podemos definirlos las posiciones donde se introducirán los datos con los que entrenamos el modelo y luego nos devuelve el modelo luego de hacer la predicción.
"""
"""
en Python se usa operadores normales -=, += etc y 
si un dato de tipo numero es muy grande o muy pequeño nos dara de notacion cientifica
"""
ngrande=4500000000000000000.1
n_litte=0.00000000001
print(ngrande,"y",n_litte)

enero = float(input("Ingrese su presupuesto para enero"))
febrero = float(input("Ingrese su presupuesto para febrero"))
marzo = float(input("Ingrese su presupuesto para marzo"))

presupuesto = enero + febrero + marzo
print("Su presupuesto total fue:" + " " + str(presupuesto))

promedio = (presupuesto) / 3
print("El promedio es:" + " " + str(promedio))

"""
Boleano

"""
is_single=True
print(type(is_single))
is_single=False
print(is_single)
# Operador logico not
print(not True)
print(not False)

is_single=not is_single
print(is_single)