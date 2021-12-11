#Hacer una función en Python para calcular un %.

def CalPorcentaje(x,y):
    rta = x/y*100 
    print(f"El {rta} % de {y} es {x}")

Bandera = True
try:
    while Bandera:
        dat1 = int(input("Ingresa el valor Parcial "))
        dat2 = int(input("Ingresa el valor Total "))
        CalPorcentaje(dat1,dat2)
        valor = int(input("Desea ingresar otro calculo, teclee 1 para si y 0 para no. "))
        if valor == 0:
            Bandera = False

except ValueError:
    print("Error, el valor o los valores ingresados no son validos. Bye")
