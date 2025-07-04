import pygame
from Funciones import *

#juego
cuadro_pregunta = generar_elemento("texturas/button_menu.png",(ANCHO_PREGUNTA,ALTO_PREGUNTA),(PREGUNTA_X,PREGUNTA_Y))
boton_atras = generar_elemento("texturas/box1.png",(ANCHO_BOTON_ATRAS,ALTO_BOTON_ATRAS),(ATRAS_X,ATRAS_Y))
cuadros_rta = generar_lista_elementos(4,"texturas/box1.png",(ANCHO_BOTON,ALTO_BOTON),RTA_X,RTA_Y,75)
#menu
lista_botones = generar_lista_elementos(4,"texturas/button_menu.png",(ANCHO_BOTON,ALTO_BOTON),BOTON_X,BOTON_Y,100)
#ajustes
boton_suma = generar_elemento("texturas/boton ajustes.png",(60,60),(470,320))
boton_resta = generar_elemento("texturas/boton ajustes.png",(60,60),(120,320))



lista_elementos_de_juego = []

lista_elementos_de_juego.append(cuadro_pregunta)
lista_elementos_de_juego.extend(cuadros_rta)
lista_elementos_de_juego.append(boton_atras)

 