import tkinter as tk
from tkinter.font import Font
from front_end.livre_page.frame_livre import frame_livre

class gestion_structuration_1:
    def cree_tab_coord_rectangle_arrondie(x1, y1, x2, y2, radius):
      tab = [x1+radius , y1,
                 x1+radius , y1,
                 x2-radius , y1,
                 x2-radius , y1,
                 x2 , y1,
                 x2 , y1+radius,
                 x2 , y1+radius,
                 x2 , y2-radius,
                 x2 , y2-radius,
                 x2 , y2,
                 x2 - radius,y2,
                 x2 - radius,y2,
                 x1 + radius,y2,
                 x1 + radius,y2,
                 x1,y2,
                 x1 , y2 - radius,
                 x1 , y2 - radius,
                 x1 , y1 + radius,
                 x1 , y1 + radius,
                 x1,y1] 
      return  tab         

    __hauteur_entete= 120
    __hauteur_pied= 80
    __hauteur_minimale_centre= 400
    __hauteur_polygone_pied= 40
    __espace_entre_block= 20
    __espace_avec_bordure_fenetre= 80
    __espace_entre_logo_titre= 50
    __ecart_largeur_dans_pied= 150
    __raduis_polynome_pied= 30
    __largeur_minimale_fenetre= 900

#nous prenons l'entete comme element plus large
    def largeur_minimale_visibilite():
        return gestion_structuration_1.__largeur_minimale_fenetre

#la hauteur minimale de visbilite
    def hauteur_minimale_visiblilite():
        return gestion_structuration_1.__hauteur_entete+ gestion_structuration_1.__hauteur_minimale_centre+ gestion_structuration_1.__hauteur_pied+ 3* gestion_structuration_1.__espace_entre_block 

    def __init__(self, feuille: tk.Canvas, nom_premiere_page, couleur, police_grand_ecrit, police_petit_ecris, photo, couleur_bordure) :
        self.__feuille= feuille
        self.__largeur_logo= 100
        self.__nom_elt_entete= "dans_entete"
        self.__nom_pied_page= "pied_page"
        self.__creer_entete(couleur, police_grand_ecrit, police_petit_ecris, photo)
        self.__cree_centre_et_pied(nom_premiere_page, couleur_bordure, police_petit_ecris)
        self.__feuille.configure(scrollregion=(0, 0, gestion_structuration_1.largeur_minimale_visibilite(), gestion_structuration_1.hauteur_minimale_visiblilite()))

    def __creer_entete(self, couleur, police_grand_ecrit: Font , police_petit_ecris : Font, photo):
        nom_appli= "APPLICATION DE GESTION DES PATIENTS"
        slogan= "la santé de tous, notre préocupation"
        self._rectangle_entete=  self.__feuille.create_rectangle(0, 0, gestion_structuration_1.__largeur_minimale_fenetre, gestion_structuration_1.__hauteur_entete, fill=couleur, width=0)
        x= (gestion_structuration_1.__largeur_minimale_fenetre)/2 - self.__largeur_logo
        y= gestion_structuration_1.__hauteur_entete/4
        self.__feuille.create_text(x, y, fill= "white", text= nom_appli, font= police_grand_ecrit, anchor= "c", tags=[self.__nom_elt_entete])
        espace= 2
        y+= police_grand_ecrit.metrics("linespace")+ espace
        self.__feuille.create_text(x, y, fill= "black", text= slogan, font= police_petit_ecris, anchor= "c", tags=[self.__nom_elt_entete])
        x+= (police_grand_ecrit.measure(nom_appli)+ self.__largeur_logo) /2+  gestion_structuration_1.__espace_entre_logo_titre 
        self.__feuille.create_image(x, gestion_structuration_1.__hauteur_entete/2, image= photo, tags=[self.__nom_elt_entete])

    def __cree_centre_et_pied(self, nom_premiere_page, couleur_bordure, police_petit_ecris : Font):
        larg= 2
        haut= 2
        x= gestion_structuration_1.__espace_avec_bordure_fenetre
        y= gestion_structuration_1.__hauteur_entete+ gestion_structuration_1.__espace_entre_block
        self.__conteneur_page= frame_livre(self.__feuille, larg, haut, nom_premiere_page, "white")
        self.__cadre_centrale= self.__feuille.create_window(x, y, height= larg, width= haut, window= self.__conteneur_page.get_frame_conserveur(), anchor="nw") 
        y= y+ haut+ gestion_structuration_1.__espace_entre_block
        self.__creer_pied(x, y, larg, couleur_bordure, police_petit_ecris)

    def __creer_pied(self, x, y, larg, couleur_bordure, police_petit_ecris : Font):
        self.__rectangle_pied= self.__feuille.create_rectangle(x, y+ gestion_structuration_1.__hauteur_polygone_pied/2, x+larg,  y+gestion_structuration_1.__hauteur_pied, fill="white", tags=[self.__nom_pied_page], width=0)   
        x+= gestion_structuration_1.__ecart_largeur_dans_pied
        larg-= 2*gestion_structuration_1.__ecart_largeur_dans_pied
        tab_coord_petit_polinome= gestion_structuration_1.cree_tab_coord_rectangle_arrondie(x, y, x+ larg, y+ gestion_structuration_1.__hauteur_polygone_pied, gestion_structuration_1.__raduis_polynome_pied) 
        self.__petit_polynome= self.__feuille.create_polygon(tab_coord_petit_polinome, smooth=True, fill= "white", tags= [self.__nom_pied_page], width=1, outline= couleur_bordure)
        mot_en_bas= "la santé avant tout"
        self.__ecris_pied= self.__feuille.create_text(x +larg/2, y+ gestion_structuration_1.__hauteur_polygone_pied/2, fill= "black", text= mot_en_bas, font= police_petit_ecris, anchor= "c", tags=[self.__nom_pied_page])

    def accomodation(self, larg, haut):
        self.__accomode_entete(larg)
        self.__accomde_centre_et_pied(larg- 2*gestion_structuration_1.__espace_avec_bordure_fenetre, haut- gestion_structuration_1.__hauteur_entete- gestion_structuration_1.__espace_entre_block)

    def __accomde_centre_et_pied(self, larg, haut):
         haut -= gestion_structuration_1.__hauteur_pied + 2*gestion_structuration_1.__espace_entre_block
         hauteur_centre= float(self.__feuille.itemcget(self.__cadre_centrale, "height"))
         largeur_centre= float(self.__feuille.itemcget(self.__cadre_centrale, "width"))
         larg_minimlae_centre= gestion_structuration_1.__largeur_minimale_fenetre- 2*gestion_structuration_1.__espace_avec_bordure_fenetre
         if(larg<larg_minimlae_centre):
            larg= larg_minimlae_centre
         if(haut< gestion_structuration_1.__hauteur_minimale_centre):
            haut= gestion_structuration_1.__hauteur_minimale_centre
         if(larg!= largeur_centre or haut != hauteur_centre):
            self.__feuille.itemconfigure(self.__cadre_centrale, height= haut, width= larg)
            self.__conteneur_page.change_taille(larg, haut)
            self.__accomodation_pied(haut- hauteur_centre, larg)

    def __accomodation_pied(self, depl, larg):
          tab_coord_rect_pied= self.__feuille.coords(self.__rectangle_pied)
          tab_coord_rect_pied[2]= tab_coord_rect_pied[0]+ larg
          self.__feuille.coords(self.__rectangle_pied, tab_coord_rect_pied)
          x= tab_coord_rect_pied[0]+ gestion_structuration_1.__ecart_largeur_dans_pied
          y= tab_coord_rect_pied[1]- gestion_structuration_1.__hauteur_polygone_pied/2
          larg-= 2*gestion_structuration_1.__ecart_largeur_dans_pied
          tab_coord_petit_polinome= gestion_structuration_1.cree_tab_coord_rectangle_arrondie(x, y, x+ larg, y+ gestion_structuration_1.__hauteur_polygone_pied, gestion_structuration_1.__raduis_polynome_pied)
          tab_coord_ecris= [x+larg/2, y+ gestion_structuration_1.__hauteur_polygone_pied/2]
          self.__feuille.coords(self.__petit_polynome, tab_coord_petit_polinome)
          self.__feuille.coords( self.__ecris_pied, tab_coord_ecris)
          self.__feuille.move(self.__nom_pied_page, 0, depl)             

    def __accomode_entete(self, larg):
        tab_coord = self.__feuille.coords(self._rectangle_entete)
        if(gestion_structuration_1.__largeur_minimale_fenetre> larg ):
            larg= gestion_structuration_1.__largeur_minimale_fenetre
        if((tab_coord[2]- tab_coord[0]) != larg):
            tab_coord[2]= tab_coord[0]+ larg
            self.__feuille.coords(self._rectangle_entete, tab_coord)
            tab_coord_contenu= self.__feuille.bbox(self.__nom_elt_entete)
            self.__feuille.move(self.__nom_elt_entete, ((tab_coord[0]+ tab_coord[2])/2- (tab_coord_contenu[2]+ tab_coord_contenu[0])/2), 0)
            
    def get_conteneur_page(self):
        return self.__conteneur_page        

