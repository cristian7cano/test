import pygame,sys
import os
from pygame.locals import *
from random import randint
##############################################################
##################                          ##################
################## JUEGO SUPERAR OBSTACULOS ##################
##################                          ##################
##############################################################
os.environ['SDL_VIDEO_CENTERED'] = '1' # CENTRADO EN LA PANTALLA #

## VARIABLES GLOBALES ##

tamX, tamY = 600,800
fondo = (255,255,255)
color_circulo = (1,1,255)
listaObstaculos = []
posicion = [0, 225, 450]
enJuego = True
arriba = True

class Jugador (pygame.sprite.Sprite):
    # Clase para el Jugador #

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.ImagenJugador = pygame.image.load(r'C:\Users\cristian\Desktop\programasio\Imagenes\CirculoJugador.png')
        self.rect = self.ImagenJugador.get_rect()
        self.rect.centerx = tamX/2
        self.rect.centery = tamY-70
        self.posAceptada = 2
        self.velocidad = 150
        #circulo = pygame.draw.circle(ventana, color_circulo, (int(posX), int(posY)), 50)

    def mover(self):
        pass

    def dibujar(self, superficie):
        superficie.blit(self.ImagenJugador,self.rect)

class Obstaculo (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagenObstaculo = pygame.image.load(r'C:\Users\cristian\Desktop\programasio\Imagenes\Obstaculo.png')
        self.rect = self.imagenObstaculo.get_rect()
        self.velocidadMov = 5
        self.rect.top = 10 
        random = randint(0,2)
        self.rect.left = posicion[random]
        self.contador = 0
    
    def movimiento(self):
        self.rect.top += self.velocidadMov

    def golpeado(self, jugador):
        
        if self.rect.colliderect(jugador):
            return True
        else:
            
            return False
    
    def velocidad(self,contador):
        self.velocidadMov += contador
        print("Mi velocidad"+str(self.velocidadMov))

    def dibujar(self, superficie):
       superficie.blit(self.imagenObstaculo,self.rect)

def Juego():
    enJuego = True
    pygame.init() # INIT PYGAME
    pygame.display.set_caption("Juego de Obstaculos") # TITULO #
    ventana = pygame.display.set_mode((tamX,tamY)) # TAMAÑO VENTANA #
    jugador = Jugador()
    obs = Obstaculo()
    
    contador = 0
    reloj = pygame.time.Clock()
    fuente = pygame.font.SysFont("Arial",30)
    Texto = fuente.render("Puntuacion: " + str(contador), 0, (120,120,120))
    
    while True:
        reloj.tick(60)
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if enJuego == True:
                if evento.type == KEYDOWN:
                    if evento.key == K_LEFT:
                        if jugador.posAceptada >1:
                            jugador.rect.left -= jugador.velocidad
                            jugador.posAceptada -=1
                    elif evento.key == K_RIGHT:
                        if jugador.posAceptada <3:
                            jugador.rect.right += jugador.velocidad
                            jugador.posAceptada +=1
        ventana.fill(fondo)
        jugador.dibujar(ventana)
        if obs.golpeado(jugador) == True:
                    enJuego = False
                    
        if enJuego == True:
            if obs.rect.top < 800:
              obs.movimiento()
              obs.dibujar(ventana)
              ventana.blit(Texto,(100,100))
            else:
                contador +=1
                obs = Obstaculo()
                obs.velocidad(contador)
                print(contador)
                print(obs.rect.left)
                Texto = fuente.render("Puntuacion: " + str(contador), 0, (120,120,120))
                ventana.blit(Texto,(100,100))
        else:
            TextoFin = fuente.render("Fin del Juego. Puntuacion: " + str(contador), 0, (120,120,120))
            ventana.blit(TextoFin,(150,150))

        pygame.display.update()

Juego()



    
