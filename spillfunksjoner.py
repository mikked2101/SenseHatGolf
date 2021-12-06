from sense_hat import SenseHat
import time
import datetime

sense = SenseHat()


def nextlevel(level):

    if level == 0:
    
        return  ([0,0,0,0,0,0,0,2],
                 [0,1,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0,0],
                 [3,0,0,0,0,0,0,-1]
                 )


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

    if level == 3:
        return ([2, 0, 4, 0, 2, 2, 0, -1],
                [0, 2, 0, 0, 0, 0, 0, 0],
                [0, 0, 3, 0, 0, 3, 0, 2],
                [0, 0, 0, 0, 0, 0, 0, 2],
                [2, 0, 0, 0, 0, 0, 0, 0],
                [2, 0, 3, 0, 0, 3, 0, 4],
                [0, 0, 0, 0, 0, 0, 2, 0],
                [1, 0, 2, 2, 0, 0, 0, 2])
    
    if level == 4:
        return ([0, 3, 0, 0, 0, 3, 0, 3],
                [0, 0, 0, 3, 0, 0, 0, 0],
                [0, 3, 2, 2, 0, 2, 0, 3],
                [0, 2, 0, 0, 0, 2, 0, 0],
                [0, 2, 0, 3, 3, 0, 2, 2],
                [0, 2, 0, 0, 0, 0, 0, 0],
                [0, 2, 2, 2, 2, 3, 0, 3],
                [1, 2, -1, 0, 0, 0, 0, 0]) 

    if level == 5:
    
        return  ([3,0,0,0,0,0,0,3],
                 [0,0,2,0,3,2,0,3],
                 [0,3,2,0,3,2,0,0],
                 [0,0,2,0,0,2,3,0],
                 [3,0,2,3,0,2,0,0],
                 [-1,0,2,0,0,2,3,4],
                 [3,3,2,0,3,2,3,3],
                 [1,0,0,0,0,0,0,3]
                 )
    if level == 6:
    
        return  ([1,2,3,3,3,3,3,3],
                 [0,2,-1,0,0,0,0,0],
                 [0,2,2,3,2,2,3,0],
                 [0,2,0,0,0,0,0,0],
                 [0,2,0,3,2,2,3,2],
                 [0,2,0,0,0,0,0,4],
                 [0,3,2,2,3,3,0,3],
                 [0,0,0,0,0,0,0,0]
                 )
    if level == 7:
    
        return  ([1,2,-1,0,0,0,0,3],
                 [0,2,2,2,2,2,0,0],
                 [0,2,3,3,3,3,3,0],
                 [0,2,3,3,2,0,0,0],
                 [0,2,0,4,3,0,3,3],
                 [0,2,0,0,2,0,0,0],
                 [0,2,0,3,3,3,3,0],
                 [0,0,0,0,0,0,0,0]
                )
    if level == 8: #Anders bane 1
        return ([1, 0, 0, 2, 0, 0, 0, 3],
                [2, 2, 0, 2, 0, 2, -1, 0],
                [0, 0, 0, 2, 0, 2, 2, 2],
                [0, 2, 2, 2, 0, 0, 0, 0],
                [0, 2, 0, 0, 0, 2, 2, 0],
                [0, 2, 0, 2, 0, 2, 4, 0],
                [0, 0, 0, 2, 0, 2, 0, 0],
                [3, 2, 2, 2, 0, 0, 0, 3]) 

    if level == 9:
        return ([0, 0, 0, 0, 0, 0, 3, -1],
                [0, 3, 2, 2, 2, 0, 2, 0],
                [0, 0, 2, 1, 2, 0, 2, 0],
                [3, 0, 0, 0, 2, 0, 2, 0],
                [2, 2, 2, 3, 2, 0, 2, 0],
                [0, 0, 0, 0, 0, 0, 2, 0],
                [0, 3, 2, 2, 2, 3, 2, 0],
                [0, 0, 0, 0, 0, 0, 0, 4]) 


"""def get_positions(level):
    holepos = []
        
        for i in range(8):
            for j in range(8):
                if level[i, j] == 1:
                    bx = i
                    by = j
                elif level[i, j] == 3:
                    holp.append([i, j])
                elif level[i, j] == -1:
                    golp = [i, j]
    return {ballpos: [bx, by], holepos : holp, goalpos, golp]}"""
    


def GAMEOVER(score = ""):
    sense.clear
    sense.show_message("GAME OVER", 0.02)
    time.sleep(0.1)
    sense.show_message("Your score: "+ str(score), 0.02)
    time.sleep(0.1)


def print_score(score):                                                                     #Funksjon som printer ut score og dato
    now = datetime.datetime.now()                                                           #datoen og tiden akkurat nå
    now1 = now.strftime("%d-%m-%Y %H:%M:%S")                                                #finere format av dato og tid
    with open("yourscore.txt", "a") as fil:                                                 #AApner fil med navn yourscore som tillater aa skrive i fil
        fil.write("\n" + "Current date and time: " + str(now1) + " Score: " + str(score))   #Score blir lagt til i fil med dato
        
def Victory(score):
    sense.clear
    sense.show_message("You Win!",scroll_speed=0.02,text_colour=[128,128,128])
    sense.show_message("Your score: "+ str(score),scroll_speed=0.02,text_colour=[128,128,128])
    print_score(score)
    for i in range (0,24):
        choice="Victoryscreen"+str(i)+".png"
        sense.load_image(choice)
        time.sleep(0.05)

def ori():
    orientation = sense.get_orientation()
    roll = (orientation.get("roll"))
    pitch = (orientation.get("pitch"))
  
    x = 0
    if (roll <= 90):
        x = (10 / 90) * roll
    elif (270 <= roll):
        x = (10 / 90) * (roll - 360)
    
    y = 0
    if (pitch <= 90):
        y = (10 / 90) * pitch
    elif (270 <= pitch):
        y = (10 / 90) * (pitch - 360)
        
    return [x, y]                           
        
    
