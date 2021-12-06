# Imporer brukte biblioteker
from sense_hat import SenseHat
import time
import datetime

sense = SenseHat()


# Denne funskjonen tar inn et heltall og returnerer en tilhoerende 8x8 matrise med baneelementer
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
                 [4, 2, 0, 0, 0, 0, 0, 0],
                 [0, 2, 0, 3, 0, 2, 2 ,2],
                 [0, 2, 0, 0, 0, 0, 0, 0],
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
                [0, 2, 0, 0, 0, 2, 0, 4],
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
    if level == 8: 
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
    
# Denne funksjonen tar inn en score og printer en melding paa skjermen med scoren.
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

# Denne funksjonen tar inn en score og viser en melding og en animasjon
def Victory(score):
    sense.clear
    sense.show_message("You Win!",scroll_speed=0.02,text_colour=[128,128,128])
    sense.show_message("Your score: "+ str(score),scroll_speed=0.02,text_colour=[128,128,128])
    print_score(score)
    for i in range (0,24):
        choice="Victoryscreen"+str(i)+".png"
        sense.load_image(choice)
        time.sleep(0.05)

def ori():                                                                                 #Funksjonen henter sensordata fra gyroskopet og returnerer en liste med en x og en y verdi.
    orientation = sense.get_orientation()                                                  
    roll = (orientation.get("roll"))                                                       #roll er en vinkel fra 0 til 360 grader, om y aksen til Sense Haten.
    pitch = (orientation.get("pitch"))                                                     #pitch er en vinkel fra 0 til 360 grader, om x aksen. 
  
    x = 0                                                                                  #gir x en verdi mellom -10 og 10 ut i fra vilken verdi roll har.
    if (roll <= 90):                                                                       #hvis roll vinklelen er over 90/-90 (under 270) blir verdien av x = 0
        x = (10 / 90) * roll
    elif (270 <= roll):
        x = (10 / 90) * (roll - 360)
    
    y = 0                                                                                  #gir y en verdi mellom -10 og 10 ut i fra vilken verdi pitch har.
    if (pitch <= 90):                                                                      #hvis pitch vinklelen er over 90/-90 (under 270) blir verdien av y = 0
        y = (10 / 90) * pitch
    elif (270 <= pitch):
        y = (10 / 90) * (pitch - 360)
        
    return [x, y]                           
        
    
