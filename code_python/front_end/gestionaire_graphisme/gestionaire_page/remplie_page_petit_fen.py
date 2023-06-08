from  front_end.livre_page.page import Page, tk
from front_end.gestionaire_graphisme.gestionaire_page.fonction_creation_elt_dans_feuille import fonction_creation_elt_page

class remplie_page_petit_fen:
    __id_petite_ecris_erreur= "ecris_erreur"

    def __fabrique_id(indice):
        return "id"+str(indice)

    def __ecoute_et_efface_petit_ecris_erreur(e, indice, feuille: tk.Canvas):
      feuille.itemconfigure(remplie_page_petit_fen.__fabrique_id(indice), text= "")

    def effacer_tout_erreur(feuille: tk.Canvas):
       feuille.itemconfigure(remplie_page_petit_fen.__id_petite_ecris_erreur, text="")  
       
    def signaler_erreur_avec_petit_ecris(tab_indice, feuille: tk.Canvas):
      for indice in tab_indice:
            feuille.itemconfigure(remplie_page_petit_fen.__fabrique_id(indice), text= "informations incorrectes")

    def fabrique_liste_entry(page_entry: Page, tab_indication, police_1, couleur_ligne):
            page_entry.change_larg_scroll_x(0)
            feuille= page_entry.get_feuile()
            larg, haut= int(feuille.cget("width")), int(feuille.cget("height"))
            x= 10
            y=10
            espace= 10
            larg_en= larg- 2*espace
            haut_en= 30
            conserveur_en= []
            for elt in tab_indication:
                en= fonction_creation_elt_page.cree_entry_indication(feuille, x, y, elt, police_1, larg_en, haut_en, "nw", [elt], couleur_ligne)
                en.configure(font= police_1)
                conserveur_en.append(en)
                y= feuille.bbox(elt)[3]+ espace 
            page_entry.get_feuile().configure(scrollregion=(0, 0, larg, y))
            if(haut< y):
                  page_entry.change_larg_scroll_y(6)
            else: 
                  page_entry.change_larg_scroll_y(0)
            page_entry.change_larg_scroll_x(0)  
            return conserveur_en               

    def fabrique_ecris_info(page_info : Page, texte, police_1):
         feuille_info= page_info.get_feuile()
         feuille_info.create_text(10, 10, text= texte, font= police_1, anchor= "nw")
         tab_coord_globale= feuille_info.bbox(tk.ALL)
         feuille_info.configure(scrollregion= (0, 0, tab_coord_globale[2]+2, tab_coord_globale[3]+2))

    def fabrique_page_recup_donnee_examination(page_info : Page,  police_1, police_interne,police_6, couleur_ligne): 
        page_info.change_larg_scroll_x(0)  
        feuille_info= page_info.get_feuile() 
        bordure= 20
        ecart_y= 10
        ecart_avec_ecris= 5
        larg, haut= int(feuille_info.cget("width")), int(feuille_info.cget("height"))
        larg -= 2*bordure
        x= bordure
        y= bordure
        haut_en= 30
         #-------------------------------------------------------------------------
        id_heure_date= "id_heure"
        espace_entre_entry_heure_date= 9
        x_heure_date= x
        larg_heur_date= (larg- 2*espace_entre_entry_heure_date)//3
        entry_date= fonction_creation_elt_page.cree_entry_indication(feuille_info, x_heure_date, y, "Date", police_1, larg_heur_date, haut_en, "nw", [id_heure_date], couleur_ligne)
        y_ecris= feuille_info.bbox(id_heure_date)[3]+ ecart_avec_ecris
        feuille_info.create_text(x_heure_date, y_ecris, anchor= "nw", font= police_6, fill= "red",  tags= [remplie_page_petit_fen.__id_petite_ecris_erreur, remplie_page_petit_fen.__fabrique_id(0)])
        entry_date.configure(font= police_interne)
        entry_date.bind("<KeyPress>", lambda e, indice= 0 : remplie_page_petit_fen.__ecoute_et_efface_petit_ecris_erreur(e, indice, feuille_info))
        x_heure_date= feuille_info.bbox(id_heure_date)[2]+ espace_entre_entry_heure_date
        entry_heure_debut= fonction_creation_elt_page.cree_entry_indication(feuille_info, x_heure_date, y, "Heure début", police_1, larg_heur_date, haut_en, "nw", [id_heure_date], couleur_ligne)
        feuille_info.create_text(x_heure_date, y_ecris, anchor= "nw", font= police_6, fill= "red",  tags= [remplie_page_petit_fen.__id_petite_ecris_erreur, remplie_page_petit_fen.__fabrique_id(1)])
        entry_heure_debut.configure(font= police_interne)
        entry_heure_debut.bind("<KeyPress>", lambda e, indice= 1 : remplie_page_petit_fen.__ecoute_et_efface_petit_ecris_erreur(e, indice, feuille_info))
        x_heure_date= feuille_info.bbox(id_heure_date)[2] + espace_entre_entry_heure_date 
        entry_heure_fin= fonction_creation_elt_page.cree_entry_indication(feuille_info, x_heure_date, y, "Heure fin", police_1, larg_heur_date, haut_en, "nw", [id_heure_date], couleur_ligne)
        entry_heure_fin.configure(font= police_interne)
        entry_heure_fin.bind("<KeyPress>", lambda e, indice= 2 : remplie_page_petit_fen.__ecoute_et_efface_petit_ecris_erreur(e, indice, feuille_info))
        feuille_info.create_text(x_heure_date, y_ecris, anchor= "nw", font= police_6, fill= "red",  tags= [remplie_page_petit_fen.__id_petite_ecris_erreur, remplie_page_petit_fen.__fabrique_id(2)])
        y = feuille_info.bbox(remplie_page_petit_fen.__id_petite_ecris_erreur)[3]+ ecart_y
        #-------------------------------------------------------------------------
        id_type= "id_en_type"
        entry_type= fonction_creation_elt_page.cree_entry_indication(feuille_info, x, y, "Type examen", police_1, larg, haut_en, "nw", [id_type], couleur_ligne)
        y_ecris= feuille_info.bbox(id_type)[3]+ ecart_avec_ecris
        id_ecris_type= remplie_page_petit_fen.__fabrique_id(3)
        feuille_info.create_text(x, y_ecris, anchor= "nw", font= police_6, fill= "red", tags= [remplie_page_petit_fen.__id_petite_ecris_erreur, id_ecris_type])
        entry_type.configure(font= police_interne)
        entry_type.bind("<KeyPress>", lambda e, indice= 3 : remplie_page_petit_fen.__ecoute_et_efface_petit_ecris_erreur(e, indice, feuille_info))
        y = feuille_info.bbox(id_ecris_type)[3]+ ecart_y
        #--------------------------------------------------------------------------
        id_remarque= "id_remarque" 
        haut_zone_texte= 80
        zone_rem= fonction_creation_elt_page.cree_zone_texte_indication(feuille_info, x, y, "Remarque", haut_zone_texte, larg, haut_zone_texte, "nw", [id_remarque], couleur_ligne)
        zone_rem.configure(font= police_interne)
        y= feuille_info.bbox(id_remarque)[3]+ ecart_y
        #--------------------------------------------------------------------------
        id_result= "id_result" 
        haut_zone_texte= 80
        zone_result= fonction_creation_elt_page.cree_zone_texte_indication(feuille_info, x, y, "Réultat examination", haut_zone_texte, larg, haut_zone_texte, "nw", [id_result], couleur_ligne)
        zone_result.configure(font= police_interne)
        y= feuille_info.bbox(id_result)[3]+ ecart_y
        #--------------------------------------------------------------------------
        id_pres= "id_pres" 
        haut_zone_texte= 80
        zone_pres= fonction_creation_elt_page.cree_zone_texte_indication(feuille_info, x, y, "Prescription après examination", haut_zone_texte, larg, haut_zone_texte, "nw", [id_pres], couleur_ligne)
        zone_pres.configure(font= police_interne)
        #-----------@--------------------------@-------------------------------@
        tab_coord_globale= feuille_info.bbox(tk.ALL)
        feuille_info.configure(scrollregion= (0, 0, tab_coord_globale[2], tab_coord_globale[3]+10))
        if(tab_coord_globale[3]< haut):
              page_info.change_larg_scroll_y(0)
        return [entry_date, entry_heure_debut, entry_heure_fin,  entry_type], [zone_rem, zone_result, zone_pres]
        
    def fabrique_page_recup_donnee_rendevous(page_info : Page,  police_1, police_interne, police_6, couleur_ligne): 
        page_info.change_larg_scroll_x(0)  
        feuille_info= page_info.get_feuile() 
        bordure= 20
        ecart_y= 10
        ecart_avec_ecris= 5
        larg, haut= int(feuille_info.cget("width")), int(feuille_info.cget("height"))
        larg -= 2*bordure
        x= bordure
        y= bordure
        haut_en= 30
        t_depart= ""
        #--------------------------------------------------------------------
        id_heure_date= "id_heure"
        espace_entre_entry_heure_date= 10
        x_heure_date= x
        larg_heur_date= (larg- espace_entre_entry_heure_date)//2
        entry_date= fonction_creation_elt_page.cree_entry_indication(feuille_info, x_heure_date, y, "Date", police_1, larg_heur_date, haut_en, "nw", [id_heure_date], couleur_ligne)
        y_ecris= feuille_info.bbox(id_heure_date)[3]+ ecart_avec_ecris
        feuille_info.create_text(x_heure_date, y_ecris, anchor= "nw", font= police_6, fill= "red", text=t_depart, tags= [remplie_page_petit_fen.__id_petite_ecris_erreur, remplie_page_petit_fen.__fabrique_id(0)])
        entry_date.bind("<KeyPress>", lambda e, indice= 0 : remplie_page_petit_fen.__ecoute_et_efface_petit_ecris_erreur(e, indice, feuille_info))
        entry_date.configure(font= police_interne)
        x_heure_date= feuille_info.bbox(id_heure_date)[2]+ espace_entre_entry_heure_date
        entry_heure= fonction_creation_elt_page.cree_entry_indication(feuille_info, x_heure_date, y, "Heure", police_1, larg_heur_date, haut_en, "nw", [id_heure_date], couleur_ligne)
        feuille_info.create_text(x_heure_date, y_ecris, anchor= "nw", font= police_6, fill= "red", text=t_depart, tags= [remplie_page_petit_fen.__id_petite_ecris_erreur, remplie_page_petit_fen.__fabrique_id(1)])
        entry_heure.bind("<KeyPress>", lambda e, indice= 1 : remplie_page_petit_fen.__ecoute_et_efface_petit_ecris_erreur(e, indice, feuille_info))
        entry_heure.configure(font= police_interne)
        y= feuille_info.bbox(remplie_page_petit_fen.__id_petite_ecris_erreur)[3]+ ecart_y
        #-------------------------------------------------------------------------
        id_raison= "raise"
        entry_raison= fonction_creation_elt_page.cree_entry_indication(feuille_info, x, y, "Raison du rendez-vous", police_1, larg, haut_en, "nw", [id_raison], couleur_ligne)
        y_ecris= feuille_info.bbox(id_raison)[3]+ ecart_avec_ecris
        feuille_info.create_text(x, y_ecris, anchor= "nw", font= police_6, fill= "red", text=t_depart, tags= [remplie_page_petit_fen.__id_petite_ecris_erreur, remplie_page_petit_fen.__fabrique_id(2)])
        entry_raison.bind("<KeyPress>", lambda e, indice= 2 : remplie_page_petit_fen.__ecoute_et_efface_petit_ecris_erreur(e, indice, feuille_info))
        entry_raison.configure(font= police_interne)
        #-----------@--------------------------@-------------------------------@
        tab_coord_globale= feuille_info.bbox(tk.ALL)
        feuille_info.configure(scrollregion= (0, 0, tab_coord_globale[2], tab_coord_globale[3]+10))
        if(tab_coord_globale[3]< haut):
              page_info.change_larg_scroll_y(0) 
        return [entry_date, entry_heure, entry_raison]
        
        