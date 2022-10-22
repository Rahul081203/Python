import pygame
import random

#COLORS
WHITE=(255,255,255)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
RED=(255,0,0)


INITIAL_POS=(350,350)


#PYGAME WINDOW
WIDTH=700
WIN=pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption("Snake - by Rahul")

class Node:
    def __init__(self,width,row,col,total_rows):
        self.row=row
        self.col=col
        self.x=row*width
        self.y=col*width
        self.color=WHITE
        self.width=width
        self.total_rows=total_rows
    
    def get_pos(self):
        return self.row,self.col

    def is_barrier(self):
        return self.color==BLACK or self.color==BLUE

    def is_snake(self):
        return self.color==BLUE
    def make_snake(self):
        self.color = BLUE
    def make_target(self):
        self.color = RED
    
    def draw(self,win):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.width))

    def __lt__(self,other):
        return False

def make_grid(rows,width):
    grid=[]
    gap=width//rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node=Node(i,j,gap,rows)
            grid[i].append(node)
    return grid

def draw_grid(win,rows,width):
    GAP=width//rows
    for i in range(rows):
        pygame.draw.line(win,BLACK,(0,i*GAP),(width,i*GAP))
    for j in range(rows):
        pygame.draw.line(win,BLACK,(j*GAP,0),(j*GAP,width))
def draw(win,grid,rows,width):
    win.fill(WHITE)
    for row in grid:
        for node in row:
            node.draw(win)
    draw_grid(win,rows,width)
    pygame.display.update()

def get_pos(pos,rows,width):
    gap=width//rows
    y,x=pos
    row=y//gap
    col=x//gap
    return row,col

def target_pos():
    return(random.randint(20,700),random.randint(20,700))

def main(win,width):
    ROWS=50
    grid=make_grid(ROWS,width)
    started=False
    run=True
    while run:
        draw(win,grid,ROWS,width)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    started=True
                
                if event.key==pygame.K_UP:
                    
    pygame.quit()

if __name__=="__main__":
    main(WIN,WIDTH)
