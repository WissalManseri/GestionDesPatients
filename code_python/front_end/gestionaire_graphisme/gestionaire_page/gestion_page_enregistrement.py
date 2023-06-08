from tkinter import StringVar
from front_end.livre_page.page import Page, tk
from front_end.gestionaire_graphisme.gestionaire_page.fonction_creation_elt_dans_feuille import fonction_creation_elt_page


class gestion_enregistrement:
    __largeur_partie_droit= 400
    __id_generale_petit_ecris= "petit_ecris"

    def __fabrique_id_ecris(numero):
        return "petit_ecris"+str(numero)

    def __init__(self, la_page: Page, couleur, coleur_ligne, police_1, police_2, police_3, police_4, police_6, photo_deco) -> None:
        self.__la_page= la_page
        self.__espace_entete= 50
        self.__espace_entre_deux_cote= 30
        self.__largeur_min= 900
        self.__hauteur_min= 520
        self.__largeur_scroll= 6
        self.__initiliser_fonction_ecouteur_bouton()
        self.__initialisation_et_entete(police_1)
        self.__cree_elt_gauche(couleur, police_2, police_3, police_6, coleur_ligne)
        self.__cree_elt_droit(photo_deco, coleur_ligne, couleur, police_4)
        self.__la_page.set_fonction(self.__accomode) 

    def __initiliser_fonction_ecouteur_bouton(self):
        self.__conteneur_fonction= [None, None, None, None]
                      
    def __initialisation_et_entete(self, police_1):
        self.__feuille= self.__la_page.get_feuile()  
        self.__feuille.configure(scrollregion=(0,0, self.__largeur_min, self.__hauteur_min))
        y= 10
        x= 0
        self.__titre= self.__feuille.create_text(x, y, text="Enregistrer un nouveau patient dans la base", anchor= "nw", font= police_1)
        
    def __cree_elt_droit(self, photo_deco, couleur_ligne, couleur, police_4):
        self.__id_elt_droit= "elt_droit"
        x= 0
        y= self.__espace_entete
        id_photo= self.__feuille.create_image(x, y,  image= photo_deco, anchor= "nw", tags= [self.__id_elt_droit])
        tab_coord_photo= self.__feuille.bbox(id_photo)
        self.__feuille.create_text((tab_coord_photo[0]+ tab_coord_photo[2])/2, y+ 10, text="HOPITAL SANTE PLUS", anchor= "c", tags= [self.__id_elt_droit])
        y= tab_coord_photo[3]+30
        larg_bout= 80
        haut_bout= 30
        id_bout= "bout_en_an"
        bouton_valider= fonction_creation_elt_page.cree_bouton(self.__feuille, x, y, larg_bout, haut_bout, [self.__id_elt_droit], couleur_ligne, "Enregistrer", police_4)
        bouton_annuler= fonction_creation_elt_page.cree_bouton(self.__feuille,  tab_coord_photo[2]- larg_bout, y, larg_bout, haut_bout, [self.__id_elt_droit, id_bout], couleur_ligne, "Annuler", police_4)
        bouton_valider.configure(command= lambda: self.__ecoute_bouton(0))
        bouton_annuler.configure(command= lambda: self.__ecoute_bouton(1))
        y= self.__feuille.bbox(id_bout)[3]+50
        self.__cree_zone_autre_fonction(x, y, couleur_ligne, couleur, police_4)

    def __cree_zone_autre_fonction(self, x, y, couleur_ligne, couleur, police_4):
        larg_rect= 300
        haut_rect= 120
        self.__feuille.create_rectangle(x, y, x+ larg_rect, y+ haut_rect, fill="white", outline=couleur_ligne,  tags=[self.__id_elt_droit])
        larg_petit_rect= 120
        haut_petit_rect= 20
        x1= x+(larg_rect- larg_petit_rect)/2
        y-= haut_petit_rect/2
        rect_info= self.__feuille.create_rectangle(x1, y, x1+ larg_petit_rect, y+ haut_petit_rect, fill= couleur, outline=couleur_ligne,  tags=[self.__id_elt_droit])
        self.__feuille.create_text(x1+ larg_petit_rect/2, y+ haut_petit_rect/2, text="Autre action", anchor= "c", tags=[self.__id_elt_droit], font=police_4)
        y= self.__feuille.bbox(rect_info)[3]+ 10
        larg_bout= 280
        haut_bout= 30
        id_bout= "bout_font_sup"
        bout_import= fonction_creation_elt_page.cree_bouton(self.__feuille,  x+ (larg_rect - larg_bout)/2, y, larg_bout, haut_bout, [self.__id_elt_droit, id_bout], couleur_ligne, "Importer un patient de la base", police_4)
        y= self.__feuille.bbox(id_bout)[3]+10
        bout_supp= fonction_creation_elt_page.cree_bouton(self.__feuille,  x+ (larg_rect - larg_bout)/2, y, larg_bout, haut_bout, [self.__id_elt_droit, id_bout], couleur_ligne, "Supprimer un patient de la base", police_4)
        bout_import.configure(command= lambda: self.__ecoute_bouton(2))
        bout_supp.configure(command= lambda: self.__ecoute_bouton(3))

    def __cree_elt_gauche(self, couleur, police_2, police_3, police_6, coleur_ligne):
        y= self.__espace_entete
        x= 80
        self.__rect_gauche= self.__feuille.create_rectangle(x, y, x+1, y+1, fill= couleur, width=1, outline= coleur_ligne)
        y+= 30
        self.__id_elt_gauche= "elt_gauche"
        self.__feuille.create_text(x, y-20, text="INFORMATIONS DU PATIENT", tags= [self.__id_elt_gauche], font= police_2, anchor="nw")
        y += 15
        self.__cree_cadre_info_patient(x, y, coleur_ligne, police_3, police_6)

    def __ecoute_entry_pour_effacer_petit_message_erreur(self, e, id_petit_ecris):
          self.__page_info_patient.get_feuile().itemconfigure(id_petit_ecris, text= "") 
 
    def __cree_cadre_info_patient(self, x, y, couleur_ligne, police_3, police_6):
        #nous prenons la taille de la partie des patient static
        larg_rect_info= 400
        haut_rect_info= 600
        self.__page_info_patient= Page(self.__feuille, larg_rect_info, haut_rect_info, "white")
        self.__cadre_info_patient= self.__feuille.create_window(x, y, width= larg_rect_info, height= haut_rect_info, window= self.__page_info_patient.get_support(), tags= [self.__id_elt_gauche], anchor= "nw")
        feuille= self.__page_info_patient.get_feuile()
        #nous suppsosons que la largeur du cadre ne sera jamais modifiee
        self.__page_info_patient.change_larg_scroll_x(0)
        espace_1= 15
        espace_avec_petit_ecris= 5
        espace_2= 10+self.__largeur_scroll
        x= espace_2
        y= 10
        haut= 25
        i= 0
        tab_id_entry= ["Code", "Nom", "Prenom", "Date de naissance", "Téléphone", "Adresse", "Profession", "Date d'enregistrement"]
        self.__conteneur_variable_en= []
        indice_sindage_entry= self.__indice_sindage_entry= 3
        nb_entry= self.__nb_entry= len(tab_id_entry)
        for k in range(indice_sindage_entry) :
            id_elt= tab_id_entry[k]
            en= fonction_creation_elt_page.cree_entry_indication(feuille, x, y, id_elt, police_3, larg_rect_info- 2*espace_2, haut, "nw", [self.__id_elt_gauche, id_elt], couleur_ligne)
            y=feuille.bbox(id_elt)[3]-3+ espace_avec_petit_ecris
            id_petit_ecris= gestion_enregistrement.__fabrique_id_ecris(k)
            feuille.create_text(x, y, anchor= "nw", fill= "red", font= police_6, tags= [gestion_enregistrement.__id_generale_petit_ecris, id_petit_ecris])
            y=feuille.bbox(id_petit_ecris)[3] +espace_1
            var= tk.StringVar()
            en.configure(font= police_3, textvariable= var)
            en.bind("<KeyPress>", lambda e, id_avertisement= id_petit_ecris : self.__ecoute_entry_pour_effacer_petit_message_erreur(e, id_avertisement) )
            self.__conteneur_variable_en.append(var)
        indice_sex=feuille.create_text(x, y, text="Sexe", font= police_3, tags=[self.__id_elt_gauche], anchor= "nw") 
        self.__id_conteneur_info_choix_sexe= "choix_sexe"
        valeur_masculin= "M"
        valeur_feminin= "F"
        diametre_bouton_radio= 18
        y=feuille.bbox(indice_sex)[3]+ 5
        self.__tab_bout_radio_masculin, id_bout_mas= fonction_creation_elt_page.cree_bouton_radio_choix(feuille, x+20 , y, valeur_masculin, police_3, diametre_bouton_radio, "nw", [self.__id_elt_gauche], self.__id_conteneur_info_choix_sexe,  valeur_masculin, False)
        t_coord_rdio_m=feuille.bbox(id_bout_mas)
        x1= t_coord_rdio_m[2]+ 30
        self.__tab_bout_radio_feminin, id_bout_fem= fonction_creation_elt_page.cree_bouton_radio_choix(feuille, x1, y, valeur_feminin, police_3, diametre_bouton_radio, "nw", [self.__id_elt_gauche], self.__id_conteneur_info_choix_sexe,  valeur_feminin, False)
        y= t_coord_rdio_m[3]-3 + espace_1
        for k in range(indice_sindage_entry, nb_entry): 
            id_elt= tab_id_entry[k]
            i+=1
            en= fonction_creation_elt_page.cree_entry_indication(feuille, x, y, id_elt, police_3, larg_rect_info- 2*espace_2, haut, "nw", [self.__id_elt_gauche, id_elt], couleur_ligne)
            y=feuille.bbox(id_elt)[3]-3+ espace_avec_petit_ecris
            id_petit_ecris= gestion_enregistrement.__fabrique_id_ecris(k+1)#+ 1 pour gerer le faite que le sexe sera pris dans le tableau des donnees
            feuille.create_text(x, y, anchor= "nw", fill= "red", font= police_6, tags= [gestion_enregistrement.__id_generale_petit_ecris, id_petit_ecris])
            y=feuille.bbox(id_petit_ecris)[3] +espace_1            
            var= tk.StringVar()
            en.configure(font= police_3, textvariable= var)
            en.bind("<KeyPress>", lambda e, id_avertisement= id_petit_ecris : self.__ecoute_entry_pour_effacer_petit_message_erreur(e, id_avertisement) )
            self.__conteneur_variable_en.append(var)    
        feuille.configure(scrollregion=(0,0, 0, y+ espace_1)) 

    def __effacer_tous_petit_message_erreur(self):
        self.__page_info_patient.get_feuile().itemconfigure(gestion_enregistrement.__id_generale_petit_ecris, text= "")            
    
    def afficher_petit_message_erreur(self, tab):
        for indice in tab:
            self.__page_info_patient.get_feuile().itemconfigure(gestion_enregistrement.__fabrique_id_ecris(indice), text= "informations incorrectes")

    def get_tab_info_patient(self):
       tab_info= []
       var: StringVar
       for i in range(self.__indice_sindage_entry):
         var= self.__conteneur_variable_en[i]
         tab_info.append(var.get().strip().upper())
       #ajout de la valeur du sexe    
       tab_info.append(fonction_creation_elt_page.valeur_choisit_par_bouton_radio_choix(self.__id_conteneur_info_choix_sexe)) 
       for i in range(self.__indice_sindage_entry, self.__nb_entry):
         var= self.__conteneur_variable_en[i]
         tab_info.append(var.get().strip().upper())
       self.__effacer_tous_petit_message_erreur()   
       return tab_info  

    def set_tab_info_patient(self, tab_info):
       self.__effacer_tous_petit_message_erreur()   
       var: StringVar
       for i in range(self.__indice_sindage_entry):
         var= self.__conteneur_variable_en[i]
         var.set(tab_info[i]) 
       #changement de la valeur du sexe
       valeur_sexe= tab_info[self.__indice_sindage_entry]
       tab_elt_bout_sexe= self.__tab_bout_radio_feminin
       if(self.__tab_bout_radio_masculin[0]== valeur_sexe):
          tab_elt_bout_sexe= self.__tab_bout_radio_masculin
       fonction_creation_elt_page.radio_bouton_choix_change(tab_elt_bout_sexe[0], tab_elt_bout_sexe[1], tab_elt_bout_sexe[2], tab_elt_bout_sexe[3], tab_elt_bout_sexe[4])  
       for i in range(self.__indice_sindage_entry, self.__nb_entry):
         var= self.__conteneur_variable_en[i]
         var.set(tab_info[i+1]) 


    def __ecoute_bouton(self, indice):#noous supposons que l'id existers dans le dict des fonction
           fonction= self.__conteneur_fonction[indice]
           if(fonction != None):
              fonction()   
        
    def supprimer_valeur_dans_entry(self):
        self.__effacer_tous_petit_message_erreur()   
        var: StringVar
        for var in self.__conteneur_variable_en:
            var.set("")

   # nous supposons que tout est entrer correctement
    def set_fonction_bouton(self, indice, fonction):
        self.__conteneur_fonction[indice]= fonction
        

    def __actualise(self, larg, haut):
        if(larg< self.__largeur_min):
            larg= self.__largeur_min 
        if(haut< self.__hauteur_min):
            haut= self.__hauteur_min    
        tab_coord_titre= self.__feuille.bbox(self.__titre)
        self.__feuille.move(self.__titre, larg/2- (tab_coord_titre[0]+ tab_coord_titre[2])/2, 0)
        larg-= gestion_enregistrement.__largeur_partie_droit
        tab_coord= [elt for elt in self.__feuille.bbox(self.__rect_gauche)]
        tab_coord[2]= larg
        tab_coord[0]= 80
        tab_coord[1]= self.__espace_entete
        tab_coord[3]= haut- 30
        self.__feuille.coords(self.__rect_gauche, tab_coord)
        tab_coord_droit= self.__feuille.bbox(self.__id_elt_droit)
        tab_coord_gauche= self.__feuille.bbox(self.__id_elt_gauche)
        self.__feuille.move(self.__id_elt_droit, tab_coord[2]- tab_coord_droit[0]+ self.__espace_entre_deux_cote, 0)
        self.__feuille.move(self.__id_elt_gauche, (tab_coord[0]+ tab_coord[2])/2 - (tab_coord_gauche[0]+ tab_coord_gauche[2])/2, 0)
        tab_coord_cadre_inf_patient= [elt for elt in self.__feuille.bbox(self.__cadre_info_patient)]
        tab_coord_cadre_inf_patient[3]= haut- 50
        self.__feuille.itemconfigure(self.__cadre_info_patient, height= (tab_coord_cadre_inf_patient[3]- tab_coord_cadre_inf_patient[1])-6)

    def __accomode(self):
        larg= float(self.__feuille.cget("width"))
        haut= float(self.__feuille.cget("height"))
        if(larg< self.__largeur_min):
            self.__la_page.change_larg_scroll_x(self.__largeur_scroll)
        else:
            self.__la_page.change_larg_scroll_x(0)
        if(haut< self.__hauteur_min):
            self.__la_page.change_larg_scroll_y(self.__largeur_scroll)
        else:
            self.__la_page.change_larg_scroll_y(0)
        self.__actualise(larg, haut)    

