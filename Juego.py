import pygame
from Constantes import *
from Funciones import *
from elementos_de_juego import *

pygame.init

lista_preguntas = []
preguntas_jugadas = [0]

parse_csv(lista_preguntas,"preguntas.csv")

pantalla = pygame.display.set_mode(PANTALLA)
reloj = pygame.time.Clock()

estado_juego = True

def mostrar_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego):
    print(preguntas_jugadas)
    retorno = "jugando"
    tiempo_reloj = iniciar_cronometro(datos_juego["tiempo_inicio"],CRONOMETRO)
    pregunta_actual = lista_preguntas[datos_juego["indice"]]  
    
    if datos_juego["vidas"] == 0:
        preguntas_jugadas[:] = [0]
        retorno = "game over"

    for evento in cola_eventos:
        #Actualizaciones
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                CLICK_SONIDO.play()
                respuesta = obtener_respuesta_click(cuadros_rta,evento.pos)
                if respuesta != None:
                    if verificar_respuesta(datos_juego,lista_preguntas[datos_juego["indice"]],respuesta):
                        cuadros_rta[respuesta-1]["superficie"].fill(COLOR_VERDE)
                        pantalla.blit(cuadros_rta[respuesta - 1]["superficie"], cuadros_rta[respuesta - 1]["rectangulo"])

                        pygame.display.flip()  # Fuerza la actualización de pantalla
                        pygame.time.delay(1000)
                        tiempo_reloj = iniciar_cronometro(datos_juego["tiempo_inicio"],CRONOMETRO)                   
                        print("acierto")
                    else:
                        ERROR_SONIDO.play()
                        print("fracaso")
                        
                    datos_juego["indice"]  = cambiar_pregunta(lista_preguntas,preguntas_jugadas,cuadro_pregunta,cuadros_rta,datos_juego)
                    pregunta_actual = lista_preguntas[datos_juego["indice"]]
                if boton_atras["rectangulo"].collidepoint(evento.pos):
                    preguntas_jugadas[:] = [0]
                    reiniciar_estadisticas(datos_juego)
                    retorno = "menu"

    pregunta_nueva = tiempo_de_juego(tiempo_reloj,datos_juego,lista_preguntas,preguntas_jugadas,cuadro_pregunta,cuadros_rta)

    if pregunta_nueva is not None:
        pregunta_actual = pregunta_nueva

                
    pantalla.blit(FONDO_JUEGO,(0,0))
    dibujar_elementos(lista_elementos_de_juego,pantalla)
    dibujar_texto_preguntas(cuadro_pregunta,cuadros_rta,pregunta_actual,FUENTE_TEXTO,COLOR_NEGRO)
    dibujar_datos_juego(f"Atras",boton_atras["superficie"],(12,5),FUENTE_TEXTO,COLOR_NEGRO)
    dibujar_datos_juego(f"PUNTUACION: {datos_juego["puntuacion"]}",pantalla,(10,10),FUENTE_RELOJ,COLOR_NEGRO)
    dibujar_datos_juego(F"VIDAS: {datos_juego["vidas"]}",pantalla,(10,60),FUENTE_RELOJ,COLOR_NEGRO)
    dibujar_datos_juego(str(tiempo_reloj),pantalla,(600,30),FUENTE_RELOJ,COLOR_NEGRO)

    return retorno