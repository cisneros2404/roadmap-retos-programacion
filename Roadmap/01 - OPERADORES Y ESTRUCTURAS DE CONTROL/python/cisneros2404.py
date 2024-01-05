"""
 EJERCICIO:
 - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
   que representen todos los tipos de estructuras de control que existan
   en tu lenguaje:
   Condicionales, iterativas, excepciones...
 - Debes hacer print por consola del resultado de todos los ejemplos.

 DIFICULTAD EXTRA (opcional):
 Crea un programa que imprima por consola todos los números comprendidos
 entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

 Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
"""

print("--- Operadores aritméticos ---")
print("Adición: 10 + 5 =", 10 + 5)
print("Sustracción: 10 - 5 =", 10 - 5)
print("Multiplicación: 10 * 5 =", 10 * 5)
print("División: 10 / 5 =", 10 / 5)
print("División entera truncada: 10.5 // 2 =", 10.5 // 2) #Redondea hacia abajo los valores decimales
print("Módulo o residuo: 10 % 5 =", 10 % 5)
print("Exponencial: 5 ** 3 =", 5 ** 3,"\n")

print("--- Operadores de asignación ---")
num_1 = 100
print("Operador =   | num_1 = 100    |", num_1)
num_1 = 100; num_1 += 50
print("Operador +=  | num_1 += 50    |", num_1)
num_1 = 100; num_1 -= 50
print("Operador -=  | num_1 -= 50    |", num_1)
num_1 = 100; num_1 *= 50
print("Operador *=  | num_1 *= 50    |", num_1)
num_1 = 100; num_1 /= 50
print("Operador /=  | num_1 /= 50    |", num_1)
num_1 = 100; num_1 %= 50
print("Operador %=  | num_1 %= 50    |", num_1)
num_1 = 100; num_1 //= 50.5
print("Operador //= | num_1 //= 50.5 |", num_1)
num_1 = 100; num_1 **= 2
print("Operador **= | num_1 **= 2    |", num_1,"\n")

print("--- Operadores de lógicos ---")
print("1. AND")
print("True and False :",True and False)
print("False and True :",False and True)
print("True and True :",True and True)
print("False and False :",False and False,"\n")
print("OR")
print("True or False :",True or False)
print("False or True :",False or True)
print("True or True :",True or True)
print("False or False :",False or False,"\n")
print("NOT")
print("not True :",not True)
print("not False :",not False,"\n")

print("---Operadores de comparación/relacionales---")
print("Operador ==  | 2==2  |", 2==2)
print("Operador !=  | 2!=2  |", 2!=2)
print("Operador >   | 2>1   |", 2>1)
print("Operador <   | 2<1   |", 2<1)
print("Operador >=  | 2>=1  |", 2>=1)
print("Operador <=  | 2<=1  |", 2<=1,"\n")

print("---Operadores de identidad---")
"""
El operador is comprueba si dos variables hacen referencia al mismo objeto, tomando como dato el identificador obtenido con la función id().
Así como el operador is not hará lo contrario que is.
En los siguientes ejemplos, el resultado será True o False según si las variables hacen referencia al mismo objeto
"""
x = 5
y = 5
print("Identificador variable x = 5:", id(x))
print("Identificador variable y = 5:", id(y))
print("Operador is | x is y     | Resultado:", x is y)
print("Operador is | x is not y | Resultado:", x is not y,"\n")
a = [1,2,3]
b = [1,2,3]
print("Identificador lista a = [1,2,3]:", id(a))
print("Identificador lista b = [1,2,3]:", id(b))
print("Operador is | a is b     | Resultado:", a is b)
print("Operador is | a is not b | Resultado:", a is not b,"\n")
p1 = "marco"
p2 = "marco"
print("Identificador variable p1 = marco:", id(p1))
print("Identificador variable p2 = marco:", id(p2))
print("Operador is | p1 is p2     | Resultado:", p1 is p2)
print("Operador is | p1 is not p2 | Resultado:", p1 is not p2,"\n")

print ("---Operadores de membresía---")
"""
Los operadores 'in' y 'not in' nos permiten saber si un elemento esta contenido o no es caso de 'not in'
en una secuencia. Por ejemplo si un número está dentro de una lista.
"""
print("Operador in     | 3 in [1,2,3]     | Resultado:", 3 in [1,2,3])
print("[1,2] in [3,4,[1,2],6,7]           | Resultado:",[1,2] in [3,4,[1,2],6,7])
print("Operador not in | 3 in not [1,2,3] | Resultado:", 3 not in [1,2,3])
print("[1,2] not in [3,4,[1,2],6,7]       | Resultado:",[1,2] not in [3,4,[1,2],6,7])