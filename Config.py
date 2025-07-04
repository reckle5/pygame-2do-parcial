import pygame
from elementos_de_juego import *
pygame.init()


def mostrar_ajustes(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    retorno = "ajustes"
    
    #Gestionar los eventos
    
    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if boton_suma["rectangulo"].collidepoint(evento.pos):
                if datos_juego["volumen_musica"] <= 95:
                    datos_juego["volumen_musica"] += 5
                    CLICK_SONIDO.play()
                else:
                    ERROR_SONIDO.play()
            elif boton_resta["rectangulo"].collidepoint(evento.pos):
                if datos_juego["volumen_musica"] > 0:
                    datos_juego["volumen_musica"] -= 5
                    CLICK_SONIDO.play()
                else:
                    ERROR_SONIDO.play()
            elif boton_atras["rectangulo"].collidepoint(evento.pos):
                retorno = "menu"
                CLICK_SONIDO.play()
        if evento.type == pygame.QUIT:
            retorno = "salir"
            
    
    #Mostrar en pantalla los elementos
    pantalla.fill(COLOR_LILA)
    
    pantalla.blit(boton_suma["superficie"],boton_suma["rectangulo"])
    pantalla.blit(boton_resta["superficie"],boton_resta["rectangulo"])
    pantalla.blit(boton_atras["superficie"],boton_atras["rectangulo"])
    
    dibujar_datos_juego("AJUSTES DE MUSICA",pantalla,(200,200),FUENTE_TEXTO,COLOR_NEGRO)
    dibujar_datos_juego(f"{datos_juego["volumen_musica"]}%",pantalla,(320,320),FUENTE_TEXTO,COLOR_NEGRO)
    dibujar_datos_juego("+",boton_suma["superficie"],(18,6),FUENTE_AJUSTE,COLOR_NEGRO)
    dibujar_datos_juego("-",boton_resta["superficie"],(20,6),FUENTE_AJUSTE,COLOR_NEGRO)

    dibujar_datos_juego(f"Atras",boton_atras["superficie"],(12,5),FUENTE_TEXTO,COLOR_VIOLETA)
    return retorno