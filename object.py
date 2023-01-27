class Coins:

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._num


    def new_coin(self, player, board) : #player?  nom des indices du bord des lignes
        x = rd.randint(1, board._line - 2)
        y = rd.randint(1, board._col - 2)
        positionPlayer = player.getPos()#position du perso
        while ((x, y) == positionPlayer):
            x = rd.randint(1, board._line - 2)
            y = rd.randint(1, board._col - 2)
        self._x = x
        self._y = y


