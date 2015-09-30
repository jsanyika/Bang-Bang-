__author__ = 'JOSHUA'

import pygame

from Camera import *
from Settings import *


class World(object):

    def __init__(self):
        settings = Settings()
        self.entities = {}
        self.entity_id = 0
        self.background = pygame.surface.Surface(settings.WORLD_SIZE).convert()
        self.background.fill((255, 255, 255))

    def add_entity(self, entity):

        self.entities[self.entity_id] = entity
        entity.id = self.entity_id
        self.entity_id += 1

    def remove_entity(self, entity):

        del self.entities[entity.id]

    def get(self, entity_id):

        if entity_id in self.entities:
            return self.entities[entity_id]
        else:
            return None

    def process(self, time_passed):
        time_passed_seconds = time_passed / 1000.0
        for entity in self.entities.itervalues():
            entity.process(time_passed_seconds)

    def render(self, surface):

        surface.blit(self.background, (0,0))
        for entity in self.entities.values():
            entity.render(surface)

    def add_camera(self, camera):
        self.camera = camera