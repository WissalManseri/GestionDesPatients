from front_end.livre_page.page import Page
from front_end.gestionaire_graphisme.gestionaire_page.fonction_creation_elt_dans_feuille import fonction_creation_elt_page, Font

class gestion_page_recherche_patient:
  def __init__(self, la_page: Page, couleur, police_1, police_2, couleur_ligne) :
    self.__la_page= la_page
    self.__nom_genrale_cadre= "cadre_genrale"
    self.__largeur_minimale= 850
    self.__hauteur_minimale= 520
    self.__larg_scroll= 5
    self.__initilisation_fonction()
    self.__initialiser(couleur, police_1, police_2, couleur_ligne)
    self.__feuille.configure(scrollregion=(0, 0, self.__largeur_minimale, self.__hauteur_minimale))
    self.__la_page.set_fonction(self.__accomode)

  def __initilisation_fonction(self):
       self.__tab_fonction_ecoute_bouton= [None, None]

  def set_fonction_tous_patient(self, fonction):
    self.__tab_fonction_ecoute_bouton[0]= fonction   

  def set_fonction_choix_patient(self, fonction):
    self.__tab_fonction_ecoute_bouton[1]= fonction 

  def get_info_case_cochable(self):
    tab_info= []
    for nom, id_case in self.__tab_id_conteneur_inf_case.items():
      tab_info.append([self.__tab_corespondance[nom], nom, fonction_creation_elt_page.valeur_case_cochage(id_case)])
    return tab_info  

  def __execution_fonction_par_bouton(self, indice):
      fonction= self.__tab_fonction_ecoute_bouton[indice]
      if(fonction != None):
         fonction()        

  def __initialiser(self, couleur, police_1: Font, police_2, couleur_ligne):
        self.__feuille= self.__la_page.get_feuile()
        larg= 800
        haut= 500
        self.rect_conteneur= self.__feuille.create_rectangle(0, 0 , larg, haut, fill= couleur, tags=[self.__nom_genrale_cadre], width=0)
        nom_entete= "Recherche du patient"
        haut_texte= police_1.metrics("linespace")+2 
        self.__feuille.create_text(larg/2, haut_texte/2, text= nom_entete, anchor="c", tags= [self.__nom_genrale_cadre], font= police_1)
        #creation cadre elt
        espace_bord_x= 20
        espace_bord_y= 50
        self.__feuille.create_rectangle(espace_bord_x, espace_bord_y, larg- espace_bord_x, haut, fill= "white", tags= [self.__nom_genrale_cadre], width=0)
        #la ligne du bas
        epaiseur_trait= 1
        y_trait= haut- epaiseur_trait
        self.__feuille.create_line([espace_bord_x, y_trait, larg- espace_bord_x, y_trait], width=1, fill= couleur_ligne, tags= [self.__nom_genrale_cadre])
        espace_1= 50
        espace_2= 20
        x= espace_bord_x+ espace_1
        y= espace_bord_y+ espace_2
        l= larg- 2*espace_1- espace_bord_x
        self.__cree_elt_interne(x, y, l, couleur_ligne, police_2)
        
  def __cree_elt_interne(self, x, y, larg, couleur_ligne, police_2: Font):
         haut_bout_tout= 35 
         id_bout= "id_bout_tous_patient"
         bout_tous_patient= fonction_creation_elt_page.cree_bouton(self.__feuille, x, y, larg, haut_bout_tout, [self.__nom_genrale_cadre, id_bout], couleur_ligne, "Voir tous les patients", police_2)
         bout_tous_patient.configure(command= lambda : self.__execution_fonction_par_bouton(0))
         y= self.__feuille.bbox(id_bout)[3]+ 20
         #--------------------------------------------------------------------------------
         haut_cadre= 300
         page_entry= Page(self.__feuille, larg, haut_cadre, "white")
         id_cadre= self.__feuille.create_window(x, y, width= larg, height= haut_cadre, window= page_entry.get_support(),anchor="nw",  tags=[self.__nom_genrale_cadre])
         page_entry.get_support().configure(bd=1, background= couleur_ligne)
         feuille_interne= page_entry.get_feuile()
         y = 20
         haut_ecris_interne= police_2.metrics("linespace")
         id_titre= feuille_interne.create_text(larg/2, y+ haut_ecris_interne/2, text="Veuillez cocher les éléments de recherche", font= police_2, anchor="c")
         y= feuille_interne.bbox(id_titre)[3]+40
         #---------------------------------------------------------------------------------
         larg_case= 20
         haut_case= 20
         espace_entre_case= 20
         a= x
         x = 50
         tab_indication_case_cochable= [["Code du patient", "Code_patient"], ["Nom", "Nom"], ["Prenom", "Prenom"], ["Date d'inscription", "Date_inscription"], ["Date de naissance", "Date_naissance"], ["Profession", "Proffession"]]
         self.__tab_id_conteneur_inf_case= {}
         self.__tab_corespondance= {}
         x_bord_case_cochable= 0
         for elt in tab_indication_case_cochable:
            id_case= fonction_creation_elt_page.cree_case_cochable(feuille_interne, x, y, larg_case, haut_case, [elt[1]], couleur_ligne, elt[0], police_2)
            self.__tab_id_conteneur_inf_case[elt[1]]=  id_case
            self.__tab_corespondance[elt[1]]= elt[0]
            tab_coord_case= feuille_interne.bbox(elt[1])
            y= tab_coord_case[3]+ espace_entre_case
            x_bord_case_cochable= tab_coord_case[2]
         feuille_interne.configure(scrollregion=(0, 0, x_bord_case_cochable
         +20, y+20))
         if(x_bord_case_cochable< larg):
            page_entry.change_larg_scroll_x(0)
         if(y< haut_cadre):
            page_entry.change_larg_scroll_y(0)
         else:
             page_entry.change_larg_scroll_y(6)
         #------------------------------------------------------------------------------------
         hauteur_petit_bout= 40
         larg_petit_bout= 90
         x= a + (larg- larg_petit_bout)/2 
         y= self.__feuille.bbox(id_cadre)[3]+ 20
         valider_choix= fonction_creation_elt_page.cree_bouton(self.__feuille, x, y, larg_petit_bout, hauteur_petit_bout, [self.__nom_genrale_cadre], couleur_ligne, "Valider", police_2)
         valider_choix.configure(command= lambda : self.__execution_fonction_par_bouton(1))   
         
  def __centralise(self, larg, haut):
       tab_coord= self.__feuille.bbox(self.__nom_genrale_cadre)
       self.__feuille.move(self.__nom_genrale_cadre, larg/2- (tab_coord[0]+ tab_coord[2])/2, haut/2- (tab_coord[1]+ tab_coord[3])/2)      
    
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
        self.__centralise(larg, haut)      
