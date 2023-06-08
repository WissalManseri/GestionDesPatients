import front_end.livre_page.frame_livre as livre

''' nous creons une fenetre qui ne pocede qu'une seule frame_livre qui ecoute la modification des dimensions de la fenetre '''

class fenetre_livre:
   
#coordoner de decalage pour que (x_centre, y_centre) soit le centre aprres creation
    def coord_debut_a_partie_du_centre(x_centre, y_centre, larg, haut):
        return x_centre- larg/2, y_centre- haut/2

#coordonner du debut pour que le composant soit au centre du composee
    def coord_mettre_au_centre_du_grand(larg_grand, haut_grand, larg_petit, haut_petit, x_grand=0, y_grand= 0):
        x_grand+= (larg_grand - larg_petit)/2
        y_grand+= (haut_grand- haut_petit)/2
        return x_grand, y_grand

#notre constructeur prend les pourcentage x et y pour creer la fenetre en prenant la longeur et la largeur les pourcentage des dimmension de l'ecran qui l'eberge ainsi peut importe la taille de l'ecran elle s'ouvrira normalement
#apres creationde la fenetre appaele la fonction __agenecement
    def __init__(self, pourcentage_x, pourcentag_y, nom_premire_page, couleur):
        self.__fen= livre.Page.tk.Tk()
        self.__fen.title("Gestion Des Patients")
        self.__agencement(pourcentage_x, pourcentag_y, nom_premire_page, couleur)

    def set_icone(self, photo_icone):
         self.__fen.iconphoto(False, photo_icone)

#ici on contruit l'interieur de la fentre du moins on mets les fondations
    def __agencement(self, pourcentage_x, pourcentag_y, nom_premire_page, couleur):
        #prise des different taille utile
        larg_ecran= self.get_largeur_ecran()
        haut_ecran= self.get_hauteur_ecran()
        larg_fen= (larg_ecran * pourcentage_x) // 100
        haut_fen= (haut_ecran* pourcentag_y) // 100
        #nous mettrons notre fenetre au centre a la primeire ouverture alors 
        a, b= fenetre_livre.coord_mettre_au_centre_du_grand(larg_ecran, haut_ecran, larg_fen, haut_fen)
        posit_x= int(a)
        posit_y= int(b)
        #nous donnons la taille et les coordonnees initiale de la fenetre
        self.__fen.geometry(f"{larg_fen}x{haut_fen}+{posit_x}+{posit_y}")
        #nous creons le frame qui ne contiendra rien mais sera qui nous permetra d;ecouter les rdimentionenment de la fenetre
        frame_ecouteur= livre.Page.tk.Frame(self.__fen, width= 0, height= 0 , bd=0)
        frame_ecouteur.pack(expand= True)
        #creation de la frame_livre prmeirere
        self.__frame_livre_originale= livre.frame_livre(self.__fen, larg_fen, haut_fen, nom_premire_page, couleur)
        self.__frame_livre_originale.get_frame_conserveur().place(x=0,y=0)
        #nous creons le manipulateur de feuille
        frame_ecouteur.bind("<Configure>", self.__accomodation)

#cette fonction ne doit etre appele qu'a la fin de tous les instruction de l'appliquation ou du moins la partie de qui seras reliee d'une quelconque maniere a la fenetre
    def lancer_la_boucle_execution_de_la_fentre(self):
        self.__fen.mainloop()  

#recuperation de la fenetre
    def get_fenetre(self):
        return self.__fen     

#nous retournons le socle de la fenetre
    def get_frame_livre_originale(self):
        return self.__frame_livre_originale

#ceci nous donne la taille de l'ecran qui contiendra la fenetre
    def get_largeur_ecran(self) :
        return self.__fen.winfo_screenwidth() 

#pour la largeur de la fenetre
    def get_largeur_fenetre(self) :
        return self.__fen.winfo_width() 

#pour la hauteur de la fenetre
    def get_hauteur_fenetre(self) :
        return self.__fen.winfo_height()    

#pour la position x de la fenetre
    def get_positon_x_fenetre(self):
       return self.__fen.winfo_rootx()         

#pour la position y de la fenetre
    def get_positon_y_fenetre(self):
       return self.__fen.winfo_rooty()                 

#ceci nous donne la taille de l'ecran qui contiendra la fenetre
    def get_hauteur_ecran(self) :#en pixel 
        return self.__fen.winfo_screenheight() 

#coordonnee centre de la fenetre
    def get_coord_centre_fen(self, larg, haut):
        x, y= fenetre_livre.coord_mettre_au_centre_du_grand(self.get_largeur_fenetre(), self.get_hauteur_fenetre(), larg, haut, self.get_positon_x_fenetre(), self.get_positon_y_fenetre())
        return int(x), int(y)

#ecoute le redimensionement de la fenetre
    def __accomodation(self, e):
        larg= self.get_largeur_fenetre()
        haut= self.get_hauteur_fenetre()
        self.__frame_livre_originale.change_taille(larg, haut)   
        self.__frame_livre_originale.get_frame_conserveur().place() 