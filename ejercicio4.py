"""
1. Ejercicio: Define una función que tome dos números y retorne su suma.
2. Ejercicio: Define una función que tome un número y retorne su factorial.
3. Ejercicio: Define una función que tome un número y determine si es primo.
4. Ejercicio: Define una función que reciba una lista de números y retorne la suma de ellos.
5. Ejercicio: Define una función que reciba una cadena de texto y retorne la cadena en reversa.
"""
#1
def suma(a,b):
  return a + b
print(suma(3,5))

#2
def factorial(c):
  if c == 0:
    return 1
  else:
    return c * factorial(c - 1)

print(factorial(21))
#3
def primo(d):
  if d < 2:
    return False
  for i in range(2,d):
    if d % i ==0:
      print("no es primo")
      return False
    print("es primo")
    return True

print(primo(4))
#4
def sumarlista(lista):
  return sum(lista)

print(sumarlista([1,5,8,2]))
#5
def invertircadena(cadena):
  return cadena[::-1]

print(invertircadena("Hola Soy Belen"))

