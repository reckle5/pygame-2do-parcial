import pygame
import random
import os
from Constantes import *
import json
from datetime import *



def generar_elemento(textura:str,medidas:tuple,pos:tuple)-> dict:
    elemento = {}
    elemento["superficie"] = pygame.transform.scale(pygame.image.load(textura),medidas)
    elemento["rectangulo"] = pygame.rect.Rect(pos,medidas)
    elemento["rectangulo"].x = pos[0]
    elemento["rectangulo"].y = pos[1]

    return elemento

def mezclar_lista(lista_preguntas: list) -> list:
    lista_mezclada = lista_preguntas.copy()
    random.shuffle(lista_mezclada)
    return lista_mezclada

def obtener_claves(archivo,separador:str) -> list:
    cabecera = archivo.readline()
    cabecera = cabecera.replace("\n","")
    lista_claves = cabecera.split(separador)
    return lista_claves

def obtener_valores(linea,separador:str) -> list:
    linea_aux = linea.replace("\n","")
    lista_valores = linea_aux.split(separador)
    return lista_valores

def crear_diccionario(lista_claves:list,lista_valores:list) -> dict:
    diccionario_aux = {} 
    for i in range(len(lista_claves)):
        diccionario_aux[lista_claves[i]] = lista_valores[i]
        
    return diccionario_aux

def cambiar_tipo_int(lista:list)-> list:
    for dic in lista:
        if "rta_correcta" in dic:
            dic["rta_correcta"] = int(dic["rta_correcta"])
    return lista

def parse_csv(lista_preguntas,nombre_archivo:str) -> bool: 
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo,"r",encoding="utf-8") as archivo:
            lista_claves = obtener_claves(archivo,",")
            for linea in archivo:
                lista_valores = obtener_valores(linea,",")
                diccionario_aux = crear_diccionario(lista_claves,lista_valores) 
                lista_preguntas.append(diccionario_aux)     
                cambiar_tipo_int(lista_preguntas)  
        return True
    else:
        return False
    
def generar_lista_elementos(cda_elementos:int,textura:str,medidas:tuple,pos_x,pos_y,espaciado:int)-> list:
    lista_elementos = []
    for i in range(cda_elementos):
        elemento = generar_elemento(textura,medidas,(pos_x,pos_y))
        lista_elementos.append(elemento)
        pos_y += espaciado
    return lista_elementos

def dibujar_elementos(lista_elementos:list,pantalla) -> bool:
    retorno = False
    if len(lista_elementos) > 0:
        for i in range(len(lista_elementos)):
            pantalla.blit(lista_elementos[i]["superficie"],lista_elementos[i]["rectangulo"])
        retorno = True
    return retorno

def mostrar_texto(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

def dibujar_texto_preguntas(superficie_cuadro,superficie_botones:list,pregunta_actual:list,fuente, color):
    mostrar_texto(superficie_cuadro["superficie"],pregunta_actual["pregunta"],(25,60),fuente,color)

    for i in range(len(superficie_botones)):
        indice_rta = i+1
        mostrar_texto(superficie_botones[i]["superficie"],pregunta_actual[f"rta_{indice_rta}"],(35,12),fuente,color)
        
def dibujar_datos_juego(dato:str,pantalla,pos,fuente,color):
    texto = fuente.render(dato, True, color)
    pantalla.blit(texto,pos)

def iniciar_cronometro(tiempo_inicio:int,duracion:int) -> int:
    
    tiempo_pasado = (pygame.time.get_ticks() - tiempo_inicio) // 1000
    tiempo_restante = max(0, duracion - tiempo_pasado)
    return tiempo_restante

def tiempo_de_juego(cronometro,datos_juego,lista_preguntas:list,preguntas_jugadas:list,caja_pregunta:dict,botones_respuesta:list):
    if cronometro < 1:
        datos_juego["vidas"] -= 1
        datos_juego["indice"] = cambiar_pregunta(lista_preguntas,preguntas_jugadas,caja_pregunta,botones_respuesta,datos_juego)
        pregunta_actual = lista_preguntas[datos_juego["indice"]]
        return pregunta_actual
    return None

def chequear_preguntas_repetidas(preguntas_impresas:list, lista_preguntas:list) -> int:
    random_indice = random.randint(0,len(lista_preguntas)-1)
   
    while random_indice in preguntas_impresas :
        random_indice = random.randint(0,len(lista_preguntas)-1)
    
    return random_indice

def generar_pregunta_actual(lista_preguntas:list,preguntas_jugadas:list) -> int:
    random_indice_pregunta = chequear_preguntas_repetidas(preguntas_jugadas,lista_preguntas)
    preguntas_jugadas.append(random_indice_pregunta)

    return random_indice_pregunta

def limpiar_superficie(elemento_juego:dict,textura:str,medidas:tuple) -> None:
    elemento_juego["superficie"] =  pygame.transform.scale(pygame.image.load(textura),medidas)

def cambiar_pregunta(lista_preguntas:list,preguntas_jugadas:list,caja_pregunta:dict,botones_respuesta:list,datos_juego) -> dict:
    datos_juego["tiempo_inicio"] = pygame.time.get_ticks()
    indice = generar_pregunta_actual(lista_preguntas,preguntas_jugadas)
    limpiar_superficie(caja_pregunta,"texturas/button_menu.png",(ANCHO_PREGUNTA,ALTO_PREGUNTA))

    for i in range(len(botones_respuesta)):
        limpiar_superficie(botones_respuesta[i],"texturas/box1.png",(ANCHO_BOTON,ALTO_BOTON))

    return indice

def obtener_respuesta_click(botones_respuesta:list,pos_click:tuple) -> None | int:
    lista_aux = []
    respuesta = None
    
    for i in range(len(botones_respuesta)):
        lista_aux.append(botones_respuesta[i]["rectangulo"])

    for i in range(len(lista_aux)):
        if lista_aux[i].collidepoint(pos_click):
            respuesta = i + 1

    return respuesta

def verificar_respuesta(datos_juego:dict,pregunta:dict,respuesta:int) -> bool:
    if respuesta == pregunta["rta_correcta"]:
        datos_juego["puntuacion"] += PUNTOS_GANADOS
        datos_juego["preguntas_correctas"] += 1
        verificar_racha_preguntas(datos_juego)
        retorno = True
    else:
        datos_juego["vidas"] -= 1
        if datos_juego["puntuacion"] > 0:
            datos_juego["puntuacion"] -= PUNTOS_PERDIDOS
        else:
            datos_juego["puntuacion"] = 0
        datos_juego["preguntas_correctas"] = 0

        retorno = False
        
    return retorno

def verificar_racha_preguntas(datos_juego):
    if  datos_juego["preguntas_correctas"] == 2:
        datos_juego["vidas"] += 1


def reiniciar_estadisticas(datos_juego:dict) -> None:
    datos_juego["puntuacion"] = 0
    datos_juego["vidas"] = CANTIDAD_VIDAS
    datos_juego["nombre"] = ""
    datos_juego["preguntas_correctas"] = 0


def game_over(pantalla):

    fondo_over = pygame.surface.Surface(PANTALLA)
    fondo_over.fill("Black")

    pantalla.blit(fondo_over, (0,0))

    mostrar_texto(pantalla,"GAME OVER",(250,100),FUENTE_RELOJ,COLOR_BLANCO)
    mostrar_texto(pantalla,"INGRESE SUS INICIALES Y PRESIONE ENTER ..",(150,300),FUENTE_RELOJ,COLOR_BLANCO)

def guardar_ranking(datos_juego):
    
    if os.path.exists("ranking.json"):    
        with open("ranking.json", "r") as file:
            lista_ranking = json.load(file)
    else:
        lista_ranking = []
    dic_ranking = {}
    dic_ranking["nombre"] = datos_juego["nombre"]
    dic_ranking["puntuacion"] = datos_juego["puntuacion"]
    dic_ranking["fecha"] =  date.today().strftime("%d/%m/%Y")

    lista_ranking.append(dic_ranking)

    with open("ranking.json", "w") as file:
        json.dump(lista_ranking, file)

def leer_archivo_json(nombre_archivo:str)->list:
    with open(nombre_archivo, 'r') as archivo:
        datos = json.load(archivo)
    return datos

def ordenar_ranking(lista:list)->list:

    for i in range(0, len(lista)-1):
        for j in range(i+1, len(lista)):
            if (lista[i]["puntuacion"] < lista[j]["puntuacion"]) :   
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux  
    return lista

def mostrar_top_10(lista_ranking:list,pantalla) -> str:
    lista_ordenada = ordenar_ranking(lista_ranking)
    score_y = 150

    for i in range(min(10,len(lista_ranking))):
        texto = f'#{i+1}- {lista_ordenada[i]["nombre"]}: {lista_ordenada[i]["puntuacion"]} pts - {lista_ordenada[i]["fecha"]}'
        mostrar_texto(pantalla,texto,(100,score_y),FUENTE_RELOJ,COLOR_BLANCO)
        score_y += 50

