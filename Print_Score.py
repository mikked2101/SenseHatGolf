def print_score(score):                     #Funksjon som printer ut score
    with open("yourscore.txt", "w") as fil: #Åpner fil med navn yourscore som tillater å skrive i fil
        fil.write("Score: " + str(score))   #Score blir lagt til i fil

