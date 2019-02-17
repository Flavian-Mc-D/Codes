#Python
# Comentarios de Python son iniciados con #
"""También hay comentarios de 
varias lineas"""

#Para ver información en pantalla:
print('hola mundo') #También puede tener comentarios aqui

#Existen las Variables que son datos que pueden ser modificados, se representan con minusculas. 

mi_variable = 5
print (mi_variable)
#5
#Azul en S.T. es el color de print, fusía el = y morado el 5, en pantalla se vé el 5 solamente.
mi_variable_2 = """ 
Cadena 
de
varias 
lineas 
"""
print (mi_variable_2)
#Cadena 
#de
#varias 
#lineas

#También existen las CONSTANTES que son valores fijos, no editables. representadas en mayusculas.
MI_CONSTANTE = 'VALOR_NO_CAMBIANTE'
print (MI_CONSTANTE)
#VALOR_NO_CAMBIANTE

#Número entero:
edad_e = 35
print (edad_e)
#35
#Número entero octal:
edad_o = 0.43
print (edad_o)
#0.43
#Número entero hexadecimal:
edad_h = 0.10 
print (edad_h)
#0.1
#Número real:
precio = 7435.28
print (precio)
#7435.28
#Booleano (verdadero / Falso):
verdadero = True 
falso = False

#Colecciones de datos:
""" 
Tuplas
Listas
Diccionarios
"""
"""
Una tupla es una variable que permite almacenar varios datos 
inmutables (no pueden ser modificados una vez creados) 
de tipos diferentes:
"""
mi_tupla = ('Cadena de texto', 10, 1.0, 'otro dato', 20)
""" 
Se puede acceder a cada uno de los datos mediante su índice 
correspondiente, siendo 0 (cero), 
el índice del primer elemento:  
"""
print (mi_tupla[0])
#Cadena de texto
print (mi_tupla[1:4])
#(10, 1.0, 'otro dato')
print (mi_tupla[2:])
#(1.0, 'otro dato', 20)
print (mi_tupla[:3])
#('Cadena de texto', 10, 1.0)
print (mi_tupla[-1])
#20
print (mi_tupla[-2])
#otro dato
"""
Lista
Una lista es similar a una tupla con la diferencia 
fundamental de que permite modificar los datos 
una vez creados 
"""
mi_lista = ['cadena de texto', 15, 2.8, 'otro dato', 25]
"""
A las listas se accede igual que a las tuplas, 
por su número de índice. 
"""
print (mi_lista[1])
#15
print (mi_lista[1:4])
#[15, 2.8, 'otro dato']
print (mi_lista[-2])
#otro dato

#Las lista NO son inmutables: 
#permiten modificar los datos una vez creados: 
mi_lista[2] = 3.8  # el tercer elemento ahora es 3.8 
print (mi_lista[2])
#3.8
#Las listas, a diferencia de las tuplas, 
#permiten agregar nuevos valores: 
mi_lista.append('Nuevo Dato')
print (mi_lista)
#['cadena de texto', 15, 3.8, 'otro dato', 25, 'Nuevo Dato']

