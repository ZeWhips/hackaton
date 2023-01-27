import pygame as pg

class Intercations:

    def __init__(self, map):
        '''direction corresponds to the last input of the player,
        map is a numpy array
        player is the instance of the class Player'''
        self._direction = None
        self._running = True
        self._map = map


    def process_event(self):
        '''Detecting actions
        To close window or move the player'''

        for event in pg.event.get():

            if event.type == pg.QUIT:
                self._running = False 
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    self._running = False

                #detect the new direction    
                elif event.key == pg.K_UP :
                    self._direction = 'up'
                elif event.key == pg.K_DOWN :
                    self._direction = 'down'
                elif event.key == pg.K_LEFT :
                    self._direction = 'left'
                elif event.key == pg.K_RIGHT :
                    self._direction = 'right'

        
    def wall_collision(self, player):
        '''True if the player hits a wall'''
        x, y = player.getPos()
        return self._map[x][y] == 1


    def pick_object(self, player, coin, potion):
        x, y = player.getPos()
        if (x, y) == (coin._x, coin._y):
            message = coin._message
        elif (x, y) == (potion._x, potion._y):
            message = potion._message
        return message 

    