import pygame
import math
from queue import PriorityQueue

#COLORS
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
PURPLE=(128,0,128)
ORANGE=(255,165,0)
GRAY=(128,128,128)
TURQUOISE=(64,224,208)

#PYGAME WINDOW
WIN_SIDE=800
WIN=pygame.display.set_mode((WIN_SIDE,WIN_SIDE))


#GRID-NODE MANAGEMENT
class Node:
    def __init__(self,row,col,width,total_rows):
        self.row = row
        self.col = col
        self.x = row*width
        self.y = col*width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows
    
        


pygame.display.set_caption("A* PathFinder")

def main():
    run=True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.quit()
    
    main()


if __name__=="__main__":
    main()