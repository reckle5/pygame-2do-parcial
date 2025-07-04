import pygame
from Constantes import *
from Funciones import *
from elementos_de_juego import *

def mostrar_ranking(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego) -> str:
    retorno = "ranking"
    #Gestionar Eventos
    for evento in cola_eventos:
        #Actualizaciones
        if evento.type == pygame.QUIT:
            retorno = "salir"
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if boton_atras["rectangulo"].collidepoint(evento.pos):
                reiniciar_estadisticas(datos_juego)
                retorno = "menu"
                CLICK_SONIDO.play()


    pantalla.fill(COLOR_LILA)

    mostrar_texto(pantalla,"RANKING TOP 10 ",(100,60),FUENTE_TITULO,COLOR_NEGRO)
    mostrar_texto(pantalla,"RANKING TOP 10 ",(98,62),FUENTE_TITULO2,COLOR_BLANCO)

    pantalla.blit(boton_atras["superficie"],boton_atras["rectangulo"])
    dibujar_datos_juego(f"Atras",boton_atras["superficie"],(12,5),FUENTE_TEXTO,COLOR_VIOLETA)

    dato_ranking = leer_archivo_json("ranking.json")
    mostrar_top_10(dato_ranking,pantalla)

    return retorno