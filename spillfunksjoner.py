def print_score(score):                     #Funksjon som printer ut score
    with open("yourscore.txt", "w") as fil: #Åpner fil med navn yourscore som tillater å skrive i fil
        fil.write("Score: " + str(score))   #Score blir lagt til i fil

def GAMEOVER(score):
    break
    sense.clear
    sense.show_message("GAME OVER")
    time.sleep(0.1)
    sense.show_message("Your score: "+str(score))
    
 def TIMER():
    new_level_time=
    levelstart= pygame.time.get_ticks
    seconds=(pygame.time.get_ticks-levelstart)/1000
    if seconds > 40:
        GAMEOVER(score)
    return seconds

 def LEVELFINISH(seconds):
        current_level+=1
        sense.clear
        sense.show_message("LEVEL"+str(current_level)
        LOAD_LEVEL()
                           
        
        
        
 def LOAD_LEVEL():
                           import numpy as np
from sense_hat import SenseHat

sense=SenseHat()



#Level 2

blank2 =         ([0, 0, 0, 0, 0, 0, 0, 0],
                  [2, 2, 2, 2, 2, 2, 2, 0],
                  [0, 2, 0, 0, 0, 0, 0, 0],
                  [0, 2, 0, 2, 0, 2, 2 ,2],
                  [0, 2, 0, 0, 0, 0, 2, 0],
                  [0, 2, 0, 2, 0, 2, 0, 2],
                  [0, 2, 0, 2, 0, 0, 0, 0],
                  [0, 0, 0, 2, 0, 2, 0, 0]
                  )

level2=np.array(blank2)

ballpos = bx, by = 1, 1 # Starting positions

start=sx, sy=0, 0
finish=fx, fy=7, 7



level2[start] = 1
level2[finish] = -1


W=(192 ,192 ,192)#Wall
H=(255, 0, 0)#Hole
F=(255, 255, 0)#Finish
G=(0, 0, 0)#Ground



for i in range(8):
    for j in range(8):
        if level2[i ,j]==2:
            sense.set_pixel(i ,j ,W)
        elif level2[i ,j]==3:
            sense.set_pixel(i ,j ,H)
        elif level2[i ,j]==-1:
            sense.set_pixel(i ,j ,F)
        else:
            sense.set_pixel(i ,j ,G)
            
        

