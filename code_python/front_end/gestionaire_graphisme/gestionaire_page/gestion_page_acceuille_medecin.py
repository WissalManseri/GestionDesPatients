from front_end.livre_page.page import Page
from  front_end.gestionaire_graphisme.gestionaire_page.fonction_creation_elt_dans_feuille import fonction_creation_elt_page, Font

class gestion_page_acceuille_medecin:
    def __init__(self, la_page: Page, photo, couleur, couleur_ligne, police_1, police_2) :
        self.__la_page= la_page 
        self.__larg_scroll= 6
        self.__initialisation(photo, couleur, couleur_ligne, police_1, police_2)
        self.__la_page.set_fonction(self.__accomode)

    def __initialisation(self, photo, couleur, couleur_ligne, police_1: Font, police_2: Font):
        self.__feuille= self.__la_page.get_feuile()
        larg= 850
        bordure_x= 50
        bordure_x_1= 40
        self.__largeur_minimale= larg + 2* bordure_x
        haut= 420
        self.__hauteur_minimale= haut +20
        #----------------------------------------------------------------------
        self.__feuille.configure(scrollregion=(0, 0, self.__largeur_minimale, self.__hauteur_minimale))
        self.__nom_genrale_cadre= "le_cadre_centre"
        texte_entete= "Prenons le controle de nos patients en un seul clic !"
        haut_ecris= police_1.metrics("linespace")
        ecart_haut= 20
        id_entete= self.__feuille.create_text(bordure_x+ (larg- bordure_x)/2, haut_ecris/2+ ecart_haut, text= texte_entete, font= police_1, tags= [self.__nom_genrale_cadre], anchor="c")    
        y= self.__feuille.bbox(id_entete)[3]+20
        self.__feuille.create_rectangle(bordure_x, y, larg, haut, fill=couleur, tags= [self.__nom_genrale_cadre], width= 0)
        x_photo= larg-350
        y_photo= haut- 300
        id_photo= self.__feuille.create_image(x_photo, y_photo,  image= photo, anchor= "nw", tags= [self.__nom_genrale_cadre]) 
        #----------------------------------------------------------------------
        slogan= "HOPITAL SANTE PLUS"
        haut_slogan= police_2.metrics("linespace")
        id_entete= self.__feuille.create_text(x_photo+ 350/2, y_photo+ haut_slogan/2+10, text= slogan, tags= [self.__nom_genrale_cadre], anchor="c", font=police_2)    
        tab_coord_photo = self.__feuille.bbox(id_photo)
        x= bordure_x+ bordure_x_1
        self.__feuille.create_rectangle(x, tab_coord_photo[1], tab_coord_photo[0]+3, haut, fill="white", tags= [self.__nom_genrale_cadre], width= 0) 
        epaiseur_trait= 1
        larg_utile= 400
        #---------------------------------------------------------------------
        x_bouton= x+ 20
        y= tab_coord_photo[1]+10
        larg_rect_sensible= larg_utile- 100
        haut_rect_sensible=30
        espace_entre_bouton= 20
        tab_nom_bouton= ["OPERATION SUR PATIENT", "AGENDA DU MEDECIN", "STATISTIQUE"]
        self.__tab_fonction_ecoute_bouton= [None, None, None]
        i= 0
        for elt in tab_nom_bouton:
            bout = fonction_creation_elt_page.cree_bouton_rectangle(self.__feuille, x_bouton, y, elt, larg_rect_sensible, haut_rect_sensible, [self.__nom_genrale_cadre, elt], police_2, "w")
            y= self.__feuille.bbox(elt)[3]+ espace_entre_bouton
            bout.configure(command= lambda indice= i: self.__ecoute_bouton(indice))
            i += 1
        #-----------------------------------------------------------------------
        x_trait_verticale= x_bouton+ larg_rect_sensible+ 20
        y_trait= tab_coord_photo[3]- epaiseur_trait
        self.__feuille.create_line([x, y_trait, x_trait_verticale, y_trait], tags= [self.__nom_genrale_cadre], fill= couleur_ligne)
        self.__feuille.create_line([x_trait_verticale, tab_coord_photo[1], x_trait_verticale, haut], tags= [self.__nom_genrale_cadre], fill= couleur_ligne)
        
    def __ecoute_bouton(self, indice):
        fonction = self.__tab_fonction_ecoute_bouton[indice]
        if(fonction != None):
            fonction()  

    def set_fonction_ecoute(self, indice, fonction):
        self.__tab_fonction_ecoute_bouton[indice]= fonction        
       
    def __centralise(self, larg):
       tab_coord= self.__feuille.bbox(self.__nom_genrale_cadre)
       self.__feuille.move(self.__nom_genrale_cadre, larg/2- (tab_coord[0]+ tab_coord[2])/2, 0)      
    
    def __accomode(self):
        larg= float(self.__feuille.cget("width"))
        haut= float(self.__feuille.cget("height"))
        if(self.__hauteur_minimale> haut):
            haut= self.__hauteur_minimale
            self.__la_page.change_larg_scroll_y(self.__larg_scroll)
        else:
           self.__la_page.change_larg_scroll_y(0)
        if(self.__largeur_minimale> larg):
            larg= self.__largeur_minimale
            self.__la_page.change_larg_scroll_x(self.__larg_scroll)
        else:
           self.__la_page.change_larg_scroll_x(0)
        self.__centralise(larg)      


