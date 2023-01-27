import random as rd

def generate_coin(niv, n):
    '''Generate a given number n of coins per niv'''
    w, h = niv.shape
    for i in range (n):
        x, y = rd.randint(0, w-1), rd.randint(0, h-1)
        while 1<= niv[x][y] <=9 and niv[x][y] != 20:
            x, y = rd.randint(0, h-1), rd.randint(0, w-1)
        niv[x][y] = 10 

def generate_potion(niv, n):
    '''Generate a given number n of potion per niv'''
    w, h = niv.shape
    for i in range (n):
        x, y = rd.randint(0, w-1), rd.randint(0, h-1)
        while 1<= niv[x][y] <=10 and niv[x][y] != 20: #check if different of walls and coins
            x, y = rd.randint(0, h-1), rd.randint(0, w-1)
        niv[x][y] = 11

def generate_trap(niv, n):
    '''Generate a given number n of trap per niv'''
    w, h = niv.shape
    for i in range (n):
        x, y = rd.randint(0, w-1), rd.randint(0, h-1)
        while 1<= niv[x][y] <=11 and niv[x][y] != 20: #check if different of walls and coins
            x, y = rd.randint(0, h-1), rd.randint(0, w-1)
        niv[x][y] = 12






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
