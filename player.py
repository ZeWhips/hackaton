class player:
    """A class that represents the snake"""

    def __init__(self, position, direction):
      
        self._pos = position #the list of the positions where the snake is
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