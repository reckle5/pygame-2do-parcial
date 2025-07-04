import pygame
from Constantes import *
from Funciones import *
from Menu import *
from Juego import *
from Game_over import *
from Rankings import *
from Config import *

pygame.init()
pygame.mixer.init()

pygame.display.set_caption("PREGUNTADOS")
icono = pygame.image.load("texturas/icono.png")
pygame.display.set_icon(icono)

pantalla = pygame.display.set_mode(PANTALLA)

reloj = pygame.time.Clock()
estado_juego = True
estado_mouse = False
estado_pregunta = False
ventana_actual= "menu" 
bandera_juego = False

datos_juego = {"puntuacion":0,"vidas":CANTIDAD_VIDAS,"nombre":"","tiempo":TIEMPO_RESTANTE,"indice":0,"preguntas_correctas":0,"tiempo_inicio":pygame.time.get_ticks(),"volumen_musica":1}

while estado_juego:

    reloj.tick(FPS)
    cola_de_eventos = pygame.event.get()

    if ventana_actual == "menu":
        ventana_actual = mostrar_menu(pantalla,cola_de_eventos)
    elif ventana_actual == "jugando":
        if bandera_juego == False:
            pygame.mixer.music.load("audios/musica fondo.mp3")
            pygame.mixer.music.set_volume(datos_juego["volumen_musica"] / 100)
            pygame.mixer.music.play(-1)
            bandera_juego = True
        print (bandera_juego)
        ventana_actual =  mostrar_juego(pantalla,cola_de_eventos,datos_juego)
    elif ventana_actual == "game over":
        if bandera_juego == True:
            pygame.mixer.music.stop()
            bandera_juego = False

        ventana_actual = mostrar_game_over(pantalla,cola_de_eventos,datos_juego)
    elif ventana_actual == "ranking":
        ventana_actual = mostrar_ranking(pantalla,cola_de_eventos,datos_juego)
    elif ventana_actual == "ajustes":
        ventana_actual = mostrar_ajustes(pantalla,cola_de_eventos,datos_juego)
    elif ventana_actual == "salir":
        estado_juego = False

    print(bandera_juego)
    pygame.display.flip()
pygame.quit()


