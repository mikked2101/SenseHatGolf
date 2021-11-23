import numpy as np
import random as rnd
import pygame
from sense_hat import SenseHat
from snakepics import *
import time

sense = SenseHat()


pygame.init()

clock = pygame.time.Clock()


R = (255, 0, 0)  # Red
W = (255, 255, 255)  # White
D = (0, 0, 0)
            

length = 1
lengthfac = 2



board = np.zeros((8, 8), dtype=np.int8) # Board setup

headpos = hx, hy = 1, 1 # Starting positionss
fruitpos = fx, fy = 6, 6

board[headpos] = 1
board[fruitpos] = -1

FPS = 3
d = "r"

running = True


while running:
    clock.tick(FPS)

    for event in sense.stick.get_events():
        
        if event.action == "pressed":
    
            if event.direction =="up":
                if d != "d":
                    d = "u"
            if event.direction =="down":
                if d != "u":
                    d = "d"
            if event.direction =="right":
                if d != "l":
                    d = "r"
                
            if event.direction =="left":
                if d != "r":
                    d= "l"


    if d == "u":
        hy -= 1
    if d == "d":
	    hy += 1
    if d == "r":
	    hx += 1
    if d == "l":
	    hx -= 1
	

 
    
    if hx < 0 or hx > 7 or hy < 0 or hy > 7: # Check if out of Bounds
        break
	
    if board[hx, hy] == -1: # Check fruit pickup
        length += lengthfac
        while True:
            fx = rnd.randint(0, 7)
            fy = rnd.randint(0, 7)
            if board[fx, fy] == 0:
                break
    
    if board[hx, hy] > 1: # Check self collision
        break
    
    
    for i in range(8): # Update Body
        for j in range(8):
            if board[i, j] > 0:
                board[i, j] += 1
            if board[i, j] > length:
                board[i, j] = 0
    
    
    board[fx, fy] = -1
    board[hx, hy] = 1
    
    for i in range(8):
        for j in range(8):
            if board[i, j] >= 1:
                sense.set_pixel(i, j, W)
            elif board[i, j] == -1:
                sense.set_pixel(i, j, R)		
            else:
                sense.set_pixel(i, j, D)

sense.set_pixels(loser())
time.sleep(1)
sense.clear()
sense.show_message(str(length), text_colour=[255, 0, 0])
       
