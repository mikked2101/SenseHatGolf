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
    new_level_time=0
    levelstart= pygame.time.get_ticks
    seconds=(pygame.time.get_ticks-levelstart)/1000
    seconds-=new_level_time
    if seconds > 40:
        GAMEOVER(score)
    return seconds


def nextlevel(level):
    if level == 1:
    
        return  ([0,2,0,0,0,2,0,1],
                 [0,0,0,2,0,0,0,0],
                 [0,2,2,2,2,2,2,2],
                 [0,0,0,0,0,0,0,0],
                 [3,0,0,3,0,0,3,0],
                 [0,0,0,0,0,0,0,0],
                 [2,2,2,2,2,2,2,0],
                 [-1,0,0,0,0,0,0,0]
                 )
    if level == 2:
        return  ([1, 0, 0, 0, 0, 0, 0, 0],
                 [2, 2, 2, 2, 2, 2, 2, 0],
                 [0, 2, 0, 0, 0, 0, 0, 0],
                 [0, 2, 0, 2, 0, 2, 2 ,2],
                 [0, 2, 0, 0, 0, 0, 2, 0],
                 [0, 2, 0, 2, 0, 2, 0, 2],
                 [0, 2, 0, 2, 0, 0, 0, 0],
                 [0, 0, 0, 2, 0, 2, 0, -1]
                 )



 def LEVELFINISH(seconds):
        sense.clear
        sense.show_message("LEVEL: "+str(current_level)
        sense.show_message("USED TIME: "+str(seconds)
        new_level_time+=seconds
        
                           
        


