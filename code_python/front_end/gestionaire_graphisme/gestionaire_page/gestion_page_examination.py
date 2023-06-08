from front_end.livre_page.page import Page
from front_end.gestionaire_graphisme.gestionaire_page.gestion_page_tableau import gestion_page_tableau
from front_end.gestionaire_graphisme.gestionaire_page.fonction_creation_elt_dans_feuille import fonction_creation_elt_page

class gestion_page_examination:
    def __init__(self, la_page: Page, couleur_ligne, couleur_entete, police_2, police_3) -> None:
        self.__la_page= la_page
        self.__largeur_scroll= 6
        la_page.change_largeur_scroll(0)
        self.__tab_fonction= [None, None]
        la_page.get_support().configure(bd=1, background=couleur_ligne)
        x, y= self.__initialise(police_2)
        y= self.__cree_page_info(x, y, police_3, couleur_entete, couleur_ligne)
        self.__cree_bouton_ajout(y, couleur_ligne, police_3)
        self.__la_page.set_fonction(self.__accomode)

    def set_tab_in(self, tab):
        self.__page_information.set_tab_info(tab)   

    def get_ligne_select(self):
        return self.__page_information.get_ligne_select() 

    def enlever_ligne(self):
        self.__page_information.enlever_ligne()       

    def ajout_ligne_in(self, ligne_in):
        self.__page_information.ajout_ligne(ligne_in)  

    def set_fonction(self, indice, fonction):
        self.__tab_fonction[indice]= fonction 

    def __execute_fonction(self, indice):
        fonction= self.__tab_fonction[indice]
        if(fonction != None):
            fonction()    

    def __initialise(self, police_2):
        self.__feuille= self.__la_page.get_feuile()
        self.__larg_min= 900
        self.__haut_min= 350
        self.__feuille.configure(scrollregion=(0, 0, self.__larg_min, self.__haut_min))
        #-------------------------------------------------------
        x= 0
        y=10
        self.__id_titre= self.__feuille.create_text(x,  y, text="EXAMINATION", font=police_2, anchor="nw")  
        #--------------------------------------------------------------------------
        y= self.__feuille.bbox(self.__id_titre)[3]+ 15
        return x, y

    def __cree_page_info(self, x, y, police_3, couleur_entete, couleur_ligne)  :
        self.__ecart_bord_x_3= 10
        self.__ecart_bord_y_3= 10
        x+= self.__ecart_bord_x_3
        y+= self.__ecart_bord_y_3
        self.__hauteur_page_info= 230
        self.__page_information= gestion_page_tableau(self.__feuille, x, y, ["Nom du médecin","Date", "Heure debut", "Heure fin", "Type examen", "Remarque",  "Résultat", "Prescription"], police_3, couleur_entete, couleur_ligne)    
        return y+ self.__hauteur_page_info

    def __cree_bouton_ajout(self, y, couleur_ligne, police_3):
        x= 0
        y += 20
        haut_bout= 35
        larg_bout= 280
        self.__id_bouton= "bout_ajout"
        bout_ajout= fonction_creation_elt_page.cree_bouton(self.__feuille, x, y, larg_bout, haut_bout, [self.__id_bouton], couleur_ligne, "Ajouter une examination", police_3)
        x= self.__feuille.bbox(self.__id_bouton)[2]+10
        bout_suppression = fonction_creation_elt_page.cree_bouton(self.__feuille, x, y, larg_bout, haut_bout, [self.__id_bouton], couleur_ligne, "Supprimer une examination", police_3)
        bout_ajout.configure(command= lambda: self.__execute_fonction(0))
        bout_suppression.configure(command= lambda: self.__execute_fonction(1))

    def __actualiser_page_utile(self, larg):
        larg -= 2*self.__ecart_bord_x_3
        self.__page_information.changer_taille(larg, self.__hauteur_page_info) 
        
    def __met_au_centre_x(self, id_elt, larg):
        tab_coord= self.__feuille.bbox(id_elt)
        self.__feuille.move(id_elt, larg/2- (tab_coord[0]+ tab_coord[2])/2, 0)

    def __centraliser(self, larg):
       self.__met_au_centre_x(self.__id_titre, larg)
       self.__met_au_centre_x(self.__id_bouton, larg)
       self.__actualiser_page_utile(larg)

    def __accomode(self):
        larg= float(self.__feuille.cget("width"))
        haut= float(self.__feuille.cget("height")) 
        if(larg< self.__larg_min):
            self.__la_page.change_larg_scroll_x(self.__largeur_scroll)
            larg= self.__larg_min
        else:
            self.__la_page.change_larg_scroll_x(0)
        if(haut< self.__haut_min):
            self.__la_page.change_larg_scroll_y(self.__largeur_scroll)
            haut= self.__haut_min
        else:
            self.__la_page.change_larg_scroll_y(0)
        self.__centraliser(larg)
        

