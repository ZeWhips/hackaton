class player:

    def __init__(self, position):
      
        self._pos = position 

    def state(self, position, direction):
      
        self._pos = position 
        self._direction = direction

    def getPos(self):
        return self._pos.copy() 

    def getDirection(self):
        return self._direction
   
    def move_head(self):
        head = self.getPos()
        x, y = head
        direction = self.getDirection()
        if direction == 'up' :
            x, y = x, y-1
        elif direction == 'down' :
            x, y = x, y+1
        elif direction == 'left' :
            x, y = x-1, y
        elif direction == 'right' :
            x, y = x+1, y
        return (x, y)