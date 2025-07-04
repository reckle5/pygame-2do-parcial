import pygame
pygame.init()
#setting
PANTALLA = (680,720)
FPS = 30

#texturas
FONDO_JUEGO = pygame.transform.scale(pygame.image.load("texturas/fondo_juego.jpg"),PANTALLA)
FONDO_MENU = pygame.transform.scale(pygame.image.load("texturas/fondo_menu.jpg"),PANTALLA)


ANCHO_PREGUNTA,ALTO_PREGUNTA = (450,230)
PREGUNTA_X,PREGUNTA_Y = (135,130)
ANCHO_BOTON,ALTO_BOTON = (250,50)
BOTON_X,BOTON_Y = (220,320)
RTA_X,RTA_Y = (230,390)
ANCHO_BOTON_ATRAS,ALTO_BOTON_ATRAS = (120,40)
ATRAS_X,ATRAS_Y = (20,670)



#jugabilidad
VIDAS = 3
CANTIDAD_VIDAS = 3
TIEMPO_RESTANTE = 30
PUNTOS_GANADOS = 100
PUNTOS_PERDIDOS = 25
CRONOMETRO = 30

#colores
COLOR_BLANCO = (255,255,255)
COLOR_NEGRO = (0,0,0)
COLOR_VERDE = (0,255,0)
COLOR_ROJO = (255,0,0)
COLOR_AZUL = (0,0,255)
COLOR_VIOLETA = (134,23,219)
COLOR_LILA = (200, 162, 200)
COLOR_VERDE_CLARO = (144, 238, 144)

#fuentes
FUENTE_TEXTO = pygame.font.SysFont("CAMBRIA",28,True)
FUENTE_TITULO = pygame.font.SysFont("Segoe UI Black",60,True)
FUENTE_DATOS = pygame.font.SysFont("arial black",30,True)
FUENTE_MENU = pygame.font.SysFont("Bahnschrift",30,True)
FUENTE_TITULO2 = pygame.font.SysFont("Segoe UI Black",59,True)
FUENTE_AJUSTE = pygame.font.SysFont("CAMBRIA",40,True)

#Segoe UI Semibold / Segoe UI Black
FUENTE_RELOJ = pygame.font.Font("DS-DIGI.TTF", 40)

#SONIDOS
CLICK_SONIDO = pygame.mixer.Sound("audios/click1.ogg")
ERROR_SONIDO = pygame.mixer.Sound("audios/error.mp3")
MUSICA_FONDO = pygame.mixer.music.load("audios/musica fondo.mp3")
