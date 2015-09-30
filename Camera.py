from Settings import *
import pygame, sys
from pygame.locals import *

class Camera(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.settings = Settings()

    def moveCamera(self, moveLeft, moveRight, moveUp, moveDown):

        if moveLeft:
            self.x -= self.settings.MOVERATE
        if moveRight:
            self.x += self.settings.MOVERATE
        if moveUp:
            self.y -= self.settings.MOVERATE
        if moveDown:
            self.y += self.settings.MOVERATE

    def isWithinActiveArea(self, entity):
        boundsLeftEdge = self.x - self.settings.SCREEN_WIDTH
        boundsTopEdge = self.y - self.settings.SCREEN_HEIGHT
        entity_x, entity_y = entity.location
        entity_w, entity_h = entity.image.get_size()
        boundsRect = pygame.Rect(boundsLeftEdge, boundsTopEdge, self.settings.SCREEN_WIDTH * 3, self.settings.SCREEN_HEIGHT * 3)
        objRect = pygame.Rect(entity_x, entity_y, entity_w, entity_h)
        return not boundsRect.colliderect(objRect)