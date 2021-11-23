import pygame
import numpy as np
from sense_hat import SenseHat

sense = SenseHat()

pygame.init()

clock = pygame.time.Clock()


R = (255, 0, 0)  # Red
W = (255, 255, 255)  # White
D = (0, 0, 0)
G = (0, 255, 0)


board = np.zeros((8, 8), dtype=np.int8) # Board setup
print(board)

ballpos = bx, by = 1, 1 # Starting positions

board[1, 1] = 1

FPS = 5



for i in range(8): # Update level
        for j in range(8):
            sense.set_pixel(i, j, G)

running = True


while running:
    clock.tick(FPS)

    for event in sense.stick.get_events():
        
        """if event.action == "pressed":
    
            if event.direction =="up":
                    d = "u"
            if event.direction =="down":
                    d = "d"
            if event.direction =="right":
                    d = "r"
            if event.direction =="left":
                    d= "l""""
    


    sense.set_pixel(bx, by, W)

sense.clear()