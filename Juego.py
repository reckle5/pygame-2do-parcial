import pygame
from Constantes import *
from Funciones import *
from elementos_de_juego import *
from comodines import *
pygame.init

lista_preguntas = []
preguntas_jugadas = [0]

parse_csv(lista_preguntas,"preguntas.csv")

pantalla = pygame.display.set_mode(PANTALLA)
reloj = pygame.time.Clock()

estado_juego = True

def mostrar_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego):

    retorno = "jugando"

    tiempo_reloj = iniciar_cronometro(datos_juego["tiempo_inicio"],CRONOMETRO)
    pregunta_actual = lista_preguntas[datos_juego["indice"]]  
   
    
    if datos_juego["vidas"] == 0:
        preguntas_jugadas[:] = [0]
        retorno = "game over"

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                CLICK_SONIDO.play()
                
                respuesta = obtener_respuesta_click(cuadros_rta,evento.pos) #respuesta de que opcion eligio para responder las preguntas
                rta_otros_botones = obtener_respuesta_click(botones_extra_juego,evento.pos) #respuesta de si toco el boton de atra o del comodin
                comodin = obtener_respuesta_click(lista_comodines,evento.pos) #respuesta de que comodin eligio

                if rta_otros_botones != None:
                    if rta_otros_botones == 1:  
                        datos_juego["comodin"] = None

                        datos_juego["popup_comodin"] = True  #se activa ventana popup de comodines
                    elif rta_otros_botones == 2:
                        preguntas_jugadas[:] = [0]
                        reiniciar_estadisticas(datos_juego)
                        retorno = "menu"  #se vuelve al menu y se reinician las estadisticas de juego

                if datos_juego["popup_comodin"] == False:
                        if respuesta != None:
                            verificar_rta = verificar_respuesta(datos_juego,lista_preguntas[datos_juego["indice"]],respuesta,pantalla,cuadros_rta)
                            
                            if verificar_rta:
                                activar_x2(datos_juego)
                                colorear_respuesta(pantalla,cuadros_rta,respuesta,COLOR_VERDE_CLARO)
                                generar_delay(1000) #delay para mostrar la opcion correcta coloreada
                                tiempo_reloj = iniciar_cronometro(datos_juego["tiempo_inicio"],CRONOMETRO)                   
                            elif verificar_rta == False:
                                colorear_respuesta(pantalla,cuadros_rta,respuesta,COLOR_ROJO)
                                ERROR_SONIDO.play()
                                generar_delay(1000) 
                            
                            if verificar_rta != None: # si verificar_rta nos devulve none es porque hay algun comodin activo, por ende no pasa de pregunta, si da distinto a none pasa de pregunta. 
                                datos_juego["indice"]  = cambiar_pregunta(lista_preguntas,preguntas_jugadas,cuadro_pregunta,cuadros_rta,datos_juego)
                                pregunta_actual = lista_preguntas[datos_juego["indice"]]
                                datos_juego["rta_inhabilitadas"][:] = []
                else:
                    if comodin != None:
                        datos_juego["comodin"] = comodin
                        activar_comodin(comodin,pantalla,lista_preguntas,preguntas_jugadas,cuadro_pregunta,cuadros_rta,datos_juego)
                        generar_delay(2500)
                        pregunta_actual = lista_preguntas[datos_juego["indice"]]
                        datos_juego["popup_comodin"] = False

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
    print(datos_juego["doble_chance"])
    print(f"c usados : {datos_juego["comodines_usados"]}")
    if datos_juego["popup_comodin"] and datos_juego["comodin"] == None:
        mostrar_popup_comodines(pantalla,lista_comodines,datos_juego)
    
    print(f"inah: {datos_juego["rta_inhabilitadas"]}")
    pygame.display.flip()
    return retorno