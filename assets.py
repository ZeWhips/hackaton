import pygame as pg

class Assets():
    assetDungeon = pg.transform.scale(pg.image.load("assets/character and tileset/Dungeon_Tileset.png"), (320, 320))
    murtopleftsize = (4*32, 5*32, 32, 32)
    murtopsize = (32, 0 , 32, 32)
    murtoprightsize = (5*32, 5*32 , 32, 32)
    murrightsize = (5*32, 32 , 32, 32)
    murbottomrightsize = (5*32, 4*32 , 32, 32)
    murbottomsize = (32, 4*32 , 32, 32)
    murbottomleftsize = (0, 4*32, 32, 32)
    murleftsize = (0, 32, 32, 32)
    murpleinsize = (8*32, 7*32, 32, 32)
    fondsize = (6*32, 0, 4*32, 3*32)
    echellesize = (9*32, 3*32, 32, 32)
    moneysize = (6*32, 8*32, 32, 32)
    trapsize = (4*32, 6*32, 32, 32)
    potionsize = (7*32, 8*32, 32, 32)


    assetPerso = pg.transform.scale(pg.image.load("assets/character and tileset/Dungeon_Character_2.png"), (224, 64))
    persosize = (2*32, 0, 32, 32)