text = "Ella sabe Python"
pedro="Eres un crack"
print(text[0])
print(text[1])
print(pedro[1])
print(pedro[6])
# print(text[999])
size = len(text)
print('size => ',size)
print(text[size - 1])
print(text[-6]) # python lo entiende que acedemos desde la ultima pocision
size2=len(pedro)
print('size => ',size2)
print(pedro[size2 - 1])
print(pedro[-5])
print("\n")
# slicing
text = "Ella sabe Python"
print(text[0:5])
print(text[10:16])
print(text[:10]) #es una forma abreviada de inicializarlo en 0
print(text[5:-1])# el problema es que quirata el ultimo digito porque es la referencia del final
print(text[5:]) # desde ese punto hasta el final
print(text[:])
print(text[10:16:1])# el ultimo digito es el numero de saltos de caracteres .
print(text[10:16:2])
print(text[::2])
lista=['hola', 'Pedro ','hola','sofi']
print(lista[1:4])
numero="123 456789"
print(numero[::2])