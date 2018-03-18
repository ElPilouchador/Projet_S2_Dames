try:  # ici on verfie que l'utlisateur a tkinter malgré qu'il soit installé par defaut
    from tkinter import Tk, Canvas
    from itertools import product  # fonction ainsi que la librairie trouvé dans
    # des forums, celle-ci permet de faire l'effet d'une boucle for mais plus
    # simplement
except:
    print("Attention tkinter n'est pas installé sur installation python")
    print("Or tkinter est une librairie par defaut depuis python 3.0.0")
    print("cela est peut-etre du a une installation personnalisée")
    print("cette installation ne peut-etre considérée comme Par Defaut")
    print("nous vous recommandons d'installer python normalement.")
    print("Le programme se lancera normalement si tkinter est présent")


# Creation d'une classe
# aide sur les classes trouvée sur la documentation python
# ainsi que sur divers forum
#la classe permet de regrouper plusieurs def dans un def "general"
#ce qui facilite l'écriture et la lisibilité du programme
class Tableau(Tk):
    def __init__(self, width, height, taille_case):  # initialision principale
        Tk.__init__(self)  # fonction initialisation de tkinter
        self.taille_case = taille_case  # la fonction self est utlisée pour les classes
        # creation d'un canvas pour tkinter
        self.canvas = Canvas(self, width=width, height=height)
        self.canvas.bind("<Button-1>", self.onclick)
        self.canvas.pack()  # pack pour permettre a tkinter de bien le lire

    def draw_rectangle(self, x1, y1, x2, y2, color):  # case de la table logique
        self.canvas.create_rectangle(
            x1, y1, x2, y2, fill=color, outline="black")

    def draw_circle(self, x1, y1, x2, y2, color):  # pion
        self.canvas.create_oval(x1, y1, x2, y2, fill=color, outline="black")

    def onclick(self, event):  # evenement click trouvé sur des forums
        # on detecte si le joueur clique un case
        i = int(event.x / self.taille_case)
        j = int(event.y / self.taille_case)
        print("Vous avez cliqué sur (%s, %s)" % (i, j))
    def pions_case(self, case):
        
        pass

    def est_dans_grille(self, event): #on verifie que le pion est dans la grille
        #on reprend la detection de clics de la fonction précedente
        i = int(event.x / self.taille_case)
        j = int(event.y / self.taille_case)
        assert j>=0 or i>= 0, "Aie, cette case n'est pas sur la grille"
        #cette assert verifie si le joueur a cliqué sur une case qui existe
#fin classe


#programme principal
if __name__ == "__main__":  # permet a python d'executer cette partie
    taille = 40
    board = Tableau(400, 400, taille)
    board.title("Dames")
    table_logique = [[0, -1, 0, -1, 0, -1, 0, -1, 0, -1],
                     [-1, 0, -1, 0, -1, 0, -1, 0, -1, 0],
                     [0, -1, 0, -1, 0, -1, 0, -1, 0, -1],
                     [-1, 0, -1, 0, -1, 0, -1, 0, -1, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                     [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                     [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                     [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]
# dans notre table a l'aide de listes de liste, on représente l'echiquier
# ainsi si l'on recontre un -1 ou un 1 on placeras alors nos pions
    for (i, j) in product(range(10), range(10)):#on demarre le placement des cases
        coord_x_1 = (i * taille) #on crée notre echiquier de maniere graphique
        coord_y_1 = (j * taille)
        coord_x_2 = coord_x_1 + taille
        coord_y_2 = coord_y_1 + taille
        color = "white" if i % 2 == j % 2 else "black" #on alterne une case /2  
        board.draw_rectangle(coord_x_1, coord_y_1, coord_x_2, coord_y_2, color)
        cell = table_logique[i][j]
        if cell != 0: #on verifie ou placer nos pions
            couleur_pion = "red" if cell > 0 else "blue"
            board.draw_circle(coord_x_1, coord_y_1, coord_x_2, coord_y_2, couleur_pion)
    board.resizable(False, False) #on empeche de modifier la fenetre
    board.mainloop() #lancement de Tkinter


#il n'y a pas encore la gestion totale du jeu
#certaines parties du programme viennent de divers forums, notamment l'idée de classe.
#Mais une inteface graphique est présente avec la detection du pointeur sur une case
