import random as rd
import pygame as pg
import argparse
import os
import logging
import re



def read_args():
    '''Read command line arguments'''
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--Heigth', type=int, default=600)
    parser.add_argument('--Width', type=int, default=600)
    parser.add_argument('--TileWidth', type=int, default=20)

    args = parser.parse_args() #args est un dictionnaire
    return args

#Fruit color
GREEN = (0, 255, 0)

#Board colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)


class Board: 
    """A class who contains the caracteristics of the board"""

    def __init__(self, Heigth, Width, TileWidth):
        self._heigth = Heigth
        self._width = Width
        self._tile = TileWidth
        self._line = Heigth//TileWidth
        self._col = Width//TileWidth

    def getHeigth(self):
        return self._heigth

    def getWidth(self):
        return self._width

    def getTileWidth(self):
        return self._tile


class Snake:
    """A class that represents the snake"""

    def __init__(self, length, positions, direction, color=pg.Color('#000000')):
        self._length = length
        self._body = positions #the list of the positions where the snake is
        self._direction = direction
        self._color = color
    

    def choose_color(self):
        new_color = input('Choose a color for the snake (in hexa):')
       
        #with regex we check if the color has the good format
        if re.search(r"^#[0-9A-Fa-f]{6}$", new_color):
            self._color = new_color


    def getLength(self):
        return self._length

    def getBody(self):
        return self._body.copy() 

    def getDirection(self):
        return self._direction
   

    def move_head(self):
        '''moving the head of the snake according to the direction, returning the position of the new head'''
        head = self.getBody()[0]
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
        

    def move_body_and_grow(self, fruit, board, game):
        '''moving the rest of the snake's body by shifting the positions in the list'''
        length = self.getLength()
        body = self.getBody()

        #1st case : the snake eats the fruit, lengthening the body and stashing the positions (other than head)
        if (fruit.x, fruit.y) == body[0] : 
            (game.score).actualize_score()
            self._body[0] = self.move_head() #replacing the head in the position list
            fruit = fruit.new_fruit(self, board)
            body.append(body[length-1])
            self._length = len(body)
            for k in range ((self._length)-2, 0, -1) :
                body[k] = body[k-1] 

        #2nd case the snake doesn't eat the fruit, just stashing the positions (other than head)
        else : 
            self._body[0] = self.move_head() #replacing the head in the position list
            for k in range (length-1, 0, -1) : 
                body[k] = body[k-1]   
        
        self._body[1:] = body[1:] #replacing the rest of the body
        



class Fruit:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property 
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y
    

    def new_fruit(self, snake, board) :
        x = rd.randint(0, board._line - 1)
        y = rd.randint(0, board._col - 1)
        body = snake.getBody()
        while (x, y) in body :
            x = rd.randint(0, board._line - 1)
            y = rd.randint(0, board._col - 1)
        self._x = x
        self._y = y



class Score :
    """A class to store the score"""

    def __init__(self):
        self._score = 0
    """Score starts at zero"""

    def actualize_score(self):
        self._score = self._score + 1 
    """the score raise when the snake eats the fruit"""




class File:
    """A class for the file containing the 5 highscores"""

    def __init__(self, file='scores.txt'):
        self._file = file
        self._highscore = [] #list that stores the scores written in the file and that actualizes the file



    def read_file(self):
        """Reading the content of the file if he exists or creating one
        Filling a temporary list that contains all the lines
        but wrong format"""

        #the file doesn't exist, we create it 
        if not os.path.exists(self._file) : 
            with open ('scores.txt', 'w') as f :
                Name = input('Nom du joueur:')
                Score = self.score_value() 
                L = [Name,Score]

        #the file exists, we read it
        else :
            with open ('scores.txt', 'r') as f :
                L = []
                for line in f :
                    L.append(line)
        return L
  


    def fill(self, L) :
        """L is the temporary list returned by the previous function
        Filling the list of highscore with the tuples (score, name)"""
        self._highscore = []
        for line in L :
            (self._highscore).append(line)
        for k in range (len(self._highscore)) :
            self._highscore[k] = (self._highscore[k]).split(',')
            self._highscore[k][1] = int((self._highscore[k][1]).strip('\n'))
            (s,n) = (self._highscore[k][1], self._highscore[k][0])
            self._highscore[k] = (s,n)
    


    def write(self, score) :
        """Testing if the score must be written
        and writing it if necessary"""

        # less than 5 scores, automatically write the score
        if len(self._highscore) < 5 :
            Name = input("player's name:")
            with open ('scores.txt', 'a') as f :
                print(Name,',',score, file=f)

        # testing if the score should be kept
        # sorting the list and poping the weakest score
        else :
            self._highscore.sort(key=None, reverse=True)
            Score_values = [self._highscore[k][0] for k in range (len(self._highscore))]
            if score > min(Score_values) :
                self._highscore.pop()
                Name = input("player's name:")
                self._highscore.append((score, Name))

                #reediting the file
                with open('scores.txt', 'w') as f : 
                    for k in range (len(self._highscore)) :
                        print(self._highscore[k][1],',',self._highscore[k][0], file=f)
    



class Game:
    

    def __init__(self, Heigth, Width, TileWidth): 
        """Initializing variables to play"""
        self.running = True
        self.board = Board(Heigth, Width, TileWidth)
        self.snake = Snake(3, [(10, 15),(11, 15),(12, 15)], 'left')
        self.fruit = Fruit(5, 7)
        self.score = Score()
        self.file = File('scores.txt')
        



    def start(self):
        """Generating a clock and a screen according to the board's dimensions"""
        pg.init()
        screen = pg.display.set_mode(((self.board)._heigth, (self.board)._width))
        clock = pg.time.Clock()
        return (screen, clock)


    def draw_checkerboard(self, screen):
        """Drawing the checkerboard on the screen"""
        line = (self.board)._line
        col = (self.board)._col

        for i in range (line) : 
            for j in range (col) :
    # the coordinates of the rectangle in pixels
                x = 20*i 
                y = 20*j 
    # use of the method draw.rect()
                if (i+j)%2 == 0 : #modulo to to draw on alternate rectangles
                    rect = pg.Rect(x, y, (self.board)._tile, (self.board)._tile)
                    pg.draw.rect(screen, RED, rect)
                else :
                    rect = pg.Rect(x, y, (self.board)._tile, (self.board)._tile)
                    pg.draw.rect(screen, WHITE, rect)


    def draw_fruit(self, screen):
        """Drawing fruit on the screen"""
        rect = pg.Rect(20*self.fruit.x, 20*self.fruit.y, (self.board)._tile, (self.board)._tile)
        pg.draw.rect(screen, GREEN, rect)


    def draw_snake(self, screen): 
        """Drawing the snake's body with the positions of the body"""
        length = self.snake.getLength()
        body = self.snake.getBody()
        for k in range (length) :
            rect = pg.Rect(body[k][0]*20,body[k][1]*20, (self.board)._tile, (self.board)._tile)
            pg.draw.rect(screen, self.snake._color, rect)



    def process_event(self):
        """Detecting actions of the player"""
        

        for event in pg.event.get():

            
            if event.type == pg.QUIT:
                self.running = False
            
            elif event.type == pg.KEYDOWN:
            
                if event.key == pg.K_q:
                    self.running = False

                #detect a change in the direction    
                elif event.key == pg.K_UP :
                    self.snake._direction = 'up'
                elif event.key == pg.K_DOWN :
                    self.snake._direction = 'down'
                elif event.key == pg.K_LEFT :
                    self.snake._direction = 'left'
                elif event.key == pg.K_RIGHT :
                    self.snake._direction = 'right'

    def detect_end_game(self):
        '''Stop the game if the snake bites his tail or turn around'''
        length = self.snake.getLength()
        body = self.snake.getBody()
        head = body[0]
        for k in range (1, length): 
            if body[k] == head :
                self.running = False


def main():

    """To launch and run the game"""
    
    args = read_args()
    Heigth = args.Heigth
    Width = args.Width
    TileWidth = args.TileWidth
    game=Game(Heigth, Width, TileWidth)
    screen, clock = game.start()
    clock = pg.time.Clock()

    game.snake.choose_color()

    while game.running:
        
        pg.display.set_caption(f"Score: {(game.score)._score}")
        clock.tick(4)

        # drawing the board with all elements
        game.draw_checkerboard(screen) 
        game.draw_fruit(screen)
        game.draw_snake(screen)
                
        # Detecting actions
        game.process_event()
        game.detect_end_game()


        game.snake.move_head()
        game.snake.move_body_and_grow(game.fruit, game.board, game)
                    
        # Actualizing the screen
        pg.display.update()

    pg.quit()

     
    L = (game.file).read_file()
    (game.file).fill(L)
    (game.file).write((game.score)._score)
    with open((game.file)._file, 'r') as f :
        for line in f :
            print(line)



# Create a logger for this module
logger = logging.getLogger(__name__)
        
# Main section
'''pour éviter que le jeu ne se lance si on importe le fichier
pour avoir accès aux classes crées'''
if __name__ == "__main__":

    import sys

    # Setup the logger
    handler = logging.StreamHandler(sys.stderr)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    # Call main function
    main()

    # Quit program properly
    quit(0)
