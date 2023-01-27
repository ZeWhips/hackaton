import pygame as pg 
from map import Map
from assets import Assets


m = Map()

def start():

    pg.init()
    
    clock = pg.time.Clock()
    h, w = m.get_size(m.niv1)
    screen = pg.display.set_mode((h, w))

    return screen, clock

screen, clock = start()
m.showMap(m.niv1, screen)

while 1:
    clock.tick(10)
    pg.display.update()

