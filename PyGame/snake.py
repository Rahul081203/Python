import pygame

#COLORS
WHITE=(255,255,255)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
RED=(255,0,0)


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

    def snake(self):
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

def main(win,width):
    ROWS=50
    grid=make_grid(ROWS,width)
    
    run=True
    while run:
        draw(win,grid,ROWS,width)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
    pygame.quit()

if __name__=="__main__":
    pos=
    main(WIN,WIDTH)
