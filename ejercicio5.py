"""
Ejercicios nivel básico
1. Crea una función para verificar si un número es par o impar y devuelva “El número es par” o “El número es impar” según corresponda.
2.Crea una función a la que pases un número como argumento, calcule el factorial de ese número y haga print del resultado.
3.Crea una función a la que se le pase un número como argumento, calcule la cantidad de dígitos y haga print de “La cantidad de dígitos es:” y el resultado total de dígitos.
4.Dada una lista de números, crea una función que devuelva el número máximo de la lista.
5.Crea una función que, dado un número, sume los dígitos de ese número y devuelva el resultado.
6.Dados dos números, crea una función para encontrar el mínimo común múltiplo (MCM) de los dos números, que se les pasarán como argumento a la función, y devuelva el MCM.  
7. Crea una función a la que, pasándole la base y la altura, calcule y devuelva el área de un triángulo.
8.Crea una función que, dado un número, verifique si un número es positivo,
negativo o cero.
9. Crea una función que, dada una palabra, cuente la cantidad de letras en una palabra.
10. Crea una función que, dada una lista de números, convierta la lista de números a su valor absoluto.
11.Crea una función que, dado un número, verifique si un número es primo.
12. Dados dos números, crea una función para encontrar el máximo común divisor (MCD) de esos dos números.

"""
#12
def buscarmcd(y,z):
  while z:
    y,z = z, y%z
  return abs(y)

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

print("El MCD es:",buscarmcd(numero1,numero2))

#11
def primo(m):
  if m < 2:
    return False
  for i in range(2,m):
    if m % i ==0:
      print("no es primo")
      return False
    print("es primo")
    return True
  
m=int(input("Ingrese un numero"))
print(primo(m))



#10
def valorabsoluto(listanum):
  for i in range(len(listanum)):
    listanum[i]=abs(listanum[i])

numeros=[-43,9,0,-5,-7]
valorabsoluto(numeros)
print("La lista con los valores abolutos es:",numeros)


#9
def counting(palabra):
  cont=0
  for letra in palabra:
    if letra.isalpha():
      cont+=1
  return cont

palabra=input("Ingresa una palabra:")
print("la palabra contiene la siguiente cantidad de letras:",counting(palabra))

#8
def conocernum(h):
   if h>0:
      return "positivo"
   elif h==0:
      return 0
   else:
      return "negativo"
   
h=float(input("Ingrese para conocer si es positivo, negativo o 0:"))

print("El numero es",conocernum(h))

#7
def calculararea(base, altura):
  area= 0.5*base*altura
  return area

base= float(input("Ingresa la base del triangulo: "))
altura=float(input("Ingrese la altura del triangulo: "))

print("El area del triagulo es:", calculararea(base,altura))



#6
def findmcm(f,g):
  if f==0 or g==0:
    return "El mcm no se puede realizar con un numero igual 0"
  else:
    maximo=max(f,g)
    while True:
      if maximo % f == 0 and maximo % g == 0:
        return maximo
      maximo +=1

number1=int(input("Ingrese el numero: "))
number2=int(input("Ingrese el otro numero: "))
print("El MCM es:", findmcm(number1,number2))
      

#5
def sumadigi(num5):
  i=str(num5)
  sum=0
  for digito in i:
    sum+= int(digito)
  return sum

num5=int(input("Ingresa un numero "))

print(sumadigi(num5)) 

#4
def nmaximo(listanum):
  max=listanum[0]
  for number in listanum:
    if number>max:
      max=number
  return max
listanum= [2,5,3,8,5,23]
print(nmaximo(listanum))
  

#3
def cantdigi(num3):
  return len(str(num3))

num3=int(input("Ingresa un numero "))
print(cantdigi(num3))

#2
def factorial(c):
  if c == 0:
    return 1
  else:
    return c * factorial(c - 1)

c=int(input("Ingresa un numero "))

print(factorial(c))

#1
def par(num):
  if num%2==0:
    return "Es par"
  else:
    return "es impar"

num_ingresado=int(input("Ingresa un numero "))

print(par(num_ingresado))







    