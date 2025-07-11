import pygame
from Constantes import *
from Funciones import *
from Menu import *
from Juego import *
from Game_over import *
from Rankings import *
from Config import *
from Agregar_preguntas import *

pygame.init()
pygame.mixer.init()

pygame.display.set_caption("PREGUNTADOS")
icono = pygame.image.load("texturas/icono.png")
pygame.display.set_icon(icono)

pantalla = pygame.display.set_mode(PANTALLA)

reloj = pygame.time.Clock()
estado_juego = True
ventana_actual= "menu" 
bandera_juego = False

datos_juego = {"puntuacion":0,
               "vidas":CANTIDAD_VIDAS,
               "nombre":"",
               "error_nombre":False,
               "tiempo":TIEMPO_RESTANTE,
               "indice":0,
               "preguntas_correctas":0,
               "tiempo_inicio":pygame.time.get_ticks(),
               "volumen_musica":0,
               "popup_comodin":False,
               "comodin":None,
               "x2_activo":False,
               "doble_chance":False,
               "rta_inhabilitadas":[],
               "comodines_usados": [],
                }

datos_preguntas_nueva = {"nueva_pregunta":"",
                        "escribir_preg":False,
                        "campo":None,
                        "rta_1": "",
                        "rta_2": "",
                        "rta_3": "",
                        "rta_4": "",
                        "rta_correcta": "",
                        "guardar_cambios":False}
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
    elif ventana_actual == "agregar preguntas":
        ventana_actual = mostrar_agregar_preguntas(pantalla, cola_de_eventos, datos_preguntas_nueva,"preguntas.csv")
    elif ventana_actual == "salir":
        estado_juego = False

    pygame.display.flip()
pygame.quit()


