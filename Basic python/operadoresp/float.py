x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
print(x == y)

y_str = format(y, ".2g")
print('str =>', y_str)
print(y_str == str(x))

print('*' * 10)

print(y, x)

tolerance = 0.00001
print(abs(x - y) < tolerance)
print(abs(x-y))
"""
y claro si los decimales que y es mayor(menos ceros) que la tolerancia :0.00001 significa que ese numero en el los decimales si pueden ser de importancia , pero si la tolerancia es mayor 
0.0000001 > 0.00000000000005 entendemos que puede llegar a ser insificativo ese margen y al  por lo tanto igualar y por x daria igual.
"""
'''
Tolerancia:
Una cierta cantidad de error ocurrirá inevitablemente entre el valor medido y el valor verdadero. Lo importante es especificar el rango de error permitido. En términos de medición, la diferencia entre las dimensiones máximas y mínimas de los errores permitidos se denomina "tolerancia". El rango de error permitido, prescrito por la normatividad, como en las normas industriales, puede denominarse también tolerancia.
Si en un dibujo se escribe "60 (+0.045 -0.000)", "60" representa la cota de referencia, y "+0.045 -0.000" indica la tolerancia de los límites superior e inferior. En este caso, el límite superior es 60.045 y el inferior es 60.000.
Una de las razones de establecer tolerancias para las aplicaciones prácticas, es encontrar un equilibrio entre el costo de procesamiento y las funciones previstas del objeto. Los aumentos de precisión conducen a aumentos proporcionales en los costos de procesamiento. El punto importante es asegurarse de que se logran las funciones y la calidad exigidas; las tolerancias se deberán establecer en consecuencia.

Información sobre el equipo
'''