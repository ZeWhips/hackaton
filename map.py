from assets import Assets
import numpy as np
import random as rd


class Map():
    pixelcase = 32

    niv1 = np.array([
        [7, 1, 1, 1, 1, 1, 1, 1, 3],
        [7, 20, 0, 0, 0, 0, 0, 0, 3], 
        [7, 0, 0, 0, 0, 0, 0, 0, 3],
        [7, 0, 0, 0, 0, 0, 0, 0, 3],
        [7, 0, 0, 0, 8, 5, 2, 0, 3],
        [6, 5, 5, 5, 4, 9, 6, 5, 4],
    ])

    niv2 = np.array([
        [7, 1, 1, 1, 1, 1, 1, 1, 3, 9, 9, 7, 1, 1, 1, 1, 3],
        [7, 0, 0, 10, 0, 0, 0, 0, 3, 9, 9, 7, 0, 0, 0, 13, 3], 
        [7, 0, 0, 0, 11, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 3],
        [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 5, 4],
        [7, 0, 10, 0, 12, 0, 8, 5, 5, 5, 5, 5, 5, 5, 4, 9, 9],
        [7, 0, 0, 0, 0, 0, 3, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [7, 0, 0, 0, 0, 0, 3, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [7, 0, 13, 0, 0, 0, 3, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [6, 5, 5, 5, 5, 5, 4, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    ])

    niv3 = np.array([
        [7, 1, 1, 1, 1, 1, 3],
        [7, 0, 0, 0, 0, 0, 3], 
        [7, 0, 0, 0, 0, 0, 3],
        [6, 5, 5, 5, 5, 5, 4],
    ])

    niv4 = np.array([
        [7, 1, 1, 1, 1, 1, 3, 9, 9, 9, 9, 9, 9],
        [7, 0, 0, 0, 0, 0, 3, 9, 9, 9, 9, 9, 9], 
        [7, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 3, 9],
        [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 9],
        [7, 0, 0, 0, 0, 0, 8, 5, 5, 2, 0, 3, 9],
        [7, 0, 0, 0, 0, 0, 3, 9, 9, 7, 0, 3, 9],
        [7, 0, 0, 0, 0, 0, 3, 9, 9, 7, 0, 3, 9],
        [6, 5, 5, 5, 5, 5, 4, 9, 9, 7, 0, 3, 9],
        [9, 7, 1, 1, 1, 1, 1, 1, 1, 1, 0, 3, 9],
        [9, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 9],
        [9, 7, 0, 0, 0, 0, 8, 5, 5, 5, 5, 4, 9],
        [9, 7, 0, 0, 0, 0, 3, 9, 9, 9, 9, 9, 9],
        [9, 6, 5, 5, 5, 5, 4, 9, 9, 9, 9, 9, 9]])

    niv2ech = [niv1, niv3]
    niv2echelle = {}

    def __init__(self):
        self.niv2echelle = {tuple(tup): self.niv2ech[i] for i, tup in enumerate(np.where(self.niv2 == 13))}

    #niv3echelle = dict(zip(np.where(niv2 == 13), [niv2]))
    
    def get_echelle(self, niveau):
        if np.sum(niveau[niveau==13]) >= 1:
            if niveau == self.niv2:
                return self.niv2echelle

    

    def get_size(self, map):
        w, h = map.shape
        return (h * self.pixelcase, w * self.pixelcase)

    def showMap(self, map, fenetre):
        for i in range(5):
            for j in range(5):
                fenetre.blit(Assets.assetDungeon, (i*4*32,j*3*32), Assets.fondsize)
            
        for j, c in enumerate(map):
            for i, case in enumerate(c):

                x = i * self.pixelcase
                y = j * self.pixelcase
                
                if case == 1:
                    fenetre.blit(Assets.assetDungeon, (x,y), Assets.murtopsize)
                if case == 2:
                    fenetre.blit(Assets.assetDungeon, (x,y), Assets.murtoprightsize)
                if case == 3:
                    fenetre.blit(Assets.assetDungeon, (x,y), Assets.murrightsize)
                if case == 4:
                    fenetre.blit(Assets.assetDungeon, (x,y), Assets.murbottomrightsize)
                if case == 5:
                    fenetre.blit(Assets.assetDungeon, (x,y), Assets.murbottomsize)
                if case == 6:
                    fenetre.blit(Assets.assetDungeon, (x,y), Assets.murbottomleftsize)
                if case == 7:
                    fenetre.blit(Assets.assetDungeon, (x,y), Assets.murleftsize)
                if case == 8:
                    fenetre.blit(Assets.assetDungeon, (x,y), Assets.murtopleftsize)
                if case == 9:
                    fenetre.blit(Assets.assetDungeon, (x,y), Assets.murpleinsize)


                if case == 10:
                    fenetre.blit(Assets.assetDungeon, (x,y), Assets.moneysize)
                if case == 11:
                    fenetre.blit(Assets.assetDungeon, (x,y), Assets.potionsize)
                if case == 12:
                    fenetre.blit(Assets.assetDungeon, (x,y), Assets.trapsize)
                if case == 13:
                    fenetre.blit(Assets.assetDungeon, (x,y), Assets.echellesize)

                if case == 20:
                    fenetre.blit(Assets.assetPerso, (x,y), Assets.persosize)


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