# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 13:03:35 2021

@author: Fredrik
"""

import numpy as np
from sense_hat import SenseHat

sense=SenseHat()



#Level 1

blank1 =         ([0,2,0,0,0,2,0,0],
                  [0,0,0,2,0,0,0,0],
                  [0,2,2,2,2,2,2,2],
                  [0,0,0,0,0,0,0,0],
                  [3,0,0,3,0,0,3,0],
                  [0,0,0,0,0,0,0,0],
                  [2,2,2,2,2,2,2,0],
                  [0,0,0,0,0,0,0,0]
                  )

level1=np.array(blank1)

ballpos = bx, by = 1, 1 # Starting positions

start=sx,sy=0,0
finish=fx,fy=7,7



level1[start] = 1
level1[finish] = -1


W=(128,0,0)#Wall
H=(255,0,0)#Hole
F=(255,255,0)#Finish
G=(0,0,0)#Ground



for i in range(8):
    for j in range(8):
        if level1[i,j]==2:
            sense.set_pixel(i,j,W)
        elif level1[i,j]==3:
            sense.set_pixel(i,j,H)
        elif level1[i,j]==-1:
            sense.set_pixel(i,j,F)
        else:
            sense.set_pixel(i,j,G)
    
