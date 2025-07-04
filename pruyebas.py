import os
import pygame
from Constantes import *
from Funciones import * 

def generar_lista_elementos(cda_elementos:int,textura:str,medidas:tuple,pos:tuple):
    lista_elementos = []
    for i in range(cda_elementos):
        elemento = generar_elemento(textura,medidas,pos)
        lista_elementos.append(elemento)
        medidas[1] += 100
    return lista_elementos

asd = generar_lista_elementos(4,"box1.png",(ancho_rta,alto_rta),(rta_x,rta_y))
print(asd)