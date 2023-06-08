import tkinter as tk

''' page est constituer d'un frame consider comme un suport et d'un canvas dans qui la partie utilisable de la page comme une feuille'''

class Page :
#notre constructeur prend en paramettre le parent dans lequelle notre page devra ce trouver puis apelle la fonction __agencement (qui est une fonction privated) ainsi que les couleur et de fond et les couleurs de scroll, la latrgeur initilae et la hauteur initiale
    def __init__(self, parent, larg, haut, couleur_font="black", couleur_scroll= "#707070", largeur_sroll= 9):
        self.__couleur_font= couleur_font
        self.__couleur_scroll= couleur_scroll
        self.__larg_scroll_x = largeur_sroll
        self.__larg_scroll_y= largeur_sroll
        self.__fonction_actualisation_interne= None #au cas ou nous aurons d'autre page interne a initialiser
        self.__agencement(parent, larg, haut)

#cette fonction creera le canvas qui sera notre feuille , les srolls et mettre en place toutes les connections
    def __agencement(self, parent, larg, haut):
        #creationdu support qui est un frame tous en mettant ses epasseurs à 0
        self.__frame_porteur= tk.Frame(parent, highlightthickness= 0, bd= 0)
        #creation du canvas feuille
        self.__feuille= tk.Canvas(self.__frame_porteur, bd=0, background= self.__couleur_font, highlightthickness=0)
        #creation des scrolles tout en connectant le scroll tel que les mouvement du scroll fait bouger la feuille soit vers le haut soit vers le bas 
        self.__scroll_x= tk.Scrollbar(self.__frame_porteur, highlightthickness= 0, troughcolor= self.__couleur_font,activebackground= self.__couleur_scroll, orient=tk.HORIZONTAL, command= self.__feuille.xview, bd=0, bg= self.__couleur_font)
        self.__scroll_y= tk.Scrollbar(self.__frame_porteur, highlightthickness= 0, troughcolor= self.__couleur_font,activebackground= self.__couleur_scroll, orient=tk.VERTICAL, command= self.__feuille.yview, bd=0, bg= self.__couleur_font)
        #connection de la taille de la feuille tel que lorsque la feuille change  alors les longeurs des srolls sont modifiées
        self.__feuille.configure(xscrollcommand= self.__scroll_x.set , yscrollcommand=self.__scroll_y.set ,scrollregion=(0,0,0,0))
        #on rend visible les elt
        self.__scroll_x.pack(side=tk.BOTTOM , fill= tk.X)
        self.__feuille.pack(side=tk.LEFT)
        self.__scroll_y.pack(side=tk.RIGHT , fill= tk.Y)
        #nous aux fonctions ecouteur d'evement
        self.__feuille.bind("<Enter>",self.__montre_scroll)
        self.__feuille.bind("<Leave>",self.__cache_scroll)
        #nous dennons les tailles aux elements de la pages
        self.change_taille(larg, haut)
        #nous donnons les tailles aux scrolls
        self.__scroll_x.configure(width=self.__larg_scroll_x)
        self.__scroll_y.configure(width=self.__larg_scroll_y)  

#les getteurs 
    def get_feuile(self) :
        return self.__feuille
           #fonction qui contient les frames
    def get_support(self) :
        return self.__frame_porteur

#les setter fonction d'ecoute
    def set_fonction(self, fonction):
        self.__fonction_actualisation_interne= fonction         

#recuper une couleur puis donne cette couleur aux scroll
    def __change_couleur_scroll(self,couleur) :
        self.__scroll_x.configure(background= couleur)
        self.__scroll_y.configure(background= couleur)

#ecoute un evemment et cache les scrolls en lui donnans la couleur de font a celle des scrolls
    def __cache_scroll(self,e) :
        self.__change_couleur_scroll(self.__couleur_font)

#ecoute un evenement et montre les scrolls en donnant une couleur distinctif aux srolls
    def __montre_scroll(self,e) :
        self.__change_couleur_scroll(self.__couleur_scroll)

#fonction de changement de taille de la page
    def change_taille(self, largeur, hauteur) :
        self.__frame_porteur.configure(width = largeur, height= hauteur) 
        if(largeur> self.__larg_scroll_x and hauteur> self.__larg_scroll_y):
            larg_feuille = largeur - self.__larg_scroll_x
            haut_feuille = hauteur - self.__larg_scroll_y
            self.__feuille.configure(width = larg_feuille, height= haut_feuille)
            if(self.__fonction_actualisation_interne != None):
                self.__fonction_actualisation_interne()

#change taille scroll x
    def change_larg_scroll_x(self, larg):
        self.__larg_scroll_x= larg 
        haut_feuille = self.__frame_porteur.cget("height")- larg
        #nous modifions les taille de la feuille
        self.__feuille.configure(height= haut_feuille)
        self.__scroll_x.configure(width=self.__larg_scroll_x)

#change taille scroll y
    def change_larg_scroll_y(self, larg):
        self.__larg_scroll_y= larg 
        larg_feuille = self.__frame_porteur.cget("width")- larg
        #nous modifions les taille de la feuille
        self.__feuille.configure(width = larg_feuille) 
        self.__scroll_y.configure(width=self.__larg_scroll_y)                           
        
#fonction qui change la largeur des scroll
    def change_largeur_scroll(self, larg):
        #premiererement nous initilaiseons la largeur des scrolls
        self.__larg_scroll_x= larg
        self.__larg_scroll_y= larg  
        #nous modifions les taille de la feuille
        larg_feuille = self.__frame_porteur.cget("width")- larg
        haut_feuille = self.__frame_porteur.cget("height")- larg
        self.__feuille.configure(width = larg_feuille, height= haut_feuille) 
        self.__scroll_x.configure(width=self.__larg_scroll_x)
        self.__scroll_y.configure(width=self.__larg_scroll_y)
        self.__scroll_x.pack()
        self.__scroll_y.pack() 
        self.__feuille.pack()

        
        