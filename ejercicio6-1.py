"""
Ejercicios nivel medio
1. Ejercicio: Define una función que utilice un bucle para imprimir los primeros n números de la serie de Fibonacci.
2. Ejercicio: Define una función que tome un número y retorne una lista de sus divisores.
3. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos únicos de la lista original.
4. Ejercicio: Define una función que tome un número y retorne la suma de sus dígitos.
5. Ejercicio: Define una función que tome una cadena y cuente el número de vocales en la cadena.
6.Define una función que tome una lista y un número n, y retorne los
primeros n elementos de la lista.
7.Define una función que tome una cadena y retorne la cantidad de
letras mayúsculas y minúsculas en la cadena.
8.Define una función que tome un número y retorne True si es un número perfecto, False en caso contrario. Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3.
9.Define una función que reciba un número y retorne su representación en binario.
10.Define una función que reciba dos listas y retorne la intersección de ambas (los elementos que están en las dos listas).
"""
#10
def insterseccion_listas(lista1,lista2):
  setlista1= set(lista1)
  setlista2= set(lista2)
  return list(set(lista1)&set(lista2))

print(insterseccion_listas([2,2,5,8,9,4], [9,0,2,5,4,8,3]))
    

#9
def binario(num):
  if num < 0:
    return "Ingrese un numero positivo"
  if num == 0:
    return "0b0"
  else:
    return bin(num)
  
print(binario(4))


#8
def numperfecto(num):
  if num <= 0: 
    return False
  sum_divisores= sum(i for i in range(1,num) if num%i==0)
  return num==sum_divisores

if numperfecto(6):
  print("Es un numero perfecto")
else:
  print("No es un numero perfecto")


#7
def contar_minmay(cadena):
  may=sum(1 for letra in cadena if letra.isupper())
  min=sum(1 for letra in cadena if letra.islower())
  return may,min

print(contar_minmay("HOolAA"))

#6
def dev_nelemtos(lista,n):
  return lista[:n]

listaa=[3, 8, 9,34,895,55,2,4]
print(dev_nelemtos(listaa,2))

#5
def contarvoc(palabra):
  return sum(1 for letra in palabra if letra.lower() in 'aeiou')

print(contarvoc("hola"))

#4
def sumadigi(y):
  str_num=str(y)
  sum=0
  for digito in str_num:
    sum+=int(digito)
  return sum


print(sumadigi(22))


#3
def elemunicos(lista):
  return list(set(lista))

lista=[1, 2, 3, 2, 4, 5, 1, 6]
print(elemunicos(lista))

#2
def divisores(m):
  return [i for i in range(1,m+1) if m%i ==0 ]

print(divisores(6))


#1
def fibonacci(n):
  a,b=0,1
  for i in range(n):
    print(a, end=' ')
    a,b=b, a+b

fibonacci(15)