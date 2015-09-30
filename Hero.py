__author__ = 'JOSHUA'

import pygame
import math

from GameEntity import *
from Settings import *

class Hero(GameEntity):
    
    def __init__(self, world, image):

        GameEntity.__init__(self, world, "Hero", image)
        self.settings = Settings()

    def process(self, time_passed):
        self.brain.think()

    def render(self, surface):

        if not self.world.camera.isWithinActiveArea(self):
            x, y = self.location
            true_x, true_y = ((self.world.camera.x + self.settings.SCREEN_WIDTH) - x), ((self.world.camera.y + self.settings.SCREEN_HEIGHT) - y)
            w, h = self.image.get_size()
            surface.blit(self.image, (true_x-w/2, true_y-h/2))

    def rotatewithcursor(self, crs_position):

        angle = 360-math.atan2(crs_position[1]-300, crs_position[0]-400)*180/math.pi
        rotimage = pygame.transform.rotate(self.image, angle)
        self.image = rotimage





