#Hacer un código en Python de preguntas y respuestas.
'''
Hacer un código en Python de preguntas y respuestas.
El programa debe tener precargado una serie de preguntas y respuestas para seleccionar.
El programa debe correr en consola con un menú imprimible y opciones a seleccionar.
Comportamiento esperado  es: 
Se visualiza la pregunta, seguido de las posibles respuestas (a, b, c, d)
El usuario las lee y procede a seleccionar una de las respuestas
Se visualiza en la consola si es verdad o falso
El programa debe continuar con las demás preguntas
Al finalizar las preguntas se debe visualizar cuantos aciertos correctos hubo y cuantos fallidos
Extra point: con ayuda del ejercicio (1) visualizar cuánto fue el % de éxito en preguntas y respuestas. 
'''
import operator

Totalpreguntas = 3
global contador
contador = 0

dic1 = {'Cuál es la capital de Colombia?':'Bogotá'}
List1= ['Bogotá','Barranquilla','Cali','Medellín','Bucaramanga']

dic2 = {'Qué significa ONU?':'Organización de naciones unidas'}
List2= ['Organización de naciones unidas','Organización de noticias unidas ','Organo nacional unilateral']

dic3 = {'Cómo se llama la profe del diplomado?':'Yurley'}
List3= ['Yurley','Laura','Tatiana']

def Pregunta1():
    global contador
    for key, value in sorted(dic1.items() , key=operator.itemgetter(1)):
        print("*****************************************************")
        print(f"{key}")
        for y in List1:
            print(y)
        rta = input("Elija la Opción correcta: ")
        if(value == rta):
            contador = contador + 1
            print("---------------------------------------------------")
            print("Rta correcta. /n")
            Pregunta2()
        else:
            print("---------------------------------------------------")
            print("Has perdido. ")

def Pregunta2():
    global contador
    for key, value in sorted(dic2.items() , key=operator.itemgetter(1)):
        print("*****************************************************")
        print(f"{key}")
        for y in List2:
            print(y)
        rta = input("Elija la Opción correcta: ")
        if(value == rta):
            contador = contador + 1
            print("---------------------------------------------------")
            print("Rta correcta. /n")
            Pregunta3()
        else:
            print("---------------------------------------------------")
            print("Has perdido. ")

def Pregunta3():
    global contador
    for key, value in sorted(dic3.items() , key=operator.itemgetter(1)):
        print("*****************************************************")
        print(f"{key}")
        for y in List3:
            print(y)
        rta = input("Elija la Opción correcta: ")
        if(value == rta):
            contador = contador + 1
            print("---------------------------------------------------")
            print("Rta correcta. /n")
            Extra()
        else:
            print("---------------------------------------------------")
            print("Has perdido. ")

def Extra():
    global contador
    print("")
    rta = contador/Totalpreguntas * 100 
    print(f"El {rta} % de {Totalpreguntas} es {contador}")
