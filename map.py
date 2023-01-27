from assets import Assets
import numpy as np


class Map():
    pixelcase = 32

    niv1 = np.array([
        [7, 1, 1, 1, 1, 1, 1, 1, 3],
        [7, 0, 0, 0, 0, 0, 0, 0, 3], 
        [7, 0, 0, 0, 0, 0, 0, 0, 3],
        [7, 0, 0, 0, 0, 0, 0, 0, 3],
        [7, 20, 0, 0, 8, 5, 2, 0, 3],
        [6, 5, 5, 5, 4, 9, 6, 5, 4],
    ])



    def get_size(self, map):
        w, h = map.shape
        return (h * self.pixelcase, w * self.pixelcase)

    def showMap(self, map, fenetre):
        fenetre.blit(Assets.assetDungeon, (0,0), Assets.fondsize)
        fenetre.blit(Assets.assetDungeon, (4*32,0), Assets.fondsize)
        fenetre.blit(Assets.assetDungeon, (0,3*32), Assets.fondsize)
        fenetre.blit(Assets.assetDungeon, (4*32,3*32), Assets.fondsize)
        fenetre.blit(Assets.assetDungeon, (8*32,0), Assets.fondsize)
        fenetre.blit(Assets.assetDungeon, (8*32,3*32), Assets.fondsize)
        fenetre.blit(Assets.assetDungeon, (8*32,6*32), Assets.fondsize)
        fenetre.blit(Assets.assetDungeon, (4*32,6*32), Assets.fondsize)
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

                if case == 20:
                    fenetre.blit(Assets.assetPerso, (x,y), Assets.persosize)

