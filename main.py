import pygame
import sys
import random
from figura import Cuadrado, Circulo, Triangulo

# Declaramos las constantes
BLANCO = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
CUADROS_POR_SEGUNDO = 30
N_FIGURAS = 10

# Fijamos la ventana
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
clock = pygame.time.Clock()

# Crear lista de figuras
listaDeFiguras = []
tuplaClasesDeFiguras = (Cuadrado, Circulo, Triangulo)

for i in range(N_FIGURAS):
    claseEscogidaAlAzar = random.choice(tuplaClasesDeFiguras)
    oFigura = claseEscogidaAlAzar(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    listaDeFiguras.append(oFigura)

# Crear el texto de estado
font = pygame.font.SysFont(None, 28)
oStatusLine = font.render('Presiona sobre las figuras', True, (0, 0, 0))

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Invertimos el orden para revisar primero la última figura dibujada
            for oFigura in reversed(listaDeFiguras):
                if oFigura.clickedInside(event.pos):
                    area = oFigura.obtenerArea()
                    elTipo = oFigura.obtenerTipo()
                    nuevoTexto = f'Presionaste sobre un {elTipo} cuya área es {area:.2f}'
                    oStatusLine = font.render(nuevoTexto, True, (0, 0, 0))
                    break # Solo trata con la figura de hasta arriba.

    # Le decimos a cada figura que se dibuje
    window.fill(BLANCO)
    for oFigura in listaDeFiguras:
        oFigura.draw()
    
    # Dibujar el texto de estado
    window.blit(oStatusLine, (4, 4))
    
    pygame.display.update()
    clock.tick(CUADROS_POR_SEGUNDO)
