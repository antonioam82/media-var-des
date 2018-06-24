import numpy as np
from VALID import ns, OKI, OK
import subprocess

def compru(opcis):
    n=0
    for i in opcis:
        if i!="A" and i!="B" and i!="C" and i!=",":
            n+=1
    if n>0 or len(opcis)==0:
        return False
    else:
        return True

        
#ESTE PROGRAMA CALCULA LA MEDIA, LA VARIANZA Y LA DESVIACIÓN TIPICA DE UNA LISTA DE DATOS.
while True:
    print("¿Que desea calcular?")
    print("A)MEDIA")
    print("B)VARIANZA")
    print("C)DESVIACIÓN TÍPICA")
    val=False
    while val==False:
        opciones=input("Introduzca las opciones que desea calcular separadas por coma: ")
        lista_op=list(opciones)
        val=compru(lista_op)
    lista=[]
    elem=OKI(input("Introduzca número de datos a calcular: "))
    for i in range(elem):
        dat=OK(input("Introduzca dato: "))
        lista.append(dat)
    print(lista)
    a=np.array(lista,float)
    if "A" in opciones:
        print("")
        res=a.mean()
        print("MEDIA: ",res)
    if "B" in opciones:
        res=a.var()
        print("")
        print("VARIANZA: ",res)
    if "C" in opciones:
        res=a.std()
        print("")
        print("DESVIACIÓN TIPICA: ",res)
        print("")
    conti=ns(input("¿Desea continuar?: "))
    if conti=="n":
        break
    subprocess.call(["cmd.exe","/C","cls"])
