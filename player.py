class Player:

    def __init__(self, position):
      
        self._pos = position 

    def state(self, position, direction, map):
        self._map = map
        self._pos = position 
        self._direction = direction

    def getPos(self):
        return self._pos

    def getDirection(self):
        return self._direction

    def getMap(self):
        return self._map
   
    def move_player(self):
        head = self.getPos()
        map = self.getMap()
        x, y = head[0], head[1]
        direction = self.getDirection()
        if direction == 'left':
            if 0 < map[x][y-1] < 10:
                print ("rencontre un mur ")
            else:
                map[x][y] = 0
                x, y = x, y-1
                map[x][y] = 20
        elif direction == 'right' :
            if 0 < map[x][y+1] < 10:
                print("rencontre un mur ")
            else:
                map[x][y] = 0
                x, y = x, y+1
                map[x][y] = 20
        elif direction == 'up' :
            if 0 < map[x-1][y] < 10:
                print("rencontre un mur ")
            else:
                map[x][y] = 0
                x, y = x-1, y
                map[x][y] = 20
        elif direction == 'down' :
            if (0 < map[x+1][y]< 10):
                print("rencontre un mur ")
            else:
                map[x][y] = 0
                x, y = x+1, y
                map[x][y] = 20
        return [x, y]
    


    def collect_coin(self):
        '''To call after moving the player and before displaying'''
        x, y = self.getPos()
        if self._map[x][y] == 10: #Coin
            self._capital += 1
            message = 'You got a coin and win 1 point of capital'
        return message


    def fall_in_trap(self):
        '''To call after moving the player and before displaying'''
        x, y = self.getPos()
        if self._map[x][y] == 12: #Trap
            self._capital += -2
            message = 'You fell in a trap and lose 2 points of capital'
        return message


    def collect_potion(self):
        '''To call after moving the player and before displaying'''
        x, y = self.getPos()
        if self._map[x][y] == 11: #Potion
            self._capital += 3
            message = 'You got a magic potion and win 3 points of capital'
        return message


    def death(self, running):
        if self._capital < 0:
            running = False
