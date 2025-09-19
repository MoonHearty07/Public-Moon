from time import sleep
from os import system
from winsound import Beep

notes = {'C' : 1635,
         'D' : 1835,
         'E' : 2060,
         'G' : 2450,
         'A' : 2750,
         'B' : 3087,
         ' ' : 37}

melodie = "EDCB GA C AG EDCB GA C"

def pomodoro(n, naming):
    for i in range(n):
        m_t = 25
        s_t = 0
        m_r = 5
        s_r = 0
        gogo = True
        while gogo:
            print(f"The task is : {naming}, part {i+1}/{n}")
            print(f'Il vous reste : {m_t} minutes et {s_t} secondes.')
            sleep(1)
            system('cls') 
            if s_t != 0:
                s_t -= 1
            else:
                s_t = 59
                if m_t != 0:
                    m_t -= 1
                else:
                    gogo = False
                    print(f"Vous avez terminer {i+1} pomodoro(s) !")
        popo = True
        while popo:
            print(f"The task is : {naming}, pause {i+1}/{n}")
            print(f'Il vous reste : {m_r} minutes et {s_r} secondes.')
            sleep(1)
            system('cls') 
            if s_r != 0:
                s_r -= 1
            else:
                s_r = 59
                if m_r != 0:
                    m_r -= 1
                else:
                    popo = False
                    for note in melodie:
                        Beep(notes[note], 100)
                    print(f"Vous avez terminer {i+1} pomodoro(s) entier et peut-être aussi la tâche {naming} ! Bravo !")


run = True

while run:
    ask = input("Do you want to add a task ? (yes or no) ")
    print("")
    still = True
    if ask == "yes":
        while still:
            name = input("What is the name of the task ? ")
            print("")
            timing = int(input("Combien de tomates (25/5) voulez-vous prendre ? "))
            print("")
            ask_start = input("Voulez-vous commencer ? (yes or no) ")
            if ask_start == "yes":
                pomodoro(timing, name)
                still = False
            elif ask_start == "non":
                print("Passez une bonne journée alors !")
                print("")
            else:
                print("Mais barrez-vous... J'en ai marre de ce boulot...")
                print("")
    else:
        print("Ah euh d'accord... Bonne journée alors !")
        print("")
        run = False
