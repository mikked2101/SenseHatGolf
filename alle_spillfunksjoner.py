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
    
        return  ([0, 2, 0, 0, 0, 2, 0, 1],
                 [0, 0, 0, 2, 0, 0, 0, 0],
                 [0, 2, 2, 2, 2, 2, 2, 2],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [3, 0, 0, 3, 0, 0, 3, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [2, 2, 2, 2, 2, 2, 2, 0],
                 [-1, 0, 0, 0, 0, 0, 0, 0]
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
        return ([2, 0, 4, 0, 2, 2, 0, -1]
                [0, 2, 0, 0, 0, 0, 0, 0]
                [0, 0, 3, 0, 0, 3, 0, 2]
                [0, 0, 0, 0, 0, 0, 0, 2]
                [2, 0, 0, 0, 0, 0, 0, 0]
                [2, 0, 1, 0, 0, 1, 0, 4]
                [0, 0, 0, 0, 0, 0, 2, 0]
                [1, 0, 2, 2, 0, 0, 0, 2])



 def LEVELFINISH(seconds):
        sense.clear
        sense.show_message("LEVEL: "+str(current_level)
        sense.show_message("USED TIME: "+str(seconds)
        new_level_time+=seconds
                           
                          
                           
def direction():
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
        
                           
def VictoryScreen():
   sense.show_message("You Win!",scroll_speed=0.02,text_colour=[128,128,128])
   sense.show_message("Your score:0",scroll_speed=0.02,text_colour=[128,128,128])

   for i in range (0,24):
       choice="Victoryscreen"+str(i)+".png"
       sense.load_image(choice)
       time.sleep(0.05)


