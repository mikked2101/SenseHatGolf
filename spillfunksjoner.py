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
    



def GAMEOVER(score = ""):                                                                  #Funksjon som vises naar spilleren faller i et hull
    sense.clear                                                                            #Toemmer skjermer slik at teksten ikke kommer i veien for noe
    sense.show_message("GAME OVER", 0.02)                                                  #Vise teksen "GAME OVER" på skjermen
    time.sleep(0.1)                                                                        #Kort pause
    sense.show_message("Your score: "+ str(score), 0.02)                                   #Vise scoren til spilleren
    time.sleep(0.1)                                                                        #Kort pause før spillet begynner på nytt



def print_score(score):                                                                     #Funksjon som printer ut score og dato
    now = datetime.datetime.now()                                                           #datoen og tiden akkurat naa
    now1 = now.strftime("%d-%m-%Y %H:%M:%S")                                                #finere format av dato og tid
    with open("yourscore.txt", "a") as fil:                                                 #AApner fil med navn yourscore som tillater aa skrive i fil
        fil.write("\n" + "Current date and time: " + str(now1) + " Score: " + str(score))   #Score blir lagt til i fil med dato


        
def Victory(score):                                                                         #Funksjon som dukker opp naar spilleren har klart alle banene                      
    sense.clear                                                                             #Toemmer skjermer slik at teksten ikke kommer i veien for noe
    sense.show_message("You Win!",scroll_speed=0.02,text_colour=[128,128,128])              #Vise teksen "You Win" på skjermen i fargen soelv
    sense.show_message("Your score: "+ str(score),scroll_speed=0.02,text_colour=[128,128,128]) #Vise scoren til spilleren i fargen soelv
    print_score(score)                                                                      #Funksjonen over med scoren til spilleren
    for i in range (0,24):                                                                  #For loekke fra 0 til 23 som brukes til aa vise seierskjermen
        choice="Victoryscreen/Victoryscreen"+str(i)+".png"                                  #Setter hver enkelt bilderamme som en variabel i hver gjennomgang av loekka
        sense.load_image(choice)                                                            #Viser variablen på LED-matrisen til SenseHat'en
        time.sleep(0.05)                                                                    #Kort pause før loopen kjører igjen                                                          



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
        
    
