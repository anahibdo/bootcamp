# ing_pan = ["harina","levadura", "sal","azucar","agua"]

# def imprimir_lista(ingredientes,nombre_producto):

#     print("lista de compras de", nombre_producto)
#     print("___________________")
#     for producto in ingredientes:
#         print(producto)

# imprimir_lista(ing_pan,"Pan")

# ing_salsa= ["tomate","azucar","sal","cebolla"]
# imprimir_lista(ing_salsa, "salsa de pizza")
# ##################CONDICIONALES#########################
# # if pregunta

# #== Igual
# # < menor que
# # > mayor que
# # <= menor o igual que
# # >= mayor o igual que
# # != distinto
# a= 3
# #pregunta 1
# if a > 3:
#     print("Si, a es mayor a 3")
#     print ("chau!")
# else:
#     print ("No, a no es mayor a 3")

# #pregunta 2
# if a== 3:
#     print("a es igual a 3")

# nota= 60
# #pregunta 3
# if nota>=60:
#     print("Pasasteeeee!!!!")
# else:
#     print("Hule ya:(")
# # Ej. crear una funcion que reciba como parametro una
# #nota del 1 al 100 e imprima si pasaste o te aplazaste

# print("ejercicio de ejemplo")
# def Resultado(nota, nombre):
#     if nota > 61:
#         print("lograste", nombre)
#     else:
#         print("Se aplazo!")
# Resultado(70, " ANAHI")

# a=7
# if a > 5 and a < 10:
#     print ("a es mayor a 5 y menor que 10")
# else:
#     print("a no esta en el rango, alguna de las 2 condiciones no se cumplieron")
# if a > 5 or a < 10:
#     print("a es mayor que 5 o menor que 10")
# else:
#     print("a no es mayor que 5 ni menor que 10")

# edad=7
# if edad > 18:
#     print("Deberia estar en la universidad")
# elif edad > 13:
#     print("Deberia estar en la secundaria")
# elif edad > 6:
#     print("Deberia estar en primaria")
# else:
#     prin("Deberia estar en su casa bbdlc")
# #Anidado
# if edad > 18:
#     print("Universidad")
# else:
#     if edad>13:
#         print("Secundaria")
#     else:
#         if edad> 6:
#             print("primaria")
#         else:
#              print("bbdlc")
# # Ej. crear una funcion puntaje que reciba como parametro una nota
# #del 1 al 100 e imprima que nota sacaste
# # nota < 60----->1
# # nota entre 60 y 70 ----->2
# # nota entre 71 y 75------>3
# #nota entre 76 y 85
# #  ------>4
# # nota mayor que 85 ------>5

# def puntaje(nota_final, nombre):


#     if nota_final <60 :
#         print("tu nota es 1", nombre)
#     elif nota_final >60  and nota_final < 70:
#         print("tu nota es 2", nombre)
#     elif nota_final >71  and nota_final < 75:
#         print("tu nota es 3", nombre)
#     elif nota_final >76  and nota_final < 85:
#         print("tu nota es 4", nombre)
#     elif nota_final >85  and nota_final < 101:
#         print("tu nota es 5 felicidades", nombre)

# puntaje(4,"Anahi")
# puntaje(68,"Willi")
# puntaje(100, "Francisco")

# # ej. Pedir al usuario que ingrese tres numeros y multiplicarlos
# # entre si, imprimir el resultado
# int("22")+ 3 #----> 25
# num1= input("ingresa el primer numero:")

# # Ej2. Pedir al usuario un numero del 1 al 100 y llamar a la
# # funcion que retornaba la nota que creamos hace un rato 
# # utilizando el valor ingresado por el usuario

# Anahi = input ("ingresa tu nombre")
# print(Anahi)
# A = int(input("tengo"))
# B = int(input("tengo"))
# C = int(input("tengo"))
# multip=A*B*C
# print (multip)

# Anahi= input ("ingresa tu nombre")
# print(Anahi)
# Anahi1= input("uno")
# Anahi2= input("dos")
# Anahi3= input("tres")
# variado= int(Anahi1)*int(Anahi2)*int(Anahi3)
# print(variado)



# #######Bucle while== mientras#####

# x=749556
# while x!=5: #mientras x sea distinto de 5 hacer lo siguiente
#     print("esto es un bucle while, se va a ejecutar mientras x sea distinto de 5")
#     x= int (input("Ingresa un numero:")) #ingresamos un valor para x
#     print("terminado!!!!")

# #contador inverso
# contador= 10
# while contador > 0:
#     print("sigo en el bucle while")
#     contador = contador -1
#     print("te quedan",contador, "oportunidades")
# print("termino")
# #contador
# contador=0
# while contador< 10:
#     print("sigo en el bucle while")
#     contador= contador+1
#     print("se repitio", contador, "veces")
# #Usando while pedir al usuario 5 ingredientes para hacer una pizza
# # y agregar a una lista, al final imprimir la lista


# Pedido=0
# lis_ingr=[]
# while Pedido <5:
#     print("pizza")
#     Pedido=Pedido+1
#     ingre=input("Ingrese los ingredientes:")
#     lis_ingr.append(ingre)
#     pedido=pedido+1

# adivino= False
# numero_secreto= 7
# while adivino == False:
#     apuesta= input("Adivina el numero secreto del 1 al 10:")
#     if int(apuesta)== numero_secreto:
#         print("GANASTE!!!")
#         adivino= True
#     else:
#         print("Segui participando nde arruinado")

# #EJ1. Crear un juego de adivinar el numero como el de arriba y
# #darle pistas al usuario si el numero que ingreso es mayor o menor
# #al numero a  adivinar
# #pista usar elif


# #Ej.2 Buscar como generar un numero aleatorio para numero_secreto

# #1 Probar que funcione sin pistas
# #2 que tengo que comparar?
# #3 donde tengo que comparar?
# #4 Informar al usuario

#EJ1.
adivinar= False
numero_pista= 70
while adivinar == False:
    apuesta= input("Adivina con pistas del 1 al 100:")

    if int(apuesta)== numero_pista:
        print("de lujo")
        adivinar= True
    elif numero_pista > int(apuesta):
        print  ("el numero es mas grande")   

    elif numero_pista< int(apuesta):
        print(" el numero es mas pequeno")
    