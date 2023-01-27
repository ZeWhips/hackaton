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
        if direction == 'up':
            if 0 < map[x][y-1] < 10:
                print ("rencontre un mur ")
            else: 
                x, y = x, y-1
                map[x][y] = 20
        elif direction == 'down' :
            if 0 < map[x][y+1] < 10:
                print("rencontre un mur ")
            else:
                x, y = x, y+1
                map[x][y] = 20
        elif direction == 'left' :
            if 0 < map[x-1][y] < 10:
                print("rencontre un mur ")
            else:
                x, y = x-1, y
                map[x][y] = 20
        elif direction == 'right' :
            if (0 < map[x+1][y]< 10):
                print("rencontre un mur ")
            else:
                x, y = x+1, y
                map[x][y] = 20
        return [x, y]
    
