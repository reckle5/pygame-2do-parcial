import pygame
from Constantes import *
from Funciones import *
from elementos_de_juego import *
pygame.key.start_text_input()

def concatenar_nueva_pregunta(datos_pregunta):
    pregunta_csv = (
        datos_pregunta["nueva_pregunta"] + "," +
        datos_pregunta["rta_1"] + "," +
        datos_pregunta["rta_2"] + "," +
        datos_pregunta["rta_3"] + "," +
        datos_pregunta["rta_4"] + "," +
        datos_pregunta["rta_correcta"] + "\n")
    return pregunta_csv

def mostrar_agregar_preguntas(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_preguntas_nueva,archivo_csv) -> str:
    retorno = "agregar preguntas"

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
               # if boton_atras["rectangulo"].collidepoint(evento.pos):
                #    retorno = "menu"
                if boton_pregunta["rectangulo"].collidepoint(evento.pos):
                    datos_preguntas_nueva["escribir_pregunta"] = True
                for i in range(len(lista_botones_preg)):
                    if lista_botones_preg[i]["rectangulo"].collidepoint(evento.pos):
                        datos_preguntas_nueva["campo"] = i   
                #if boton_guardar["rectangulo"].collidepoint(evento.pos):
                #    concatenar_nueva_pregunta(datos_preguntas_nueva)
                #    with open("preguntas.csv", "a", encoding="utf-8") as archivo:
                #        archivo.write(archivo_csv)          
        elif evento.type == pygame.TEXTINPUT:
            if datos_preguntas_nueva["escribir_pregunta"]:
                datos_preguntas_nueva["nueva_pregunta"] += evento.text
            elif datos_preguntas_nueva["campo"] == 0:
                datos_preguntas_nueva["rta_1"] += evento.text
            elif datos_preguntas_nueva["campo"] == 1:
                datos_preguntas_nueva["rta_2"] += evento.text
            elif datos_preguntas_nueva["campo"] == 2:
                datos_preguntas_nueva["rta_3"] += evento.text
            elif datos_preguntas_nueva["campo"] == 3:
                datos_preguntas_nueva["rta_4"] += evento.text
            elif datos_preguntas_nueva["campo"] == 4:
                if evento.text in "1234":
                    datos_preguntas_nueva["rta_correcta"] = evento.text

        elif evento.type == pygame.KEYDOWN :
            if evento.key == pygame.K_RETURN: 
                datos_preguntas_nueva["escribir_pregunta"] = False 
            
    pantalla.fill(COLOR_LILA)

    dibujar_elementos([boton_pregunta, boton_atras,boton_guardar], pantalla)
    dibujar_elementos(lista_botones_preg, pantalla)


    mostrar_texto(boton_pregunta["superficie"], datos_preguntas_nueva["nueva_pregunta"],(90,70),FUENTE_COMODIN,COLOR_NEGRO)
    mostrar_texto(lista_botones_preg[0]["superficie"], datos_preguntas_nueva["rta_1"],(210,30),FUENTE_COMODIN,COLOR_NEGRO)
    mostrar_texto(lista_botones_preg[1]["superficie"], datos_preguntas_nueva["rta_2"],(210,30),FUENTE_COMODIN,COLOR_NEGRO)
    mostrar_texto(lista_botones_preg[2]["superficie"], datos_preguntas_nueva["rta_3"],(210,30),FUENTE_COMODIN,COLOR_NEGRO)
    mostrar_texto(lista_botones_preg[3]["superficie"], datos_preguntas_nueva["rta_4"],(210,30),FUENTE_COMODIN,COLOR_NEGRO)
    mostrar_texto(lista_botones_preg[4]["superficie"], datos_preguntas_nueva["rta_correcta"],(210,30),FUENTE_COMODIN,COLOR_NEGRO)
    
    
    mostrar_texto(boton_pregunta["superficie"],"AGREGAR PREGUNTA AL JUEGO",(80,30),FUENTE_MENU,COLOR_NEGRO)
    mostrar_texto(lista_botones_preg[0]["superficie"],"Opcion 1",(20,17),FUENTE_MENU,COLOR_NEGRO)
    mostrar_texto(lista_botones_preg[1]["superficie"],"Opcion 2",(20,17),FUENTE_MENU,COLOR_NEGRO)
    mostrar_texto(lista_botones_preg[2]["superficie"],"Opcion 3",(20,17),FUENTE_MENU,COLOR_NEGRO)
    mostrar_texto(lista_botones_preg[3]["superficie"],"Opcion 4",(20,17),FUENTE_MENU,COLOR_NEGRO)
    mostrar_texto(lista_botones_preg[4]["superficie"],"Op. correcta",(20,17),FUENTE_MENU,COLOR_NEGRO)

    dibujar_datos_juego("Atras",boton_atras["superficie"],(12,5),FUENTE_TEXTO,COLOR_NEGRO)
    dibujar_datos_juego("Guardar",boton_guardar["superficie"],(12,5),FUENTE_TEXTO,COLOR_VERDE)


    

    pygame.display.flip()
    return retorno