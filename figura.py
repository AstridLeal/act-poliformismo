import pygame
import random
import math

# Fijamos los colores
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Definimos la clase para el cuadrado
class Cuadrado():
    def __init__(self, window, maxWidth, maxHeight):
        self.window = window
        self.widthAndHeight = random.randrange(10, 100)
        self.color = random.choice((ROJO, VERDE, AZUL))
        self.x = random.randrange(1, maxWidth - self.widthAndHeight)
        self.y = random.randrange(1, maxHeight - self.widthAndHeight)
        self.rect = pygame.Rect(self.x, self.y, self.widthAndHeight, self.widthAndHeight)
        self.shapeType = 'cuadrado'

    def clickedInside(self, mousePoint):
        return self.rect.collidepoint(mousePoint)

    def obtenerTipo(self):
        return self.shapeType

    def obtenerArea(self):
        return self.widthAndHeight * self.widthAndHeight

    def draw(self):
        pygame.draw.rect(self.window, self.color, self.rect)

# Definimos la clase para el círculo
class Circulo():
    def __init__(self, window, maxWidth, maxHeight):
        self.window = window
        self.color = random.choice((ROJO, VERDE, AZUL))
        self.radio = random.randrange(10, 50)
        self.x = random.randrange(1, maxWidth - self.radio * 2)
        self.y = random.randrange(1, maxHeight - self.radio * 2)
        self.centroX = self.x + self.radio
        self.centroY = self.y + self.radio
        self.rect = pygame.Rect(self.x, self.y, self.radio * 2, self.radio * 2)
        self.shapeType = 'círculo'

    def clickedInside(self, mousePoint):
        distancia = math.sqrt((mousePoint[0] - self.centroX) ** 2 + (mousePoint[1] - self.centroY) ** 2)
        return distancia <= self.radio

    def obtenerTipo(self):
        return self.shapeType

    def obtenerArea(self):
        return math.pi * (self.radio ** 2)

    def draw(self):
        pygame.draw.circle(self.window, self.color, (self.centroX, self.centroY), self.radio)

# Definimos la clase para el triángulo
class Triangulo():
    def __init__(self, window, maxWidth, maxHeight):
        self.window = window
        self.width = random.randrange(10, 100)
        self.height = random.randrange(10, 100)
        self.color = random.choice((ROJO, VERDE, AZUL))
        self.x = random.randrange(1, maxWidth - self.width)
        self.y = random.randrange(1, maxHeight - self.height)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.shapeType = 'triángulo'

    def clickedInside(self, mousePoint):
        inRect = self.rect.collidepoint(mousePoint)
        if not inRect:
            return False
        # Hacemos algunas cuentas para ver si el punto está adentro del triángulo
        xOffset = mousePoint[0] - self.x
        yOffset = mousePoint[1] - self.y
        # Verifica si el punto está dentro del triángulo con respecto a su base y altura
        return (0 <= xOffset <= self.width) and (0 <= yOffset <= self.height)

    def obtenerTipo(self):
        return self.shapeType

    def obtenerArea(self):
        return 0.5 * self.width * self.height

    def draw(self):
        pygame.draw.polygon(self.window, self.color, ((self.x, self.y + self.height), (self.x, self.y), (self.x + self.width, self.y)))