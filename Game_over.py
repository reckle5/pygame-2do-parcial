import pygame
from Constantes import *
from Funciones import *
pygame.mixer.init()

def mostrar_game_over(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego) -> str:
    retorno = "game over"

    #Gestionar Eventos
    for evento in cola_eventos:
        #Actualizaciones
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.TEXTINPUT:
            datos_juego["nombre"] += evento.text
        elif evento.type  == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    guardar_ranking(datos_juego)
                    retorno = "ranking"
                elif evento.key == pygame.K_BACKSPACE:
                     datos_juego["nombre"] = datos_juego["nombre"][:-1]
            
 
    game_over(pantalla)
    mostrar_texto(pantalla,datos_juego["nombre"],(250,500),FUENTE_RELOJ,COLOR_VERDE)

    return retorno