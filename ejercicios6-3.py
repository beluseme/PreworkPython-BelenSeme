"""
21. Ejercicio: Define una función que reciba una cadena y cuente el número de dígitos y letras que contiene.
22. Ejercicio: Define una función que reciba una lista de números y retorne la suma acumulada de los números
23. Ejercicio: Define una función que encuentre el elemento más común en una lista.
24. Ejercicio: Define una función que tome un número y retorne un diccionario con la tabla de multiplicar de ese número del 1 al 10.
25. Ejercicio: Define una función que tome una cadena y retorne un diccionario con la cantidad de apariciones de cada caracter en la cadena.
26. Ejercicio: Define una función que tome dos listas y retorne la lista de elementos que no están en ambas listas.
27. Ejercicio: Define una función que tome una lista y retorne la lista sin duplicados.
28. Ejercicio: Define una función que reciba un número entero positivo y retorne la suma de los cuadrados de todos los números pares menores o iguales a ese número.
29. Ejercicio: Define una función que reciba una lista de números y retorne el promedio de los números en la lista.
"""
#29
def promediolista(lista29):
    sum=0
    contador=0
    for digito in lista29:
        sum+=digito
        contador+=1
    return sum/contador

lista29=[2,2,5,8,9,4]
print(promediolista(lista29))

#28
def sumacuadrados_paresmenores(num):
    sum=0
    for i in range(2,num+1,2):
        sum += (i**2)
    return sum

print(sumacuadrados_paresmenores(4)) 


#27
def noduplicados(lista27):
    return set(lista27)

lista23=[2,2,5,8,9,4]
print(noduplicados(lista23))

#26
def noinsterseccion_listas(lista1,lista2):
  return list(set(lista1) ^ set(lista2))

print(noinsterseccion_listas([2,2,5,8,9,4], [9,0,2,5,4,8,3]))

#25
def apariciones(cadena):
    apariciones={}
    for caracter in cadena:
        apariciones[caracter]=apariciones.get(caracter,0)+1
    return apariciones

cadena="Hola a todos como estan"
print(apariciones(cadena))


#24
def diccionario_multiplos(num):
    diccionario={}

    for i in range(1,11):
        resultado=num*i
        diccionario[i]=resultado
    return diccionario

num=int(input("Ingrese un numero"))

print(diccionario_multiplos(num))

#23
def elemento_mascomun(lista23):
    return max(set(lista23), key=lista23.count)
    
lista23=[2,6,5,7,6,6,5,4,6,8]
print(elemento_mascomun(lista23))


#22
def suma_lista(lista):
    suma=0
    suma_acumulada=[]
    for digi in lista:
        suma+=digi
        suma_acumulada.append(suma)
    return suma_acumulada

lista= [1, 2, 3, 4, 5]
print(suma_lista(lista))


#21
def cuentadigitos(cadena):
    letras=0
    digitos=0
    for caracter in cadena:
        if caracter.isalpha():
            letras+=1
        elif caracter.isdigit():
            digitos +=1
    return letras,digitos

cadena="Belen3442"

letras,digitos=cuentadigitos(cadena)
print("Numero de letras:",letras)
print("Numero de digitos:",digitos)


