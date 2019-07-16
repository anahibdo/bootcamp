#Imprimir el ultimo elemento de una lista sin saber cuantos
# Elementos tiene, solucion general
otra_lista = [5 , "Hola que tal", "chau", 4]
otra_lista.append("AAAA")


# solucion paso por paso
dim_lista = len(otra_lista)
print("La dimension de otra_lista es", dim_lista)
indice_del_ultimo = dim_lista -1
print("El indice del ultimo elemento es", indice_del_ultimo)
print(otra_lista[indice_del_ultimo])

#Solucion de una linea
print(otra_lista[len(otra_lista)-1])

#esto es equivalante
for numero in range (1,11):
    print (numero)
# a esto
    for numero in [1,2,3,4,5,6,7,8,9,10]:
        print(numero)
#Imprimir hola 10 veces
for numero in [1,2,3,4,5,6,7,8,9,10]:
    print("hola", numero) #imprimir numero es opcional

#Imprimir el numero de resultado de la suma de los numeros
#del 1 al 10 
Challenge=[1,2,3,4,5,6,7,8,9,10] #se cra una lista
a=0                              # se crea una variable de base
for x in Challenge:              # se crea un ciclo que va a correr la cantidad de elementos que tiene
    a=a+x                         # s va acumulando las sumas
print(a)
sumatoria=0
for valor in range(1,11):
    sumatoria= sumatoria+ valor
    print(sumatoria)
    ################## FUNCIONES ################


    def suma (num1, num2):
        resultado = num1+ num2
        return resultado

    #Equivalente a la de arriba
    def suma2(num1, num2):
        return num1+num2

    print(suma(5,10))
    resul= suma (5,8)
    print(resul)
    # crear una funcion resta, que reciba como parametro dos numeros
    # y retorne la resta de esos numeros
    # luego llamar a la funcion e imprimir el resultado

    # Crear una funcion saludo2 que reciba como parametro nombre y edad
    # e imprima "HOLA SOY____Y TENGO_____ANOS"
    # Llamar varias veces a la funcion con distintos valores
    # Nota: retornar algo es opcional
def Plantaciones (sembrar,germinar):
        cultivo = sembrar+germinar
        return cultivo
print(Plantaciones(4,9))
def Plantaciones2 (sembrar,germinar):
    cultivo = sembrar- germinar
    return cultivo
print(Plantaciones(4,9))
print(Plantaciones2(4,4))

def saludo2(nombre,edad):
    print("hola soy", nombre, "y tengo", edad, "anos")
saludo2("Anahi", 26)
# Ej. Crear una funcion suma_lista que reciba como argumento una 
# lista de numeros y retorne la suma de sus elementos
# Pista: usar for y una variable acumulador
listita = [1,2,3,4,5] #1+2+3+4+5=15
listota= [100,5,5] # el valor de retorno seria 110
# Pista 2 , la llamada deberia ser:
# suma_lista (listita)
#suma_listo(listota)
#pista 3
def suma_lista(una_lista):
    suma=0
    for x in una_lista:
        suma=suma + x
    print(suma)
    return suma
suma_lista(listita)

#Ej2
lista1 =[1,2,3,4,5]
def suma_lista(lista):
    datos=0
    for x in lista: 
        datos= x+datos
    return datos
print(suma_lista(lista1))

lista2= [4,5,6,7,8,9]
def suma_lista2(lista2):
    datos=0
    for x in lista2:
        datos= x+datos
    return datos
print(suma_lista2(lista2))

def lista_cuadrado(listajeyma):
    a=[]
    for jeyma in listajeyma:
        a.append(jeyma*jeyma)
    return a
otravez= [1,4,9,16,25]
resultado_cuad= lista_cuadrado(otravez)
print(resultado_cuad)

######################################
#ej.: eliminar todos los elementos de una lista utilizando "for"
grupo5 = ["N","F1","F2","A"]
print("antes", grupo5)
for j in grupo5:
    grupo5.pop()
print("despues", grupo5)

# Crear una funcion suma_cuadrado que reciba una lista de numeros
# y retorne el valor de la suma de cada numero al cuadrado
# [1,2,3]--> 1+4+9+19--> 30

list_numeros = [1,2,3,4]

def suma_cuadrado(lista_n):
    suma=0
    for p in lista_n:
        suma = suma + (p*p)
        return suma
print (suma_cuadrado(list_numeros))









