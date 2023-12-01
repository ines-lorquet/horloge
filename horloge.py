import time
def affichage(heure):
    format = "{:02d}:{:02d}:{:02d}".format(heure[0], heure[1], heure[2])
    print(format)

def init_heure():
    heures=int(input("Heure : "))
    minutes=int(input("Minutes : "))
    secondes=int(input("Secondes : "))
    return heures,minutes,secondes

def inti_alarme():
    alarme_heures=int(input("L'heure de votre alarme : "))
    alarme_minutes=int(input("Les minutes de votre alarme : "))
    alarme_secondes=00
    return alarme_heures,alarme_minutes,alarme_secondes

def all():
    affichage_heure=init_heure()
    affichage_alarme=inti_alarme()

    while True:
        affichage(affichage_heure)
        time.sleep(1)
        affichage_heure = (affichage_heure[0], affichage_heure[1], affichage_heure[2]+1)

        if affichage_heure[2]==60:
            affichage_heure = (affichage_heure[0], affichage_heure[1]+1, 0)

        if affichage_heure[1]==60:
            affichage_heure = (affichage_heure[0]+1, 0, 0)
        
        if affichage_heure[0]==24:
            affichage_heure = (0, affichage_heure[1], affichage_heure[2])

        if affichage_alarme==affichage_heure:
            print(" || ALARME || ")
all()