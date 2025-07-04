import pygame
from Constantes import *
from Funciones import *
from elementos_de_juego import *

pygame.init()

def mostrar_menu(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]) -> str:
    retorno = "menu"
    
    for evento in cola_eventos:
       
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                for i in range(len(lista_botones)):
                    if lista_botones[i]["rectangulo"].collidepoint(evento.pos):
                        CLICK_SONIDO.play()
                        if i == 0:
                            retorno = "jugando"
                        elif i == 1:
                            retorno = "ranking"
                        elif i == 2:
                            retorno = "ajustes"
                        else:
                            print("salir")
                            retorno = "salir"
        
    pantalla.blit(FONDO_MENU,(0,0))

    
    dibujar_elementos(lista_botones,pantalla)

    mostrar_texto(pantalla,"PREGUNTADOS ",(100,101),FUENTE_TITULO,COLOR_NEGRO)
    mostrar_texto(pantalla,"MUSIC ",(217,155),FUENTE_TITULO,COLOR_NEGRO)

    mostrar_texto(pantalla,"PREGUNTADOS ",(98,98),FUENTE_TITULO2,COLOR_BLANCO)
    mostrar_texto(pantalla,"MUSIC ",(218,152),FUENTE_TITULO2,COLOR_BLANCO)

    mostrar_texto(lista_botones[0]["superficie"],"JUGAR",(80,10),FUENTE_MENU,COLOR_VIOLETA)
    mostrar_texto(lista_botones[0]["superficie"],"JUGAR",(77,10),FUENTE_MENU,COLOR_LILA)

    mostrar_texto(lista_botones[1]["superficie"],"RANKINGS",(60,10),FUENTE_MENU,COLOR_VIOLETA)
    mostrar_texto(lista_botones[1]["superficie"],"RANKINGS",(57,10),FUENTE_MENU,COLOR_LILA)

    mostrar_texto(lista_botones[2]["superficie"],"AJUSTES",(60,10),FUENTE_MENU,COLOR_VIOLETA)
    mostrar_texto(lista_botones[2]["superficie"],"AJUSTES",(57,10),FUENTE_MENU,COLOR_LILA)

    mostrar_texto(lista_botones[3]["superficie"],"SALIR",(80,10),FUENTE_MENU,COLOR_VIOLETA)
    mostrar_texto(lista_botones[3]["superficie"],"SALIR",(77,10),FUENTE_MENU,COLOR_LILA)

    return retorno