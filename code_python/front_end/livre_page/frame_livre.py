import front_end.livre_page.page as Page

''' ici nous voulons reunir plusieurs pages dans une seule au seins d'une meme frame qui donneras sa taille à la page visible et le reste devrons etre reduire pour se cacher drrierer cele visible on pourra des lors ajouter pluisuers page toute en leur donnat un identifiant livre_frame devra contenir au moins une page'''

class frame_livre :
# le constructeur prend en parametre le parent, les dimension du livre , le nom et les elt neccessaires pour la creation de la premeire page ensuite cree le dictionnaire qui devra les contenir et la premeire  page
    def __init__(self, parent, larg, haut, nom_premiere_page, couleur_font="#EEEEEE", couleur_scroll= "#707070", largeur_sroll= 7):
        self.__frame_conserveur: Page.tk.Frame = Page.tk.Frame(parent, width= larg, height= haut)
        self.__ensemble_page_interne= {}
        self.__page_courante= None
        self.__page_courante= self.cree_nouvelle_page(nom_premiere_page, couleur_font, couleur_scroll, largeur_sroll)
        self.__actualiser_page_courante()

#prend en parametre les elt d'une page et son identifiant puis la cree si aucune page ne pocede cette identifiant et la retourne
    def cree_nouvelle_page(self, nom_page: str, couleur_font="black", couleur_scroll= "gray", largeur_sroll= 9)-> Page.Page:
       if(not nom_page in self.__ensemble_page_interne):
            elt_page= Page.Page(self.__frame_conserveur, 0, 0, couleur_font, couleur_scroll, largeur_sroll)
            elt_page.get_support().place(x= 0, y= 0)
            self.__ensemble_page_interne[nom_page]= elt_page
            self.__actualiser_page_courante()
            return elt_page
       return None            

# donne a la page courante la taille du conserveur
    def __actualiser_page_courante(self):
        if(self.__page_courante != None):
          self.__page_courante.change_taille(self.__frame_conserveur.cget("width"), self.__frame_conserveur.cget("height"))
          self.__page_courante.get_support().place()
          self.__page_courante.get_support().tkraise()

#ici on veut mettre une autre page au dessus alors on reduire celui courant et on agrandit celui selectioner
    def changer_page(self, nom_nouvelle_page):
        if(nom_nouvelle_page in self.__ensemble_page_interne):
             nouvelle_page: Page.Page = self.__ensemble_page_interne[nom_nouvelle_page]
             if(nouvelle_page!= self.__page_courante):
                #nous  changeaons la page courante
                ancien_courant: Page.Page = self.__page_courante
                self.__page_courante= nouvelle_page
                #nous l'agrandissons puis nous la mettons au dessus
                self.__actualiser_page_courante()
                self.__page_courante.get_support().tkraise()
                #nous reduissons l'acien page 
                ancien_courant.change_taille(0, 0)
                ancien_courant.get_support().place()
                return True 
        return False        

#on prend en parametre le nom(identifiant d'une page) et on la retourne si elle existe
    def get_page(self, nom_page)-> Page.Page:
        if(nom_page in self.__ensemble_page_interne):
            return  self.__ensemble_page_interne[nom_page] 
        return None    

#recuperation de la frame support
    def get_frame_conserveur(self)-> Page.tk.Frame:
        return self.__frame_conserveur                 

#nous prennons en paramettre les dimensions et change les dimmensions du support et de la page courante
    def change_taille(self, largeur, hauteur):
        self.__frame_conserveur.configure(width = largeur, height= hauteur)
        self.__actualiser_page_courante()        