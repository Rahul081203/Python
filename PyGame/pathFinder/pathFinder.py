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

    def get_pos(self):
        return self.row,self.col

    def is_closed(self):
        return self.color == RED
    def is_open(self):
        return self.color == GREEN
    def is_barrier(self):
        return self.color == BLACK
    
    def is_start(self):
        return self.color == ORANGE
    def is_end(self):
        return self.color == PURPLE
    def reset(self):
        return self.color == WHITE
    
    def make_closed(self):
        return self.color == RED

    def make_open(self):
        return self.color == GREEN
    def make_barrier(self):
        return self.color == BLACK
    def make_end(self):
        return self.color == TURQUOISE
    def make_path(self):
        return self.color == PURPLE
    
    def draw(self,win):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.width))
    
    def update_neighbors(self,grid):
        pass

    def __lt__(self,other):
        return False

# MANHATTTAN DISTANCE : distance for the quickest L-shaped path from current node to destination
def h(p1,p2):
    x1,y1=p1
    x2,y2=p2
    return abs(x1-x2)+abs(y1-y2)


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