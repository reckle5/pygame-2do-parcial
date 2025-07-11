import pygame
from Constantes import *
from elementos_de_juego import *
from Funciones import*

def mostrar_popup_comodines(pantalla,lista_comodines,datos_juego):
    sombra = pygame.Surface((680,720))
    sombra.set_alpha(128)  # Nivel de transparencia
    sombra.fill(COLOR_NEGRO)
    pantalla.blit(sombra, (0, 0))

    popup_rect = pygame.Rect(100, 130, 550, 230)
    pygame.draw.rect(pantalla, COLOR_ANARANJADO, popup_rect, border_radius=10)
    pygame.draw.rect(pantalla, COLOR_NEGRO, popup_rect, 2, border_radius=10)
    dibujar_datos_juego("¡¡ Elige un comodín !!",pantalla,(popup_rect.x + 120, popup_rect.y + 15),FUENTE_MENU,COLOR_NEGRO)
    monstrar_comodines_no_usados(lista_comodines,pantalla,datos_juego)

        



def activar_comodin(comodin_elegido:int,pantalla,lista_preguntas,preguntas_jugadas,cuadro_pregunta,cuadros_rta,datos_juego):
    match comodin_elegido:
        case 1:
            if comodin_elegido in datos_juego["comodines_usados"]:
                dibujar_datos_juego("Este comodin ya fue usado, elige otro!",pantalla,(120,325),FUENTE_COMODIN,COLOR_NEGRO)
                datos_juego["comodin"] = None
            else:
                dibujar_datos_juego("Elegiste el comodín BOMBA!",pantalla,(120,325),FUENTE_COMODIN,COLOR_NEGRO)
                desactivar_comodines(lista_comodines,comodin_elegido,pantalla)
                activar_bomba(lista_preguntas[datos_juego["indice"]],pantalla,datos_juego,cuadros_rta)
                datos_juego["comodines_usados"] += [1]
        case 2:
            if comodin_elegido in datos_juego["comodines_usados"]:
                dibujar_datos_juego("Este comodin ya fue usado, elige otro!",pantalla,(120,325),FUENTE_COMODIN,COLOR_NEGRO)
                datos_juego["comodin"] = None
            else:
                dibujar_datos_juego("Elegiste el comodín X2!",pantalla,(120,325),FUENTE_COMODIN,COLOR_NEGRO)
                datos_juego["x2_activo"] = True
                datos_juego["comodines_usados"] += [2]
        case 3:
            if comodin_elegido in datos_juego["comodines_usados"]:
                dibujar_datos_juego("Este comodin ya fue usado, elige otro!",pantalla,(120,325),FUENTE_COMODIN,COLOR_NEGRO)
            else:
                dibujar_datos_juego("Elegiste el comodín DOBLE CHANCE!",pantalla,(120,325),FUENTE_COMODIN,COLOR_NEGRO)
                datos_juego["doble_chance"] = True
                datos_juego["comodines_usados"] += [3]
        case 4:
            if comodin_elegido in datos_juego["comodines_usados"]:
                dibujar_datos_juego("Este comodin ya fue usado, elige otro!",pantalla,(120,325),FUENTE_COMODIN,COLOR_NEGRO)
            else:
                dibujar_datos_juego("Elegiste el comodín PASAR PREGUNTA!",pantalla,(120,325),FUENTE_COMODIN,COLOR_NEGRO)
                activar_pasar_pregunta(lista_preguntas,preguntas_jugadas,cuadro_pregunta,cuadros_rta,datos_juego)
                datos_juego["comodines_usados"] += [4]

            


    