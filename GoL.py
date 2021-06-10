import sys, pygame
import numpy as np
from pygame import display
import random
pygame.init()

fps = 12
clock = pygame.time.Clock()
size = width, height = 800, 600
black = (0, 0, 0)
white = (255, 255, 255)
scale = 20
offset = 1

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Game Of Conway")

class Grid():
    def __init__(self,width, height,scale,offset):
        self.scale = scale
        self.offset = offset
        self.rows = int(width/scale)
        self.cols = int(height/scale)
        self.ogrid = np.ndarray(shape=(self.rows,self.cols))
        self.hold = np.ndarray(shape=(self.rows,self.cols))

    def randomfill(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.ogrid[i][j] = random.randint(0,1)
        return self
    
    def logic(self,i,j,soma):
        if self.ogrid[i][j] == 1:
            pygame.draw.rect(screen,black,[i*self.scale,j*self.scale,self.scale-self.offset,self.scale-self.offset])
        else:
            pygame.draw.rect(screen,white,[i*self.scale,j*self.scale,self.scale-self.offset,self.scale-self.offset])
        if self.ogrid[i][j] == 0 and soma == 3:
            self.hold[i][j] = 1
        elif self.ogrid[i][j] == 1 and soma < 2 or soma > 3:
            self.hold[i][j] = 0
        else:
            self.hold[i][j] = self.ogrid[i][j]
    
    def scannear(self):
        for i in range(self.rows):
            for j in range(self.cols):
                total = 0
                for x in range(-1,2):
                    for y in range(-1,2):
                        x_line = (i+x+self.rows) % self.rows
                        y_line = (j+y+self.cols) % self.cols
                        total += self.ogrid[x_line][y_line]
                total -= self.ogrid[i][j]
                self.logic(i,j,total)
        self.ogrid = self.hold
      
NewArray = Grid(width,height,scale,offset)
NewArray.randomfill()

while 1:
    clock.tick(fps)
    screen.fill(white)
    NewArray.scannear()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    pygame.display.update()


