import pygame, sys
from pygame.locals import *

from World import *
from Camera import *
from GameEntity import *
from Hero import *
from Settings import *

def run():

    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(settings.SCREEN_SIZE, 0, 32)

    world = World()

    w, h = settings.WORLD_SIZE

    camera = Camera(0, 0)

    world.add_camera(camera)

    clock = pygame.time.Clock()

    hero_img = pygame.image.load("pictures\Top_Down_Survivor_2\Top_Down_Survivor/flashlight\idle\survivor-idle_flashlight_0.png").convert_alpha()
    hero = Hero(world, hero_img)
    world.add_entity(hero)

    Move_Left = False
    Move_Right = False
    Move_Down = False
    Move_Up = False

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    Move_Down = True
                    Move_Up = False
                elif event.key == K_LEFT:
                    Move_Right = True
                    Move_Left = False
                elif event.key == K_RIGHT:
                    Move_Left = True
                    Move_Right = False
                elif event.key == K_DOWN:
                    Move_Up = True
                    Move_Down = False

            elif event.type == KEYUP:
                if event.key == K_UP:
                    Move_Down = False
                elif event.key == K_LEFT:
                    Move_Right = False
                elif event.key == K_RIGHT:
                    Move_Left = False
                elif event.key == K_DOWN:
                    Move_Up = False

            #elif event.type == MOUSEMOTION:
                #pos = pygame.mouse.get_pos()
                #hero.rotatewithcursor(pos)

        camera.moveCamera(Move_Left, Move_Right, Move_Up, Move_Down)

        time_passed = clock.tick(30)

        world.process(time_passed)
        world.render(screen)

        pygame.display.update()

if __name__ == "__main__":
    run()
