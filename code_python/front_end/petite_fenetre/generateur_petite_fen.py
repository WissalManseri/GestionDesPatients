import front_end.livre_page.frame_livre as conteneur
import tkinter as tk

class  generateur_petite_fen:
    elt_consever= None
    couleur_ecris= "blue"
    couleur_centre= "#74D1B3"
    __fenetre_ouvert= False#nous allons interdit l'ouverture de plusieurs fenetre
    def __init__(self, fen:tk.Tk):
        self.__fen= fen
        self.__initialise()
        
    def __initialise(self):
        self.__fonction_avant_fermeture= None
        self._page_globale= None
        
    def __generer_fen(self, larg, haut, x, y): 
        generateur_petite_fen.elt_consever= None   
        top= self._top= tk.Toplevel(self.__fen)
        top.geometry(f"{larg}x{haut}+{x}+{y}")
        conteneur_page= conteneur.frame_livre(self._top, larg, haut, "page", generateur_petite_fen.couleur_centre)
        conteneur_page.get_frame_conserveur().place(x=0,y=0)
        self._page_globale= conteneur_page.get_page("page")
        self._page_globale.get_feuile().bind("<Destroy>", self.__signaler_suppresion, "+")

    def fait__attendre(self):
        self._top.wait_window(self._top)#nous faissons atttendre toutes les autre excution jusqu'a la fermeture 

#ici nous 
    def __parametrage_de_connection_a_la_fen_parente(self, bloquer_fen= True):
        if(bloquer_fen):
          #self.top.overrideredirect(True)#pour enlever l'antete
           self._top.grab_set()
        self._top.transient(self.__fen)#nous lions la petite fentre a la grande
        self._top.resizable(width=False, height=False)#nous interdissons le changement de taille
        
#fait les dernieres operations necessaire avant la suppression de la fenetre 
    def __signaler_suppresion(self, e):
        if(self.__fonction_avant_fermeture != None):
            self.__fonction_avant_fermeture()
        self.__initialise()   
        generateur_petite_fen.__fenetre_ouvert= False  
        
#la fonction chargee de creer la fentre
    def _cree_une_petite_fentre(self, x, y, larg, haut, bloquer_fen= True):  
        if(not generateur_petite_fen.__fenetre_ouvert):
            generateur_petite_fen.__fenetre_ouvert= True            
            self.__generer_fen(larg, haut, x, y)
            self.__parametrage_de_connection_a_la_fen_parente(bloquer_fen)
            
