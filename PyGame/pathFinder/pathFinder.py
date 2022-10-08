from re import L
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
CLOSED=(204,255,51)

#PYGAME WINDOW
WIN_SIDE=500
WIN=pygame.display.set_mode((WIN_SIDE,WIN_SIDE))

pygame.display.set_caption("A* PathFinder")


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
        return self.color == CLOSED
    def is_open(self):
        return self.color == GREEN
    def is_barrier(self):
        return self.color == BLACK
    
    def is_start(self):
        return self.color == RED
    def is_end(self):
        return self.color == BLUE
    def reset(self):
        self.color = WHITE
    
    def make_closed(self):
        self.color = CLOSED

    def make_open(self):
        self.color = GREEN
    def make_barrier(self):
        self.color = BLACK
    def make_start(self):
        self.color = RED
    def make_end(self):
        self.color = BLUE
    def make_path(self):
        self.color = ORANGE
    
    def draw(self,win):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.width))
    
    def update_neighbors(self,grid):
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col])
        
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.col])
        
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col + 1])
        
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col - 1])
        

    def __lt__(self,other):
        return False

# MANHATTTAN DISTANCE : distance for the quickest L-shaped path from current node to destination
def h(p1,p2):
    x1,y1=p1
    x2,y2=p2
    return abs(x1-x2)+abs(y1-y2)

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
        pygame.draw.line(win,GRAY,(0,i*GAP),(width,i*GAP))
    for j in range(rows):
        pygame.draw.line(win,GRAY,(j*GAP,0),(j*GAP,width))

def draw(win,grid,rows,width):
    win.fill(WHITE)
    for row in grid:
        for node in row:
            node.draw(win)
    draw_grid(win,rows,width)
    pygame.display.update()

def get_clicked_pos(pos,rows,width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap
    return row, col
def reconstruct_path(parent,current,draw):
    while current in parent:
        current = parent[current]
        current.make_path() # make the current node as a part of the path i.e. color it purple
        draw() # call algorithm


def algorithm(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue() # In a priority queue, the elements are arranged based on their priority score, for us it is the least f-score
    open_set.put((0, count, start)) # Priority queue uses put instead of push or append to add an element
    # count has been inserted to the open set first as it can be used to break ties between any two nodes with the same f-score based on which was inserted first.
    # '0' is the f-score for the start node
    
    parent={} # to keep track of the parent neighbors

    #Initiating g_score and f_score for a given node(except start or end) to be infinity so that the next node is always considered to be the shortest path towards finding the end node.
    g_score = {node:float("inf") for row in grid for node in row}
    g_score[start]=0
    f_score = {node:float("inf") for row in grid for node in row}
    f_score[start]=h(start.get_pos(),end.get_pos())

    open_set_hash={start} # to tell us if a node is in the queue or not

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2] # we used index 2 because the open_set element has the node variable at the 2nd index
        open_set_hash.remove(current)

        if current==end: # if current node is path, then reconstruct the path from end to start
            reconstruct_path(parent,end,draw)
            end.make_end()
            start.make_start()
            return True
        for neighbor in current.neighbors:
            temp_g_score=g_score[current]+1 # Assuming the path distance of neighbor from the current node is 1 we can assume that the temporary g_score for the neighboring node is one more than the current g_score of the node in question
            if temp_g_score<g_score[neighbor]: # if the current temp_g_score is smaller than the neighboring node's g_score then, switch to this path which is the better one as it has lower g_score.
                parent[neighbor]=current # Set the new path's parent to be the current node

                #Updating the g_score and f_score of the neighboring node of the current node
                g_score[neighbor]= temp_g_score
                f_score[neighbor]= temp_g_score+h(neighbor.get_pos(),end.get_pos())
        
                if neighbor not in open_set_hash:
                    count+=1
                    open_set.put((f_score[neighbor],count,neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
        draw() # recursively call algorithm function until the iteration is terminated
        if current != start:
            current.make_closed()
    return False # return False if path not found
        
def main(win,width):
    ROWS = 50
    grid = make_grid(ROWS,width)
    start = None
    end = None
    run = True
    started = False
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if started:
                continue;
            
            if pygame.mouse.get_pressed()[0]: #  if left mouse button clicked
                pos=pygame.mouse.get_pos()
                row,col=get_clicked_pos(pos,ROWS,width)
                node=grid[row][col]
                if not start and node != end:
                    start = node
                    start.make_start()

                elif not end and node != start:
                    end = node
                    end.make_end()
                
                elif node !=end and node !=start:
                    node.make_barrier()

            elif pygame.mouse.get_pressed()[2]:# if right mouse button clicked
                pos = pygame.mouse.get_pressed()
                row, col=get_clicked_pos(pos,ROWS,width)
                node=grid[row][col]
                node.reset()
                if node == start:
                    start = None
                elif node == end:
                    end = None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    algorithm(lambda: draw(win,grid,ROWS,width),grid,start,end)
    
                if event.type == pygame.K_c:
                    start=None
                    end=None
                    grid=make_grid(ROWS,width)
    pygame.quit()



if __name__=="__main__":
    main(WIN,WIN_SIDE)