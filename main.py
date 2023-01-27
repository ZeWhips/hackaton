from interactions import Interactions
import player
import pygame as pg 
from map import Map
from assets import Assets

interaction = Interactions()
position = [1,1]
player = player.Player(position)
running = interaction._running

#start
m = Map()
pg.init()
clock = pg.time.Clock()
h, w = m.get_size(m.niv1)
screen = pg.display.set_mode((h, w))
m.showMap(m.niv1, screen)

#pos init

while(interaction._running):
    clock.tick(1)
    #charge la touche rentrée sur le clavier (interactions)
    interaction.process_event()
    direction = interaction._direction
    player.state(position, direction, m.niv1)
    #methode du joueur(touche clavier) renvoie une nouvelle map
    position = player.move_player()
    m.niv1 = player.getMap

    #display new map
    pg.display.update()

pg.quit()
