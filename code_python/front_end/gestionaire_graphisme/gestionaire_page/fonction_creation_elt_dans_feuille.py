from tkinter import Canvas, Entry, Button, Text
from tkinter.font import Font
from front_end.livre_page.fentre_livre import fenetre_livre
from front_end.gestionaire_graphisme.gestion_premiere_structuration import gestion_structuration_1

class fonction_creation_elt_page:
    __coloration_cercle_interne= "black"
    __espace_entre_indication_et_elt= 10
    __pourcentage_petit_cercle_interne_radio= 50
    __conteneur_valeur_groupe_bouton_radio= {}
    __conteneur_valeur_case_cochage= {}
    __nombre_de_case_cochable= 0
    __couleur_sensiblitee= "#74D1B3"

    def valeur_choisit_par_bouton_radio_choix(id_bouton):
        if(id_bouton in fonction_creation_elt_page.__conteneur_valeur_groupe_bouton_radio):
            return fonction_creation_elt_page.__conteneur_valeur_groupe_bouton_radio[id_bouton]
        return None   

    def valeur_case_cochage(id_case):
         if(id_case in fonction_creation_elt_page.__conteneur_valeur_case_cochage):
            return fonction_creation_elt_page.__conteneur_valeur_case_cochage[id_case]
         return None        

    def __cree_windo(x, y, elt, larg, haut, feuille: Canvas, tab_tags, anchor):
        feuille.create_window(x, y, width= larg, height= haut, window= elt, tags= tab_tags, anchor= anchor)

    def __activer_bouton_radio(id_cercle_bouton, feuille: Canvas, tab_tags):
        tab_coord= feuille.bbox(id_cercle_bouton)
        diametre_cercle= ((tab_coord[2]- tab_coord[0])*fonction_creation_elt_page.__pourcentage_petit_cercle_interne_radio)/100
        x, y= fenetre_livre.coord_debut_a_partie_du_centre((tab_coord[0]+ tab_coord[2])/2, (tab_coord[1]+ tab_coord[3])/2, diametre_cercle, diametre_cercle)
        feuille.create_oval(x, y, x+ diametre_cercle, y+ diametre_cercle, fill= fonction_creation_elt_page.__coloration_cercle_interne, tags= tab_tags)

#faut s'arranger a ne pas donner des memes id pour les boutons qui ne pas de meme groupe si non nous aurons des incoherence aussi eviter au max de mettre la meme valeur pour 2 boutons du meme groupe
    def cree_bouton_radio_choix(feuille: Canvas, x, y, nom_indication, police_ecriture: Font, diametre_cercle, anchor, tab_tags, id_bouton, valeur, verticale= True):#id_bouton nous servira a prendre les valeur du bouton selectioner ainsi qu'a indexe par tags le cercle de distinction sur les bouton de meme groupe donc de meme id 
        id_indication= feuille.create_text(x, y, text=nom_indication, font= police_ecriture, anchor= anchor, tags= tab_tags)
        tab_coord= feuille.bbox(id_indication)
        if(verticale):
            y= tab_coord[3]
            x, y= fenetre_livre.coord_debut_a_partie_du_centre(tab_coord[0]+3+police_ecriture.measure(nom_indication)/2, y+ diametre_cercle, diametre_cercle, diametre_cercle)
        else:
            x= tab_coord[2] -3
            x, y= fenetre_livre.coord_debut_a_partie_du_centre(x+ diametre_cercle, tab_coord[1]+ police_ecriture.metrics("linespace")/2, diametre_cercle, diametre_cercle)
        id_cercle= feuille.create_oval(x, y, x+ diametre_cercle, y+ diametre_cercle, fill= "white", tags= tab_tags)
        id_groupe= "id_grp_radio"+str(id_cercle)
        feuille.addtag_withtag(id_groupe, id_cercle)
        feuille.addtag_withtag(id_groupe, id_indication)
        feuille.itemconfigure(id_groupe, activefill= fonction_creation_elt_page.__couleur_sensiblitee)
        tab_cercle_interne= tab_tags+ [id_groupe, id_bouton]
        if(not id_bouton in fonction_creation_elt_page.__conteneur_valeur_groupe_bouton_radio):
            fonction_creation_elt_page.__activer_bouton_radio(id_cercle, feuille, tab_cercle_interne)
            fonction_creation_elt_page.__conteneur_valeur_groupe_bouton_radio[id_bouton]= valeur
        feuille.tag_bind(id_groupe, "<Button>", lambda e: fonction_creation_elt_page.__ecoute_bouton_radio_choix(e, valeur, id_cercle, feuille, tab_cercle_interne, id_bouton))
        return [valeur, id_cercle, feuille, tab_cercle_interne, id_bouton], id_groupe

#focntion tres delicate car faut absolument que les elts entrees soit en armonie avec celle de la creation des bouton et 
    def radio_bouton_choix_change(valeur, id_cercle_bouton, feuille: Canvas, tab_cercle_interne, id_bouton):
        if(fonction_creation_elt_page.__conteneur_valeur_groupe_bouton_radio[id_bouton]!= valeur):
            feuille.delete(id_bouton)#nous effassons l'ancien petit cercle
            fonction_creation_elt_page.__conteneur_valeur_groupe_bouton_radio[id_bouton]= valeur
            fonction_creation_elt_page.__activer_bouton_radio(id_cercle_bouton, feuille, tab_cercle_interne)

#la fonction qui s'execute lorsqu'on clique sur le bouton ou l'ensemble indexant le bouton au choix
    def __ecoute_bouton_radio_choix(e, valeur, id_cercle_bouton, feuille: Canvas, tab_cercle_interne, id_bouton):
        fonction_creation_elt_page.radio_bouton_choix_change(valeur, id_cercle_bouton, feuille, tab_cercle_interne, id_bouton)
        
    def cree_entry_indication(feuille: Canvas, x, y, nom_indication, police_ecriture: Font, larg, haut, anchor, tab_tags, couleur_ligne, verticale= True):    
        id_indication= feuille.create_text(x, y, text=nom_indication, font= police_ecriture, anchor= anchor, tags= tab_tags)
        tab_coord= feuille.bbox(id_indication)
        en=  Entry(feuille, width= larg, highlightbackground= couleur_ligne)
        if(verticale):
            y= tab_coord[3]+ fonction_creation_elt_page.__espace_entre_indication_et_elt/2
            x= tab_coord[0] +3
            fonction_creation_elt_page.__cree_windo(x, y, en, larg, haut, feuille, tab_tags, "nw")
        else:
           x= tab_coord[2] + 2*fonction_creation_elt_page.__espace_entre_indication_et_elt + larg/2
           y= (tab_coord[1]+ tab_coord[3])/2 
           fonction_creation_elt_page.__cree_windo(x, y, en, larg, haut, feuille, tab_tags, "c")
        return en

    def __ecoute_sortie_entre_dans_bouton(e, bout: Button, couleur, feuille: Canvas, id_contour):
         bout.configure(highlightbackground= couleur, background= couleur)
         feuille.itemconfigure(id_contour, fill= couleur)         

    def cree_bouton(feuille: Canvas, x, y, larg, haut, tab_tags, couleur_ligne, nom_indication, police: Font, couleur_activation= "#74D1B3"):
       radius= 20
       tab_coord= gestion_structuration_1.cree_tab_coord_rectangle_arrondie(x, y, x+larg, y+haut, radius)
       id_contour= feuille.create_polygon(tab_coord, smooth= True, tags= tab_tags, fill="white", width= 1, outline=couleur_ligne )
       larg-= 8
       haut-= 4
       bout= Button(feuille, width= larg, height= haut, background= "white", highlightbackground= "white", bd=0, highlightcolor= "white", text=nom_indication, font= police, activebackground= couleur_activation, anchor="c")
       fonction_creation_elt_page.__cree_windo(x+ 4, y+ 2, bout, larg, haut, feuille, tab_tags, "nw")
       bout.bind("<Enter>", lambda e: fonction_creation_elt_page.__ecoute_sortie_entre_dans_bouton(e, bout, couleur_activation, feuille, id_contour))
       bout.bind("<Leave>", lambda e: fonction_creation_elt_page.__ecoute_sortie_entre_dans_bouton(e, bout, "white", feuille, id_contour))
       return bout

    def __cocher_case(feuille: Canvas, id_case, tab_tags):
         tab_coord= feuille.bbox(id_case)
         larg_virgule= 6
         x= tab_coord[0]+ 3
         y= tab_coord[1] + 3
         haut= (tab_coord[3]- tab_coord[1]) - 6
         larg= (tab_coord[2] - tab_coord[0]) - 6
         tab= [x, y+ haut/2 + larg_virgule/2,
               x+ larg/2, y+ haut,
               x+ larg, y+larg_virgule,
               x+ larg, y,
               x+ larg/2, y+ haut- larg_virgule,
               x, y+ haut/2- larg_virgule/2  
         ]
         feuille.create_polygon(tab, tags= tab_tags)

#utilise id_case pour conserver les valeurs de cochage et indexer la vircule de cochage
    def __ecoute_case_cochable(e, feuille: Canvas, id_rect_cohable, id_case, tab_tags_virgule):
         if(fonction_creation_elt_page.__conteneur_valeur_case_cochage[id_case]):
            fonction_creation_elt_page.__conteneur_valeur_case_cochage[id_case]= False 
            feuille.delete(id_case)
         else:
             fonction_creation_elt_page.__conteneur_valeur_case_cochage[id_case]= True 
             fonction_creation_elt_page.__cocher_case(feuille, id_rect_cohable, tab_tags_virgule) 

    def cree_case_cochable(feuille: Canvas, x, y, larg, haut, tab_tags, couleur_ligne, nom_indication, police: Font, etat= False):
        espace_indicateur_cadre= 30
        id_indicateur= feuille.create_text(x+ larg+ espace_indicateur_cadre, y, text=nom_indication, font= police, anchor= "nw", tags= tab_tags)
        tab_coord_indicateur= feuille.bbox(id_indicateur)
        y= (tab_coord_indicateur[1]+ tab_coord_indicateur[3])/2 - haut/2
        id_rect_cochable= feuille.create_rectangle(x, y, x+ larg, y+haut, fill="white", width=1, outline= couleur_ligne, tags= tab_tags)
        id_groupe= "id_grp_case"+str(id_indicateur)
        id_case= "cochable"+str(fonction_creation_elt_page.__nombre_de_case_cochable)
        fonction_creation_elt_page.__nombre_de_case_cochable += 1
        feuille.addtag_withtag(id_groupe, id_rect_cochable)
        feuille.addtag_withtag(id_groupe, id_indicateur)
        tab_tags_virgule= tab_tags+[id_case, id_groupe]
        feuille.itemconfigure(id_groupe, activefill= fonction_creation_elt_page.__couleur_sensiblitee)
        if(etat):
            fonction_creation_elt_page.__conteneur_valeur_case_cochage[id_case]= True
            fonction_creation_elt_page.__cocher_case(feuille, id_rect_cochable, tab_tags_virgule) 
        else:
            fonction_creation_elt_page.__conteneur_valeur_case_cochage[id_case]= False
        feuille.tag_bind(id_groupe, "<Button>", lambda e: fonction_creation_elt_page.__ecoute_case_cochable(e, feuille, id_rect_cochable, id_case, tab_tags_virgule))
        return id_case  

    def __ecoute_sortie_entre_dans_bouton_rectangle(e, bout: Button, couleur):
         bout.configure(highlightbackground= couleur, background= couleur)
         
#dessin le rectangle avec les ecris a l'interieur donne une sensibilitee d'entree et sortie de la zone et retourn un id du groupe 
    def cree_bouton_rectangle(feuille: Canvas, x, y, indication, larg, haut,tab_tags, police: Font, anch, couleur_activation= "#74D1B3"):
       bout= Button(feuille, width= larg, height= haut, background= "white", highlightbackground= "white", bd=0, highlightcolor= "white", text=indication, font= police, activebackground=couleur_activation , anchor= anch,)   
       bout.bind("<Enter>", lambda e, couleur= couleur_activation: fonction_creation_elt_page.__ecoute_sortie_entre_dans_bouton_rectangle(e, bout, couleur))
       bout.bind("<Leave>", lambda e, couleur= "white": fonction_creation_elt_page.__ecoute_sortie_entre_dans_bouton_rectangle(e, bout, couleur))
       fonction_creation_elt_page.__cree_windo(x, y, bout, larg, haut, feuille, tab_tags, "nw") 
       return bout

    def sinde_ecris_en_ligne(ecris:str, police: Font, larg_dispo):#pour diviser une ecris en verticale
        lar_unit= police.measure("M") 
        n= larg_dispo/ lar_unit 
        s= ""
        tab_str= ecris.split("\\n")
        nb= len(tab_str)
        j=1
        for elt_ecris in tab_str :
            i= 0
            j+=1
            for lettre in elt_ecris:
                s += lettre
                if(i >= n):
                    s += "\n"
                    i = 0
                else:   
                   i+=1
            if(j< nb):
               s += "\n"       
        return  s
          
    def cree_zone_texte_indication(feuille: Canvas, x, y, nom_indication, police_ecriture: Font, larg, haut, anchor, tab_tags, couleur_ligne, verticale= True):    
        id_indication= feuille.create_text(x, y, text=nom_indication, font= police_ecriture, anchor= anchor, tags= tab_tags)
        tab_coord= feuille.bbox(id_indication)
        en=  Text(feuille, width= larg, highlightbackground= couleur_ligne)
        if(verticale):
            y= tab_coord[3]+ fonction_creation_elt_page.__espace_entre_indication_et_elt/2
            x= tab_coord[0] +3
            fonction_creation_elt_page.__cree_windo(x, y, en, larg, haut, feuille, tab_tags, "nw")
        else:
           x= tab_coord[2] + 2*fonction_creation_elt_page.__espace_entre_indication_et_elt + larg/2
           y= (tab_coord[1]+ tab_coord[3])/2 
           fonction_creation_elt_page.__cree_windo(x, y, en, larg, haut, feuille, tab_tags, "c")
        return en      
