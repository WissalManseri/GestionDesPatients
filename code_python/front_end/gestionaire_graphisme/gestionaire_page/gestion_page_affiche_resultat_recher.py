from front_end.livre_page.page import Page
from front_end.gestionaire_graphisme.gestionaire_page.gestion_page_tableau import gestion_page_tableau
from tkinter.font import Font
from front_end.gestionaire_graphisme.gestionaire_page.fonction_creation_elt_dans_feuille import fonction_creation_elt_page

class gestion_page_affichage_resultat_recherche :
    def __init__(self, la_page: Page, police_1, police_3, couleur_entete, couleur, couleur_ligne) -> None:
        self.__la_page= la_page
        self.__largeur_scroll= 6
        self.__tab_elt_spacifique_requete= []
        x,y = self.__initialiser(couleur, couleur_ligne, police_1, police_3)
        self.__cree_page_utile(x, y, police_3, couleur_entete, couleur_ligne)
        self.__feuille.configure(scrollregion=(0,0, self.__larg_min, self.__haut_min))
        self.__la_page.set_fonction(self.__accomode)

    def set_tab_elt_de_requette(self, tab_elt):#tab_elt dois soit contenir des preparer pour les requettes soit etre vide
        self.__tab_elt_spacifique_requete= tab_elt 

    def enlever_ligne(self):
        self.__page_information.enlever_ligne()    

    def get_tab_elt_de_requette(self):
        return  self.__tab_elt_spacifique_requete  

    def __initialiser(self, couleur, couleur_ligne, police_1: Font, police_3):
        self.__larg_min= 800
        self.__haut_min= 500
        self.__feuille= self.__la_page.get_feuile()
        x= self.__ecart_bord_x_1= 50 
        y= self.__ecart_bord_y_1= 20
        self.__ecart_bord_x_2= 35
        self.__ecart_bord_y_2= 0
        t= 200
        self.__rect_cadre_1= self.__feuille.create_rectangle(x, y, x+ t, y+ t, fill=couleur, width=0)   
        haut_ecrit= police_1.metrics("linespace")  
        y+= haut_ecrit+10
        #-------------------------------------------------------------------------
        self.__id_titre= self.__feuille.create_text(x+ t/2, y- haut_ecrit/2, text= "Liste des patients", font= police_1, anchor="c")
        #----------------------------------------------------------------------------------------
        x+= self.__ecart_bord_x_2
        self.__rect_cadre_2= self.__feuille.create_rectangle(x, y, x+ t, y+ t, fill="white", width=0)
        #-----------------------------------------------------------------------
        y+= 15
        larg_bout= 200
        haut_bout= 30
        self.__id_bouton_entete= "id_bout_entete"
        tab_nom_bouton_entete= ["actualiser", "information", "executer", "recherche"]
        a= x
        self.__tab_fonction_bout=[]
        i= 0
        for elt in tab_nom_bouton_entete:
            bout= fonction_creation_elt_page.cree_bouton(self.__feuille, a, y, larg_bout, haut_bout, [self.__id_bouton_entete], couleur_ligne, elt, police_3)
            bout.configure(command= lambda indice= i: self.__execute_fonction(indice))
            a= self.__feuille.bbox(self.__id_bouton_entete)[2]+10
            self.__tab_fonction_bout.append(None)
            i += 1
        y = self.__feuille.bbox(self.__id_bouton_entete)[3]+10   
        #-----------------------------------------------------------------------
        #nous accomodons les coordonees su trait lors des modification de la fenetre
        self.__id_trait_bas= self.__feuille.create_line([0, 0, 0, 0], fill= couleur_ligne)
        return x, y

    def set_fonction_bouton(self, indice, fonction):
        self.__tab_fonction_bout[indice]= fonction 

    def __execute_fonction(self, indice):
        fonction= self.__tab_fonction_bout[indice]
        if(fonction!= None):
            fonction()     
        
    def __cree_page_utile(self, x, y, police_3, couleur_entete, couleur_ligne)  :
        self.__ecart_bord_x_3= 10
        self.__ecart_bord_y_3= 10
        x+= self.__ecart_bord_x_3
        y+= self.__ecart_bord_y_3
        self.__page_information= gestion_page_tableau(self.__feuille, x, y, ["Code", "Nom", "Prenom", "Sexe", "Date de naissance", "Téléphone", "Adresse", "Profession", "Date d'enregistrement"], police_3, couleur_entete, couleur_ligne) 

    def __actualiser(self, larg, haut):
        if(larg< self.__larg_min):
              larg= self.__larg_min
        if(haut< self.__haut_min):
              haut= self.__haut_min     
        tab_coord= self.__feuille.coords(self.__rect_cadre_1)
        larg-= self.__ecart_bord_x_1
        haut -= self.__ecart_bord_y_1
        tab_coord[2]= larg
        tab_coord[3]= haut
        self.__feuille.coords(self.__rect_cadre_1, tab_coord)  
        tab_coord_titre=  self.__feuille.bbox(self.__id_titre)
        self.__feuille.move(self.__id_titre, (tab_coord[0]+ tab_coord[2])/2- (tab_coord_titre[0]+ tab_coord_titre[2])/2,0)
        self.__actualiser_rect_2(larg, haut)    

    def __actualiser_rect_2(self, larg, haut):
        tab_coord= self.__feuille.coords(self.__rect_cadre_2)
        tab_coord[2]= larg- self.__ecart_bord_x_2
        tab_coord[3]= haut-  self.__ecart_bord_y_2
        self.__feuille.coords(self.__rect_cadre_2, tab_coord)  
        tab_coord_id_bouton_entete=  self.__feuille.bbox(self.__id_bouton_entete)
        self.__feuille.move(self.__id_bouton_entete, (tab_coord[0]+ tab_coord[2])/2- (tab_coord_id_bouton_entete[0]+ tab_coord_id_bouton_entete[2])/2,0)
        tab_trait_bas= [tab_coord[0], tab_coord[3]-1, tab_coord[2], tab_coord[3]-1]
        self.__feuille.coords(self.__id_trait_bas, tab_trait_bas)
        self.__actualiser_page_utile((tab_coord[2]- tab_coord[0]), (tab_coord[3]- tab_coord[1])- (tab_coord_id_bouton_entete[3]- tab_coord_id_bouton_entete[1])-10)

    def __actualiser_page_utile(self, larg, haut):
        larg -= 2*self.__ecart_bord_x_3
        haut -= self.__ecart_bord_y_3+ 40
        self.__page_information.changer_taille(larg, haut)  

    def __accomode(self):
        larg= float(self.__feuille.cget("width"))
        haut= float(self.__feuille.cget("height"))  
        if(larg< self.__larg_min):
            self.__la_page.change_larg_scroll_x(self.__largeur_scroll)
        else:
            self.__la_page.change_larg_scroll_x(0)
        if(haut< self.__haut_min):
            self.__la_page.change_larg_scroll_y(self.__largeur_scroll)
        else:
            self.__la_page.change_larg_scroll_y(0)
        self.__actualiser(larg, haut)    

    def set_info_utile(self, tab):
        self.__page_information.set_tab_info(tab)     

    def get_ligne_select(self):
        return self.__page_information.get_ligne_select()              
        