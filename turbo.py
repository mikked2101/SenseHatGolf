import pygame
import numpy as np
from sense_hat import SenseHat

sense = SenseHat()
pygame.init()

clock = pygame.time.Clock()

blank1 =         ([0,2,0,0,0,2,0,0],
                  [0,0,0,2,0,0,0,0],
                  [0,2,2,2,2,2,2,2],
                  [0,0,0,0,0,0,0,0],
                  [3,0,0,3,0,0,3,0],
                  [0,0,0,0,0,0,0,0],
                  [2,2,2,2,2,2,2,0],
                  [0,0,0,0,0,0,0,0]
                  )
level=np.array(blank1)

B=(255, 255, 255) #Ball
W=(128, 0, 0) # Wall
H=(0, 255, 0) # Hole
F=(255, 255, 0) # Finish
G=(0, 0, 0) # Ground

board = np.zeros((8, 8), dtype=np.int8) # Board setup
print(board)

ballpos = bx, by = 1, 1 # Starting positions

vx = 0
vy = 0

board[1, 1] = 1

FPS = 5
d = "n"



for i in range(8): # Update level
    for j in range(8):
        sense.set_pixel(i, j, G)

running = True


while running:
    clock.tick(FPS)

    for event in sense.stick.get_events():
        
        if event.action == "pressed":
    
            if event.direction =="up":
                vy = -1
            if event.direction =="down":
                vy = 1
            if event.direction =="right":
                vx = 1
            if event.direction =="left":
                vx = -1
    
    level[bx, by] = 0

    if vy != 0:
        try: 
            if level[bx, by + vy] == 2 or by + vy == -1 or by + vy == 8:
                vy = 0
        except IndexError:
            vy = 0

        by += vy

    if vx != 0:
        try:
            if level[bx + vx, by] == 2 or bx + vx == -1 or bx + vx == 8:
                vx = 0
        except IndexError:
            vx = 0
        bx += vx

    level[bx, by] = 1


    



    for i in range(8):
        for j in range(8):
            if level[i, j]==1:
                sense.set_pixel(i, j, B)
            elif level[i,j]==2:
                sense.set_pixel(i,j,W)
            elif level[i,j]==3:
                sense.set_pixel(i,j,H)
            elif level[i,j]==-1:
                sense.set_pixel(i,j,F)
            else:
                sense.set_pixel(i,j,G)
        

sense.clear()
