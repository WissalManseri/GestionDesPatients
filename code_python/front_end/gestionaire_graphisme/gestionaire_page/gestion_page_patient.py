from front_end.livre_page.frame_livre import frame_livre
from front_end.livre_page.page import Page
from front_end.gestionaire_graphisme.gestionaire_page.gestion_page_tableau import gestion_page_tableau
from tkinter.font import Font
from front_end.gestionaire_graphisme.gestionaire_page.fonction_creation_elt_dans_feuille import fonction_creation_elt_page
from front_end.gestionaire_graphisme.gestionaire_page.gestion_page_examination import gestion_page_examination
from front_end.gestionaire_graphisme.gestionaire_page.gestion_page_rende_vous import gestion_page_rendez_vous


class gestion_page_patient:
    def __init__(self, la_page: Page, police_1, police_3, police_4, couleur_entete, couleur, couleur_ligne) -> None:
        self.__la_page= la_page
        self.__largeur_scroll= 6
        self.__nom_entete_2= "elt_inter_1"
        self.__definition_id_page()
        self.__code_patient_courant= None
        self.__initilise_fonction_ecoute()
        x,y = self.__initialiser(couleur, couleur_ligne, police_1, police_3)
        self.__cree_page_info(x, y, police_3, couleur_entete, couleur_ligne)
        self.__feuille.configure(scrollregion=(0,0, self.__larg_min, self.__haut_min))
        self.__cree_livre_operation(x, y+ self.__hauteur_page_info+ 20, couleur_ligne, police_3, police_4, couleur_entete)
        self.__la_page.set_fonction(self.__accomode)

    def get_code_patient(self):
        return self.__code_patient_courant    

    def __definition_id_page(self):
        self.__id_page_examination= "page_examination"
        self.__id_page_rendez_vous= "Page_endez_vous"  

    def __initilise_fonction_ecoute(self):
        self.__tab_fonction= [None, None]  

    def __execute_fonction_par_bout(self, indice) :
        fonction= self.__tab_fonction[indice]
        if(fonction != None):
            fonction()    

    def set_fonction_bout(self, indice, fonction):
        self.__tab_fonction[indice]= fonction                   
  
    def __initialiser(self, couleur, couleur_ligne, police_1: Font, police_2: Font):
        self.__larg_min= 900
        self.__haut_min= 800
        self.__feuille= self.__la_page.get_feuile()
        #-------------------------------------------------
        t= 200
        x= self.__ecart_bord_x_1= 50 
        haut_ecrit= police_1.metrics("linespace")
        y= haut_ecrit+10
        self.__id_titre= self.__feuille.create_text(x+ t/2, y- haut_ecrit/2, text= "Effectuer une action sur le patient", font= police_1, anchor="c")
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
        haut_bout= 35
        larg_bout= 180
        bout_Nouveau_patient= fonction_creation_elt_page.cree_bouton(self.__feuille, x, y+ 20, larg_bout, haut_bout, [self.__nom_entete_2], couleur_ligne, "Nouveau Patient", police_2)
        bout_agenda = fonction_creation_elt_page.cree_bouton(self.__feuille, x+ larg_bout+ 40, y+ 20, larg_bout, haut_bout, [self.__nom_entete_2], couleur_ligne, "Mon agenda", police_2)
        y= self.__feuille.bbox(self.__nom_entete_2)[3]+10
        bout_Nouveau_patient.configure(command= lambda indice= 0: self.__execute_fonction_par_bout(indice))
        bout_agenda.configure(command= lambda indice= 1: self.__execute_fonction_par_bout(indice))
        #----------------------------------------------------
        self.__id_trait_bas= self.__feuille.create_line([x, y, x+t, y+t], fill= couleur_ligne)
        return x, y

    def __cree_page_info(self, x, y, police_3, couleur_entete, couleur_ligne)  :
        self.__ecart_bord_x_3= 10
        self.__ecart_bord_y_3= 10
        x+= self.__ecart_bord_x_3
        y+= self.__ecart_bord_y_3
        self.__hauteur_page_info= 100
        self.__page_information= gestion_page_tableau(self.__feuille, x, y, ["Code", "Nom", "Prenom", "Sex", "Age", "Téléphone", "Adresse", "Profession", "Date"], police_3, couleur_entete, couleur_ligne) 

    def set_tab_info_patient(self, tuple_elt):
        if(len(tuple_elt)> 0):
           self.__code_patient_courant= tuple_elt[0]
           self.__page_information.set_tab_info([tuple_elt])
        else:
            self.__code_patient_courant=  None   
            self.__page_information.set_tab_info([]) 

    def __cree_livre_operation(self, x, y, couleur_ligne, police_2, police_3, couleur_entete):
        larg= 100
        x+= self.__ecart_bord_x_3
        self.__haut_livre_operation= 400
        self.__livre_operation=   frame_livre(self.__feuille, larg, self.__haut_livre_operation, self.__id_page_examination, "white")
        self.__id_livre_operation= self.__feuille.create_window(x, y, width= larg, height= self.__haut_livre_operation, window= self.__livre_operation.get_frame_conserveur(), anchor= "nw")
        y+= self.__haut_livre_operation+ 10
        haut_bout= 35
        larg_bout= 200
        bout_choix_examination = fonction_creation_elt_page.cree_bouton(self.__feuille, x, y+ 5, larg_bout, haut_bout, [], couleur_ligne, "EXAMINATION", police_2)
        bout_choix_rendez_vous = fonction_creation_elt_page.cree_bouton(self.__feuille, x+ larg_bout+20, y+ 5, larg_bout, haut_bout, [], couleur_ligne, "RENDEZ-VOUS", police_2)
        #----------------------------------------
        bout_choix_examination.configure(command= lambda id_zone= self.__id_page_examination: self.__change_zone_operation(id_zone))
        bout_choix_rendez_vous.configure(command= lambda id_zone= self.__id_page_rendez_vous: self.__change_zone_operation(id_zone)) 
        #-----------------------------------------
        self.__cree_page_operation(couleur_ligne, police_2, police_3, couleur_entete)

    def __change_zone_operation(self, id_zone):#ici nous avons de faire si c'est necesaire tous les operation intermediare avant la presentation de la page
        self.__livre_operation.changer_page(id_zone)

    def __cree_page_operation(self, couleur_ligne, police_2, police_3, couleur_entete):
        self.__page_examination= gestion_page_examination(self.__livre_operation.get_page(self.__id_page_examination), couleur_ligne, couleur_entete, police_2, police_3) 
        self.__page_rendez_vous= gestion_page_rendez_vous(self.__livre_operation.cree_nouvelle_page(self.__id_page_rendez_vous, "white"), couleur_ligne, couleur_entete, police_2, police_3)   

    def presenter_rendez_vous(self):
        self.__livre_operation.changer_page(self.__id_page_rendez_vous)    

    def get_gestion_page_examination(self):
       return self.__page_examination

    def get_gestion_page_rendez_vous(self):
       return self.__page_rendez_vous  

    def __actualiser(self, larg, haut):
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
        self.__actualiser_page_utile((tab_coord[2]- tab_coord[0]))

    def __actualiser_page_utile(self, larg):
        larg -= 2*self.__ecart_bord_x_3
        self.__page_information.changer_taille(larg, self.__hauteur_page_info) 
        self.__feuille.itemconfigure(self.__id_livre_operation, width= larg, height= self.__haut_livre_operation) 
        self.__livre_operation.change_taille(larg- 4, self.__haut_livre_operation- 4)

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
        self.__actualiser(larg, haut)  
