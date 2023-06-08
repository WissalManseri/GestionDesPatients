from front_end.livre_page.page import Page, tk
from tkinter.font import Font
from front_end.gestionaire_graphisme.gestionaire_page.fonction_creation_elt_dans_feuille import fonction_creation_elt_page

class gestion_page_acceuille:
    def __init__(self, la_page: Page, couleur, couleur_ligne, police_1: Font, police_2: Font, police_3: Font) -> None:
        self.__la_page= la_page
        self.__nom_genrale_cadre= "pour_cadre"
        self.__largeur_minimale= 850
        self.__hauteur_minimale= 420
        self.__initialise(couleur, couleur_ligne, police_1, police_2, police_3)
        self.__larg_scroll= 5
        self.__fonction_validation= None
        self.__la_page.set_fonction(self.__accomode)

    def set_fonction_validation(self, fonction):
       self.__fonction_validation= fonction

    def __lancer_validation(self):
        if(self.__fonction_validation != None) :
            self.__fonction_validation()
        
    def __initialise(self, couleur, couleur_ligne, police_1: Font, police_2: Font, police_3: Font):
        self.__feuille= self.__la_page.get_feuile()
        larg= 800
        haut= 400
        nom_entete= "CHOIX DU PROFIL"
        haut_texte= police_1.metrics("linespace")+2 
        self.rect_conteneur= self.__feuille.create_rectangle(0, 0 , larg, haut, fill= couleur, tags=[self.__nom_genrale_cadre], width=0)
        self.__feuille.create_text(larg/2, haut_texte/2, text= nom_entete, anchor="c", tags= [self.__nom_genrale_cadre], font= police_1)
        #creation cadre elt
        espace_bord_x= 20
        espace_bord_y= 50
        self.__feuille.create_rectangle(espace_bord_x, espace_bord_y, larg- espace_bord_x, haut- espace_bord_y, fill= "white", tags= [self.__nom_genrale_cadre], width=0)
        x= espace_bord_x
        y= espace_bord_y
        l= larg- 2*espace_bord_x
        self.__cree_partie_formulaire(x, y, l, police_2, police_3, couleur_ligne)
        self.__feuille.configure(scrollregion=(0, 0, self.__largeur_minimale, self.__hauteur_minimale))

    def __cree_partie_formulaire(self, x, y, larg, police_2: Font, police_3: Font, couleur_ligne):
         h_texte= police_2.metrics("linespace")+2
         indication= "veuilllez choisir votre profil et entrez le code"
         ecart= 30
         id_indication= self.__feuille.create_text(x+ larg/2, y+ h_texte/2+ ecart, text=indication, anchor='c', tags= [self.__nom_genrale_cadre], font= police_2) 
         tab_indication= self.__feuille.bbox(id_indication)
         y= tab_indication[3]+ 27
         larg_indication= police_2.measure(indication)
         x1= x+(larg- larg_indication)/2+ 50
         x2= x+ larg- (larg- larg_indication)/2- 50
         rayon= 30
         id_bouton_radio= "radio"
         self.__id_conserveur_info_bouton_radio= "radio_acceuill1"
         self.__id_assistant= "assistant"
         self.__id_medesin= "medesin"
         fonction_creation_elt_page.cree_bouton_radio_choix(self.__feuille, x1, y, "ASSISTANT", police_3, rayon, "nw", [self.__nom_genrale_cadre, id_bouton_radio], self.__id_conserveur_info_bouton_radio, self.__id_assistant, True)
         fonction_creation_elt_page.cree_bouton_radio_choix(self.__feuille, x2, y, "MEDECIN", police_3, rayon, "ne", [self.__nom_genrale_cadre, id_bouton_radio], self.__id_conserveur_info_bouton_radio, self.__id_medesin, True)
         y= self.__feuille.bbox(id_bouton_radio)[3]+30
         x= tab_indication[0]
         id_entry= "id_en"
         entry_code= fonction_creation_elt_page.cree_entry_indication(self.__feuille, x, y, "entrez votre code pour vous connecter", police_3, 180, 30, "nw", [self.__nom_genrale_cadre, id_entry], couleur_ligne, False)
         self.__variable_contenant_code= tk.StringVar()
         entry_code.configure(font= police_3, textvariable= self.__variable_contenant_code)
         y= self.__feuille.bbox(id_entry)[3]+20
         larg_bouton= 150
         bouton_valider= fonction_creation_elt_page.cree_bouton(self.__feuille, (tab_indication[0]+ tab_indication[2])/2 -larg_bouton/2, y, larg_bouton, 30, [self.__nom_genrale_cadre], couleur_ligne, "Valider", police_3)
         bouton_valider.configure(command= self.__lancer_validation)
         
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

    def supprimer_code(self):
        self.__variable_contenant_code.set("")      

    def get_code(self):
        return self.__variable_contenant_code.get() 

    def get_id_medecin(self):
        return self.__id_medesin 

    def get_id_assistant(self):
        return self.__id_assistant 

    def get_id_profil_choisit(self):
        return fonction_creation_elt_page.valeur_choisit_par_bouton_radio_choix(self.__id_conserveur_info_bouton_radio)               