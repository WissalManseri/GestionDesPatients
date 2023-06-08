from  front_end.gestionaire_graphisme.gestionaire_page.fonction_creation_elt_dans_feuille import fonction_creation_elt_page,  Font, Canvas
from front_end.livre_page.page import Page

class gestion_page_tableau:
    police_ecris_dans_tableau: Font
    couleur_ligne_selecte= ""
    def __fabrique_id_rect_info(indice):
        return "rect_ligne_ecoute"+str(indice)

    def plus_long_mot(tab_mot):
        if(len(tab_mot)==0):
            return None 
        mot_long= tab_mot[0]
        nb= len(mot_long)
        for mot in tab_mot:
            lrg= len(mot)
            if(lrg> nb):
                mot_long= mot 
                nb= lrg 
        return mot_long 

    __ecart_min_bordure= 10      

    def __init__(self,feuille: Canvas, x, y, tab_nom_case, police_ecrit_entete: Font, couleur_entete, couleur_ligne) -> None:
        self.__tab_nom_case= tab_nom_case
        self.__police_erit_entete= police_ecrit_entete
        self.__nom_rect_info= "rect_info"
        self.__nom_rect_info_interne= "inf_interne"
        self.__indice_ligne_select= None
        self.__lageur_scroll= 6
        self.__tab_info_interne= []
        self.__espace_entre_eris= 10
        self.___initialise(feuille, x, y)
        self.__couleur_entete= couleur_entete
        self.__couleur_ligne= couleur_ligne
        y= self.__creation_entete(self.__largeur_min)
        self.__creation_pati_info(0, y, 20)
        self.__creation_interne(self.__largeur_min)
        self.__la_page_centrale.set_fonction(self.__accomode_page_info)

    def get_ligne_select(self):
        if(self.__indice_ligne_select != None):
            return self.__tab_info_interne[self.__indice_ligne_select] 
        return None    

    def __ecoute_echange_indice_select(self, e, indice):
         feuille= self.__page_info.get_feuile()
         if(self.__indice_ligne_select != None):
            id_ancien= gestion_page_tableau.__fabrique_id_rect_info(self.__indice_ligne_select)
            feuille.itemconfigure(id_ancien, fill= "white")
         if(indice != self.__indice_ligne_select):   
            self.__indice_ligne_select= indice
            id_nouv= gestion_page_tableau.__fabrique_id_rect_info(indice)
            feuille.itemconfigure(id_nouv, fill= gestion_page_tableau.couleur_ligne_selecte)
         else: 
            self.__indice_ligne_select= None   
                
    def ___initialise(self, feuille: Canvas, x, y) :
        nom_plus_long= gestion_page_tableau.plus_long_mot(self.__tab_nom_case)
        larg_case_min= self.__police_erit_entete.measure(nom_plus_long)+ 2*gestion_page_tableau.__ecart_min_bordure 
        self.__largeur_min= len(self.__tab_nom_case)* larg_case_min
        self.__espace_y= 10
        self.__haut_entete= self.__police_erit_entete.metrics("linespace")+ 2*self.__espace_y
        self.__haut_min= self.__haut_entete+ 100
        larg_page_centrale= self.__largeur_min
        haut_page_centrale= 200
        self.__la_page_centrale= Page(feuille, larg_page_centrale, haut_page_centrale, "white")
        self.__feuille_parent= feuille
        self.__id_cadre=  feuille.create_window(x, y, width= larg_page_centrale, height= haut_page_centrale, window= self.__la_page_centrale.get_support(), anchor="nw") 
        self.__la_page_centrale.change_larg_scroll_y(0)
        self.__la_page_centrale.change_larg_scroll_x(self.__lageur_scroll) 
        self.__feuille= self.__la_page_centrale.get_feuile()
        self.__feuille.configure(scrollregion=(0,0, self.__largeur_min, self.__haut_min))

    def __creation_entete(self, larg):
        epaiseur_trait= 1
        haut= self.__haut_entete
        x= epaiseur_trait
        y= epaiseur_trait
        nb_elt= len(self.__tab_nom_case)
        larg /= nb_elt
        for mot in self.__tab_nom_case  :
            id_elt= self.__feuille.create_rectangle(x, y, x+larg, y+ haut, width=epaiseur_trait, fill= self.__couleur_entete, tags= [self.__nom_rect_info], outline= self.__couleur_ligne) 
            self.__feuille.create_text(x+larg/2, y+haut/2, anchor="c", text= mot, tags= [self.__nom_rect_info], font= self.__police_erit_entete)
            x= self.__feuille.bbox(id_elt)[2]-epaiseur_trait
        y+= haut + epaiseur_trait 
        return y- epaiseur_trait  

    def __desine_ligne(self, y, larg, tab, epaiseur_trait, feuille: Canvas, espace_bord_y, espace_bord_x, id_rect, id_grp):
         x= espace_bord_x
         b= y+ espace_bord_y
         for ecris in tab :
               feuille.create_text(x, b, anchor="nw", text= ecris, tags= [self.__nom_rect_info_interne, id_grp], font= gestion_page_tableau.police_ecris_dans_tableau)
               x+= larg
         y_bas= feuille.bbox(id_grp)[3] + espace_bord_y   
         x= 0 
         for elt in tab:
            id_courant= feuille.create_rectangle(x, y, x+ larg, y_bas, tags= [self.__nom_rect_info_interne, id_rect, id_grp], width=epaiseur_trait, fill= "white", outline= self.__couleur_ligne)
            feuille.tag_lower(id_courant)#nous mettons les rectangle en dessous
            x = feuille.bbox(id_courant)[2]- epaiseur_trait
         return feuille.bbox(id_grp)[3]    
             
    def __creation_interne(self, larg):
        self.__indice_ligne_select= None
        feuille= self.__page_info.get_feuile()
        epaiseur_trait= 1
        y= 0
        nb= len(self.__tab_nom_case)
        larg /= nb
        i= 0
        espace_bord_y= 2
        espace_bord_x= 6
        for elt in self.__tab_info_interne:
            id_rect= gestion_page_tableau.__fabrique_id_rect_info(i)
            id_grp= "grp"+id_rect#ceci pour permetre une grande ecoute et une coloration specifique
            tab_elt_sinder= [fonction_creation_elt_page.sinde_ecris_en_ligne(ecris, gestion_page_tableau.police_ecris_dans_tableau, larg- 2*espace_bord_x) for ecris in elt]
            y= self.__desine_ligne(y, larg, tab_elt_sinder, epaiseur_trait, feuille, espace_bord_y, espace_bord_x, id_rect, id_grp)- epaiseur_trait
            feuille.tag_bind(id_grp, "<Button>", lambda e, indice= i: self.__ecoute_echange_indice_select(e, indice))
            i += 1
        feuille.configure(scrollregion=(0, 0, 0, y+2))  

    def __actualiser_tableau(self):
        larg= float(self.__page_info.get_feuile().cget("width"))
        self.__page_info.get_feuile().delete(self.__nom_rect_info_interne)
        self.__creation_interne(larg)
            
    def set_tab_info(self, tab):
        self.__tab_info_interne= tab  
        self.__actualiser_tableau()

    def ajout_ligne(self, elt):
        self.__tab_info_interne.append(elt)  
        self.__actualiser_tableau()

    def enlever_ligne(self):
        if(self.__indice_ligne_select  != None):
            del self.__tab_info_interne[self.__indice_ligne_select] 
            self.__indice_ligne_select= None
            self.__actualiser_tableau()   

    def __creation_pati_info(self, x, y, haut):
        larg= self.__largeur_min
        self.__page_info= Page(self.__feuille, larg, haut, "white") 
        self.__page_info.change_larg_scroll_y(self.__lageur_scroll)
        self.__page_info.change_larg_scroll_x(0)  
        self.__page_info.get_support().configure(background= self.__couleur_ligne, bd=1)
        self.__cadre_partie_info= self.__feuille.create_window(x, y, width= larg, height= haut, window=self.__page_info.get_support(), anchor="nw")     

    def __actualiser(self, larg, haut):
           if(larg< self.__largeur_min):
              larg= self.__largeur_min
              self.__la_page_centrale.change_larg_scroll_x(self.__lageur_scroll)
           else:
             self.__la_page_centrale.change_larg_scroll_x(0)    
           if(haut< self.__haut_min):
            haut= self.__haut_min   
           self.__feuille.delete(self.__nom_rect_info)
           self.__creation_entete(larg- self.__lageur_scroll)
           self.__page_info.get_feuile().delete(self.__nom_rect_info_interne)
           self.__creation_interne(larg- self.__lageur_scroll)       
           
    def __actualiser_partie_info(self, larg, haut):
        haut -= self.__haut_entete
        self.__feuille.itemconfigure(self.__cadre_partie_info, width= larg, height= haut)
        self.__page_info.change_taille(larg- self.__lageur_scroll, haut)   
         
    def __accomode_page_info(self):
        larg= float(self.__feuille.cget("width"))
        if(larg< self.__largeur_min):
            larg= self.__largeur_min
        haut= float(self.__feuille.cget("height"))  
        self.__actualiser_partie_info(larg- self.__lageur_scroll, haut)            
   
    def changer_taille(self, larg, haut):
        self.__feuille_parent.itemconfigure(self.__id_cadre, width= larg, height= haut)
        self.__actualiser(larg, haut)       
        self.__la_page_centrale.change_taille(larg + self.__lageur_scroll,  haut)     
        
