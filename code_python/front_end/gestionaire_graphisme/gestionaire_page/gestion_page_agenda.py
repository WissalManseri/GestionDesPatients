from front_end.livre_page.page import Page
from front_end.gestionaire_graphisme.gestionaire_page.gestion_page_tableau import gestion_page_tableau
from tkinter.font import Font
from front_end.gestionaire_graphisme.gestionaire_page.fonction_creation_elt_dans_feuille import fonction_creation_elt_page

class gestion_page_agenda:
    def __init__(self, la_page: Page, police_1, police_3, couleur_entete, couleur, couleur_ligne) -> None:
        self.__la_page= la_page
        self.__largeur_scroll= 6
        self.__nom_entete_2= "elt_inter_1"
        self.__tab_fonction = [None, None]
        x,y = self.__initialiser(couleur, couleur_ligne, police_1, police_3)
        self.__cree_page_utile(x, y, police_3, couleur_entete, couleur_ligne)
        self.__feuille.configure(scrollregion=(0,0, self.__larg_min, self.__haut_min))
        self.__la_page.set_fonction(self.__accomode)

    def set_tab_in(self, tab):
        self.__page_information.set_tab_info(tab)   

    def get_ligne_select(self):
        return self.__page_information.get_ligne_select()         

    def set_fonction(self, indice, fonction):
        self.__tab_fonction[indice]= fonction 

    def __execute_fonction(self, indice):
        fonction= self.__tab_fonction[indice]
        if(fonction != None):
            fonction()        
  
    def __initialiser(self, couleur, couleur_ligne, police_1: Font, police_2: Font):
        self.__larg_min= 1200
        self.__haut_min= 450
        self.__feuille= self.__la_page.get_feuile()
        #-------------------------------------------------
        t= 200
        x= self.__ecart_bord_x_1= 50 
        haut_ecrit= police_1.metrics("linespace")
        y= haut_ecrit+10
        self.__id_titre= self.__feuille.create_text(x+ t/2, y- haut_ecrit/2, text= "Votre AGENDA", font= police_1, anchor="c")
        #---------------------------------------------------
        self.__ecart_bord_y_1= 20
        y += self.__ecart_bord_y_1
        self.__ecart_bord_x_2= 35
        y_ecart_haut_2= 40
        self.__ecart_bord_y_2= 0  
        self.__rect_cadre_1= self.__feuille.create_rectangle(x, y, x+ t, y+ t, fill=couleur, width=0)
        #----------------------------------------------------
        x+= self.__ecart_bord_x_2
        y+= y_ecart_haut_2
        self.__rect_cadre_2= self.__feuille.create_rectangle(x, y, x+ t, y+ t, fill="white", width=0)   
        #---------------------------------------------------
        y += 10
        haut_bout= 35
        larg_bout= 120
        bout_actualiser= fonction_creation_elt_page.cree_bouton(self.__feuille, x, y, larg_bout, haut_bout, [self.__nom_entete_2], couleur_ligne, "actualiser", police_2)
        a= self.__feuille.bbox(self.__nom_entete_2)[2]+20
        bout_traiter = fonction_creation_elt_page.cree_bouton(self.__feuille, a, y, larg_bout, haut_bout, [self.__nom_entete_2], couleur_ligne, "traiter", police_2)
        y= self.__feuille.bbox(self.__nom_entete_2)[3]+10
        bout_actualiser.configure(command= lambda: self.__execute_fonction(0))
        bout_traiter.configure(command= lambda: self.__execute_fonction(1))
        #----------------------------------------------------
        self.__id_trait_bas= self.__feuille.create_line([x, y, x+t, y+t], fill= couleur_ligne)
        return x, y

    def __cree_page_utile(self, x, y, police_3, couleur_entete, couleur_ligne)  :
        self.__ecart_bord_x_3= 10
        self.__ecart_bord_y_3= 10
        x+= self.__ecart_bord_x_3
        y+= self.__ecart_bord_y_3
        self.__page_information= gestion_page_tableau(self.__feuille, x, y, ["Date", "Heure", "Identifiant du patient", "Nom", "Prenom"], police_3, couleur_entete, couleur_ligne) 

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
        tab_coord_indication=  self.__feuille.bbox(self.__nom_entete_2)
        self.__feuille.move(self.__nom_entete_2, (tab_coord[0]+ tab_coord[2])/2- (tab_coord_indication[0]+ tab_coord_indication[2])/2,0)
        tab_trait_bas= [tab_coord[0], tab_coord[3]-1, tab_coord[2], tab_coord[3]-1]
        self.__feuille.coords(self.__id_trait_bas, tab_trait_bas)
        self.__actualiser_page_utile((tab_coord[2]- tab_coord[0]), (tab_coord[3]- tab_coord[1])- (tab_coord_indication[3]- tab_coord_indication[1])-10)

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
