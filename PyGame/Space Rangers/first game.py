from pickle import TRUE
import pygame
import os
from pygame.locals import *
pygame.init()



import os
os.getcwd()
WIDTH,HEIGHT=900,500

WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
BLUE=(0,0,255)

FPS=60
WIN=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")

VELOCITY=5
BULLET_VELOCITY=5
MAX_BULLETS=5

SPACESHIP_WIDTH=100
SPACESHIP_HEIGHT=60

BLUE_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

BLUE_SPACESHIP_IMAGE=pygame.image.load("./PyGame/Space Rangers/Assets/blue.png")
RED_SPACESHIP_IMAGE=pygame.image.load("./PyGame/Space Rangers/Assets/red.png")
BLUE_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(BLUE_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)
RED_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)

SPACE = pygame.transform.scale(pygame.image.load("./PyGame/Space Rangers/Assets/space.png"),(WIDTH,HEIGHT))

BORDER=pygame.Rect((WIDTH/2) - 5,0,10,HEIGHT)

HEALTH_FONT = pygame.font.SysFont('comicsans',40)
WINNER_FONT = pygame.font.SysFont('algerian',100)


#What we want to draw
def draw_window(blue,red,red_bullets,blue_bullets,blue_health,red_health):
    WIN.blit(SPACE,(0,0))
    pygame.draw.rect(WIN,BLACK,BORDER)

    red_health_text=HEALTH_FONT.render("Health: "+str(red_health),1,WHITE)
    blue_health_text=HEALTH_FONT.render("Health: "+str(blue_health),1,WHITE)

    WIN.blit(BLUE_SPACESHIP,(blue.x,blue.y))#to load surfaces to your pygame window you have to use blit function
    #In pygame the origin lies on the top left corner of the window 
    WIN.blit(RED_SPACESHIP,(red.x,red.y))

    WIN.blit(red_health_text,(WIDTH - red_health_text.get_width()-10,10))
    WIN.blit(blue_health_text,(10,10))
    for bullet in red_bullets:
        pygame.draw.rect(WIN,RED,bullet)
    for bullet in blue_bullets:
        pygame.draw.rect(WIN,BLUE,bullet)

    pygame.display.update()

def blue_movement(keys_pressed,blue):
    if keys_pressed[pygame.K_a] and blue.x - VELOCITY > 0: # if 'a' pressed
            blue.x-=VELOCITY
    if keys_pressed[pygame.K_d] and blue.x + VELOCITY< BORDER.x-60:
        blue.x+=VELOCITY
    if keys_pressed[pygame.K_w] and blue.y - VELOCITY > 0:
        blue.y-=VELOCITY
    if keys_pressed[pygame.K_s] and blue.y + VELOCITY < HEIGHT-100:
        blue.y+=VELOCITY

def red_movement(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT] and red.x - VELOCITY > BORDER.x: #LEFT
            red.x-=VELOCITY
    if keys_pressed[pygame.K_RIGHT] and red.x + VELOCITY < WIDTH - 60: #RIGHT
        red.x+=VELOCITY
    if keys_pressed[pygame.K_UP] and red.y - VELOCITY > 0: #UP
        red.y-=VELOCITY
    if keys_pressed[pygame.K_DOWN] and red.y + VELOCITY < HEIGHT-100:  #DOWN
        red.y+=VELOCITY

def bullets_control(blue_bullets, red_bullets, blue, red):
    for bullet in blue_bullets:
        bullet.x += BULLET_VELOCITY
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            blue_bullets.remove(bullet)      
        elif bullet.x > WIDTH:
            blue_bullets.remove(bullet)
    for bullet in red_bullets:
        bullet.x -=BULLET_VELOCITY
        if blue.colliderect(bullet):
            pygame.event.post(pygame.event.Event(BLUE_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)

def show_winner(text):
    winner_text=WINNER_FONT.render(text,1,WHITE)
    WIN.blit(winner_text,(WIDTH/2 - winner_text.get_width()/2, HEIGHT/2-winner_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(10000)


#Infinite Loop
def main():
    red=pygame.Rect(700,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    blue=pygame.Rect(100,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    red_bullets=[]
    blue_bullets=[]
    red_health=10
    blue_health=10
    clock=pygame.time.Clock()
    run=True
    while run:
        clock.tick(FPS) # Setting a fps=60
        #Looping through events in the pygame window
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(blue_bullets) < MAX_BULLETS:
                    bullet=pygame.Rect(blue.x+blue.width,blue.y+ blue.height/2,10,5)
                    blue_bullets.append(bullet)
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet=pygame.Rect(red.x,red.y+ red.height/2,10,5)
                    red_bullets.append(bullet)
            if event.type==RED_HIT:
                red_health-=1
            if event.type==BLUE_HIT:
                blue_health-=1
        winner=""
        if red_health<0:
            winner="BLUE WINS !!!"
        if blue_health<0:
            winner="RED WINS !!!"
        if winner != "":
            show_winner(winner)
            break;

        
        
        keys_pressed=pygame.key.get_pressed()#Store the presently pressed keys in keys_pressed
        blue_movement(keys_pressed,blue)
        red_movement(keys_pressed,red)
        bullets_control(blue_bullets,red_bullets,blue,red)
        draw_window(blue,red,red_bullets,blue_bullets,blue_health,red_health)
    main()

if __name__=="__main__":
    main()