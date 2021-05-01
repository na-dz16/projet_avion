################################
#Information sur le Groupe
#MIASHS L1S2 TD1
#Groupe 2
#Projet_avion
#Yannis KYRIASIS
#Nadir HADEOUI
#Ismael AYAD
#Oumou ATJI
#https://github.com/uvsq22004651/projet_avion/edit/main/incendie.py
################################

################################ Fonctionnement du programme


################################# IMPORTATIONS DE LIBRAIRIES
import tkinter as tk

################################ INITIALISATION
screen = tk.Tk()
screen.title("avion")

################################# CONSTANTES
SIEGES_VIDES = "steel blue"
COULOIR = "light steel blue"
ZERO_BAGEGE = "yellow"
UN_BAGAGE = "orange"
DEUX_BAGAGES = "red"
SIEGES_OCCUPEES = "green"
LARGEUR = 140
HAUTEUR = 600
# la longeur des carrés qui constituent le quadrillage
COTE = 20
NB_COl = LARGEUR // COTE
NB_LINE = HAUTEUR // COTE

tableau = None

################################# FONCTIONS
def sieges_couloir():
    global COTE, SIEGES_VIDES, COULOIR
    """Création des sièges et du couloir de l'avion"""
    for i in range (7):
        for j in range (30):
                carré = canvas.create_rectangle(i*COTE, j*COTE, (1+i)*COTE, (1+j)*COTE, fill = SIEGES_VIDES)
                if i == 3:
                    canvas.itemconfig(carré, fill = COULOIR)

def coordonnées_lignes_colonnes():
    """Fonction qui retourne la colonne et la ligne dans l'avion
    grâce aux coordonnées de x et y"""
    return x // COTE, y // COTE


def tableau_2D():
    """Création d'un tableau à deux dimension permettant de connaître
    le rôle de chaque celule, le couloir est initilisé à 0, tandis 
    que les sièges sont initialisés à 1"""
    global tableau
    tableau = []
    for i in range(NB_COl):
        if i == 3:
            tableau.append([0]*NB_LINE) #couloir
        else:
            tableau.append([1]*NB_LINE) #sièges


def voisins():
    """Retourne si un passager à un voisin devant ou derrière lui
    dans le couloir de l'avion"""


################################# PROGRAMME PRINCIPALE 
canvas = tk.Canvas(screen, width = 140, height = 600, borderwidth=0, highlightthickness=0, bg = "black")

case1 = tk.Button(screen, text="  ", bg="yellow")
label1 = tk.Label(screen, text="ZERO BAGAGE")

case2 = tk.Button(screen, text="  ", bg="orange")
label2 = tk.Label(screen, text="UN BAGAGE")

case3 = tk.Button(screen, text="  ", bg="red")
label3 = tk.Label(screen, text="DEUX BAGAGES")

case4 = tk.Button(screen, text="  ", bg="steel blue")
label4 = tk.Label(screen, text="SIEGES VIDES")

case5 = tk.Button(screen, text="  ", bg="green")
label5 = tk.Label(screen, text="SIEGES OCCUPEES")

sieges_couloir()


################################# PLACEMENT DES WIDGETS
canvas.grid(column = 0, row = 0, rowspan=5)

case1.grid(column=1, row=0)
label1.grid(column=2, row=0)

case2.grid(column=1, row=1)
label2.grid(column=2, row=1)

case3.grid(column=1, row=2)
label3.grid(column=2, row=2)

case4.grid(column=1, row=3)
label4.grid(column=2, row=3)

case5.grid(column=1, row=4)
label5.grid(column=2, row=4)


################################# FIN DE LA BOUCLE
screen.mainloop()