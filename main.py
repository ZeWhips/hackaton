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
currentniveau = m.niv1

#pos init

while(interaction._running):
    clock.tick(25)
    #charge la touche rentrée sur le clavier (interactions)
    interaction.process_event()
    player.state(position, interaction._direction, currentniveau)
    
    #methode du joueur(touche clavier) renvoie une nouvelle map
    position = player.move_player()

    currentniveau = player.getMap()
    h, w = m.get_size(currentniveau)
    
    m.showMap(currentniveau, screen)

    interaction._direction = None
    #display new map
    pg.display.update()

pg.quit()
