import math
import os
import random
import re
import sys
import pprint
import numpy as np

def creaMatriz(n,m): #primero debe ser creado el espacio antes de asignarle valores
    matriz = []
    for i in range(n): #matriz de 0
        a = [0]*m
        matriz.append(a)
    return matriz

def llenar_matriz(m,row,colum):
    for i in range(row):
        for j in range(colum):
            valor=random.randint(1, 100)
            m[i][j]=valor
    return m
 
def matriz_simple_a(row,colum):
    m=creaMatriz(row,colum)  
    llenar_matriz(m,row,colum)
    print(m)


def matriz_numpy(n,m):
    l = np.zeros((n, m))
    llenar_matriz(l,n,m)
    #print(l)
    print(l[0][0])
      

def menor(l):
    
    menor=l[0]
    poss=0
    for x in range(len(l)):
        if l[x] <= menor:
          menor=l[x]
          poss=x
    
    l.pop(poss)
    return(menor)
        

def ord_manual_burbuja(n):
    l=[]
    aux=[0]*n
    for x in range(n):
        l.append(random.randint(1,100))

    print(l)
    i=0
    while len(l)>0:
        aux[i]= menor(l)
        i+=1

    return (aux)

    
    


    
 

if __name__ == "__main__":
    # matriz_simple_a(2,2)
    # matriz_numpy(2,2)

    ord_manual_burbuja(5)

    #En python al hacer "slides" de una lista se tienen en cuenta 3 posiciones lista[inicio:fin:incremento] De esta manera le ordenamos empezar en el número 2, terminar al final (con los dos puntos ":") y avanzar con intervalos de 2.
    lista = [1,2,3,4,5,6,7,8,9,10,11]
    print(lista[1::2])