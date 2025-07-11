import pygame
from Funciones import *

#juego
cuadro_pregunta = generar_elemento("texturas/button_menu.png",(ANCHO_PREGUNTA,ALTO_PREGUNTA),(PREGUNTA_X,PREGUNTA_Y))
boton_atras = generar_elemento("texturas/box1.png",(ANCHO_BOTON_ATRAS,ALTO_BOTON_ATRAS),(ATRAS_X,ATRAS_Y))
cuadros_rta = generar_lista_elementos(4,"texturas/box1.png",(ANCHO_BOTON,ALTO_BOTON),RTA_X,RTA_Y,75)

#menu
lista_botones = generar_lista_elementos(5,"texturas/button_menu.png",(ANCHO_BOTON,ALTO_BOTON),BOTON_X,BOTON_Y,80)

#ajustes
boton_suma = generar_elemento("texturas/boton ajustes.png",(60,60),(470,320))
boton_resta = generar_elemento("texturas/boton ajustes.png",(60,60),(120,320))

#comodines
bomba = generar_elemento("texturas/bomba.png",(75,65),(180, 230))
doble_puntos = generar_elemento("texturas/x2.png",(75,65),(275, 230))
doble_chance = generar_elemento("texturas/doble chance.png",(75,65),(370, 230))
pasar_pregunta = generar_elemento("texturas/pasar.png",(70,65),(465, 230))

comodin= generar_elemento("texturas/comodin.png",(90,115),(70,460))
comodin["superficie"].set_colorkey((152, 154, 143)) 


bomba["superficie"].set_colorkey((152, 154, 143)) 
doble_puntos["superficie"].set_colorkey((152, 154, 143)) 
doble_chance["superficie"].set_colorkey((152, 154, 143)) 
pasar_pregunta["superficie"].set_colorkey((152, 154, 143)) 

#nuevas_preguntas
boton_pregunta = generar_elemento("texturas/box1.png",(600,120),(50,180))    
lista_botones_preg= generar_lista_elementos(5,"texturas/button_menu.png",(200,ALTO_BOTON),20,BOTON_Y,50)
boton_guardar = generar_elemento("texturas/box1.png",(140,60),(530,630))    
#ajustes
botones_extra_juego = []
botones_extra_juego.extend([comodin,boton_atras])

lista_comodines = []
lista_comodines.extend([bomba,doble_puntos,doble_chance,pasar_pregunta])

lista_elementos_de_juego = []

lista_elementos_de_juego.append(cuadro_pregunta)
lista_elementos_de_juego.extend(cuadros_rta)
lista_elementos_de_juego.append(boton_atras)
lista_elementos_de_juego.append(comodin)
 