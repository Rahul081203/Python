from pickle import TRUE
import pygame
import os
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

BLUE_SPACESHIP_IMAGE=pygame.image.load("./Assets/blue.png")
RED_SPACESHIP_IMAGE=pygame.image.load("./Assets/red.png")
BLUE_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(BLUE_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)
RED_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)

SPACE = pygame.transform.scale(pygame.image.load("./Assets/space.png"),(WIDTH,HEIGHT))

BORDER=pygame.Rect((WIDTH/2) - 5,0,10,HEIGHT)

#What we want to draw
def draw_window(blue,red,red_bullets,blue_bullets):
    WIN.blit(SPACE,(0,0))
    pygame.draw.rect(WIN,BLACK,BORDER)
    WIN.blit(BLUE_SPACESHIP,(blue.x,blue.y))#to load surfaces to your pygame window you have to use blit function
    #In pygame the origin lies on the top left corner of the window 
    WIN.blit(RED_SPACESHIP,(red.x,red.y))

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
        if red_health<=0:
            winner="BLUE WINS !!!"
        if blue_health<=0:
            winner="RED WINS !!!"


        
        
        keys_pressed=pygame.key.get_pressed()#Store the presently pressed keys in keys_pressed
        blue_movement(keys_pressed,blue)
        red_movement(keys_pressed,red)
        bullets_control(blue_bullets,red_bullets,blue,red)
        draw_window(blue,red,red_bullets,blue_bullets)
    pygame.quit()

if __name__=="__main__":
    main()