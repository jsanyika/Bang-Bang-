__author__ = 'JOSHUA'
from gameobjects.vector2 import Vector2
from StateMachine import *


class GameEntity(object):

        def __init__(self, world, name, image):

            self.world = world
            self.name = name
            self.image = image
            self.location = Vector2(0,0)
            self.destination = Vector2(0,0)
            self.speed = 0.
            self.brain = StateMachine()

        def process(self, time_passed):

            self.brain.think()

            if self.speed > 0. and self.location != self.destination:

                vec_to_destination = self.destination - self.location
                distance_to_destination = vec_to_destination.get_length()
                heading = vec_to_destination.get_normalized()
                travel_distance = min(distance_to_destination, time_passed * self.speed)
                self.location += travel_distance * heading
