from front_end.livre_page.fentre_livre import fenetre_livre 
#from front_end.petite_fenetre.generateur_petite_fen import generateur_petite_fen
from front_end.gestionaire_graphisme.gestion_premiere_structuration import gestion_structuration_1, tk
from tkinter.font import Font
from front_end.gestionaire_graphisme.gestionaire_page.gestion_page_acceuille import gestion_page_acceuille
from front_end.gestionaire_graphisme.gestionaire_page.gestion_page_enregistrement import gestion_enregistrement
from front_end.gestionaire_graphisme.gestionaire_page.gestion_page_recherche_patient import gestion_page_recherche_patient
from front_end.gestionaire_graphisme.gestionaire_page.gestion_page_acceuille_medecin import gestion_page_acceuille_medecin
from front_end.gestionaire_graphisme.gestionaire_page.gestion_page_affiche_resultat_recher import gestion_page_affichage_resultat_recherche
from front_end.gestionaire_graphisme.gestionaire_page.gestion_page_agenda import gestion_page_agenda
from front_end.gestionaire_graphisme.gestionaire_page.gestion_page_patient import gestion_page_patient
from front_end.gestionaire_graphisme.gestionaire_page.fonction_creation_elt_dans_feuille import fonction_creation_elt_page
from back_end.gestion_back_end.gestion_base import gestion_base
from back_end.constituant_elementaire.medecin import Medecin
from tkinter.messagebox import showerror, askquestion
from front_end.petite_fenetre.generateur_petite_fen_info import generateur_petite_fen_info
from front_end.gestionaire_graphisme.gestionaire_page.gestion_page_tableau import gestion_page_tableau
from front_end.gestionaire_graphisme.gestionaire_page.remplie_page_petit_fen import remplie_page_petit_fen
from back_end.gestion_back_end.gestion_controle_entrer import gestion_controle_entrer

class agencement:
    def __init__(self) -> None:
       self.__creation_elt_1()
       self.__creation_elt_2()
       self.__creation_elt_3()
       self.__creation_elt_4()
       self.__creation_elt_5()
       self.__parametrage_1()
       self.__parametrage_2()
       self.__cree_bout_retour_et_acceuil()
       self.__lancer_applie()

# zone des creation objet qui sont des fonction qui regroupe de objets qui sont creer tout en suivant une depandence     
    
    def __creation_elt_1(self):#creation des attribut globale
      self.__identifie_medecin= "(vous)"
      self.__couleur_1= "#EEEEEE"
      self.__couleur_2= "#74D1B3"
      self.__couleur_3= "#C2DB85" 
      self.__couleur_bordure= "#707070"
      self.__id_page_acceuille_1= 'acceuile'
      self.__id_page_enregistrement= "save_patient"
      self.__id_page_recherche_patient= "recherche_patient"
      self.__id_page_acceuille_2= "acc_patient"
      self.__id_page_result_recherche_patient= "result_rech_patient"
      self.__id_page_agenda= "agenda"
      self.__id_page_patient_unique= "patient_unique"
      self.__largeur_scroll= 6
      gestion_page_tableau.couleur_ligne_selecte= self.__couleur_2
      self.__tab_trace_evolution_id= [self.__id_page_acceuille_1]
      self.__tab_trace_evolution_acceuil= [self.__id_page_acceuille_1]

    def __creation_elt_2(self):#pour la fenetre et l'indexation de la parge porteuse
      #nous produisons la fenentre et indexons la frame fenetre sense conserver toutes les pages
       self.__fenetre_appli= fenetre_livre(80, 85, "page", self.__couleur_1)
       self.__page_porteuseuse= self.__fenetre_appli.get_frame_livre_originale().get_page("page")
      #les constructeurs de boite de dialogue  personnalisee de texte 
       self.__contructeur_fen_info = generateur_petite_fen_info(self.__fenetre_appli.get_fenetre())
      #ouverture de la base de donnee
       self.__manipule_base= gestion_base("conservateur/Base_donnee_hopitale.db")
       
    def __creation_elt_3(self):#pour les polices et photo et photos
      nom_police= "Tauri"
      self.__police_1= Font(family=nom_police, weight="normal", size= 26)
      self.__police_2= Font(family=nom_police, weight="normal", size= 20)
      self.__police_3= Font(family=nom_police, weight="normal", size= 15)
      self.__police_4= Font(family=nom_police, weight="normal", size= 13)
      self.__police_5= Font(family=nom_police, weight="normal", size= 9)
      self.__police_6= Font(family=nom_police, weight="normal", size= 8)
      gestion_page_tableau.police_ecris_dans_tableau= self.__police_4
      self.__photo_logo= tk.PhotoImage(file= "image/logo.png")
      self.__photo_deco= tk.PhotoImage(file="image/deco.png")
      self.__photo_deco_2= tk.PhotoImage(file= "image/deco_2.png")
      self.__fenetre_appli.set_icone(self.__photo_logo)
      
    def __creation_elt_4(self):#pour gestion de la structure generale de l'appli et l'indexation de la frame_live contneur des page utiles
        self.__decor_permanant= gestion_structuration_1(self.__page_porteuseuse.get_feuile(), self.__id_page_acceuille_1,  self.__couleur_2, self.__police_1, self.__police_4, self.__photo_logo, self.__couleur_bordure)
        self.__conteneur_page_appli= self.__decor_permanant.get_conteneur_page()

    def __creation_elt_5(self):#creation des pages
      #creation de la premeire page d'acceuille
        self.__manipule_page_acceuille= gestion_page_acceuille(self.__conteneur_page_appli.get_page(self.__id_page_acceuille_1), self.__couleur_2, self.__couleur_bordure, self.__police_1, self.__police_2, self.__police_3)
      #creation de la page d'enregistrement des patients
        self.__manipule_page_enregistrement= gestion_enregistrement(self.__conteneur_page_appli.cree_nouvelle_page(self.__id_page_enregistrement, "white"), self.__couleur_2, self.__couleur_bordure, self.__police_2, self.__police_3, self.__police_4, self.__police_5, self.__police_6, self.__photo_deco)   
      #creation de la page de recherche des patients
        self.__manipule_page_recherche= gestion_page_recherche_patient(self.__conteneur_page_appli.cree_nouvelle_page(self.__id_page_recherche_patient, "white"), self.__couleur_2, self.__police_1, self.__police_3, self.__couleur_bordure)
      #creation page acdeuille medecin
        self.__manipule_page_acceuille_medecin=   gestion_page_acceuille_medecin(self.__conteneur_page_appli.cree_nouvelle_page(self.__id_page_acceuille_2, "white"), self.__photo_deco_2, self.__couleur_2, self.__couleur_bordure, self.__police_1, self.__police_3)
      #creation page resultat recherche patient
        self.__manipule_page_resultat_rech_patient= gestion_page_affichage_resultat_recherche(self.__conteneur_page_appli.cree_nouvelle_page(self.__id_page_result_recherche_patient, "white"), self.__police_1, self.__police_3, self.__couleur_3, self.__couleur_2, self.__couleur_bordure)  
      #creation page_agenda 
        self.__manipule_page_agenda= gestion_page_agenda(self.__conteneur_page_appli.cree_nouvelle_page(self.__id_page_agenda, "white"), self.__police_1, self.__police_3, self.__couleur_3, self.__couleur_2, self.__couleur_bordure)
      #creatient page patient
        self.__manipule_page_patient= gestion_page_patient(self.__conteneur_page_appli.cree_nouvelle_page(self.__id_page_patient_unique, "white"), self.__police_1, self.__police_3, self.__police_4, self.__couleur_3, self.__couleur_2, self.__couleur_bordure)
      #conservation page examination
        self.__page_examination=  self.__manipule_page_patient.get_gestion_page_examination()     
      #conservation page examination
        self.__page_rendez_vous=  self.__manipule_page_patient.get_gestion_page_rendez_vous() 

#zone de parametrage 
    def __parametrage_1(self):
      self.__page_porteuseuse.set_fonction(self.__accomodation_page) 

    def __parametrage_2(self):#nous connectons les bouton des pages aux actions de maniers permanante
      self.__manipule_page_acceuille.set_fonction_validation(self.__changement_accueille_vers_autre)
      #----------------------------------------------------------------
      self.__manipule_page_enregistrement.set_fonction_bouton(0, self.__enregistrement_patient)
      self.__manipule_page_enregistrement.set_fonction_bouton(1, self.__annuler_donnee_patient)
      self.__manipule_page_enregistrement.set_fonction_bouton(2, self.__changement_enregistrement_vers_info_patient_pour_importer)
      self.__manipule_page_enregistrement.set_fonction_bouton(3, self.__changement_enregistrement_vers_info_patient_pour_supprimer)
      #----------------------------------------------------------------
      self.__manipule_page_patient.set_fonction_bout(0, self.__nouveau_patient_pris_dans_base) 
      self.__manipule_page_patient.set_fonction_bout(1, self.__nouveau_patient_pris_dans_agenda)
      #---------------------------------------------------------------- 
      self.__manipule_page_recherche.set_fonction_tous_patient(self.__aficher_info_tous_les_patients)
      self.__manipule_page_recherche.set_fonction_choix_patient(self.__recupere_info_elet_choix)
      #----------------------------------------------------------------
      self.__manipule_page_acceuille_medecin.set_fonction_ecoute(0, self.__changement__acceuille_medecin_vers_patient)
      self.__manipule_page_acceuille_medecin.set_fonction_ecoute(1, self.__changement__acceuille_medecin_vers_agenda)
      #----------------------------------------------------------------
      self.__manipule_page_resultat_rech_patient.set_fonction_bouton(0, self.__actualiser_page_resultat_recherche_patient)
      self.__manipule_page_resultat_rech_patient.set_fonction_bouton(1, self.__afficher_info_tab_patient)
      self.__manipule_page_resultat_rech_patient.set_fonction_bouton(3, self.__changement_resultat_vers_recherche_patient)
      #--------------------------------------------------------------------- 
      self.__page_examination.set_fonction(0, self.___ajouter_examination)
      self.__page_examination.set_fonction(1, self.__supprimer_examination)
      #-----------------------------------------------------------------------
      self.__page_rendez_vous.set_fonction(0, self.__ajouter_rendez_vous)
      self.__page_rendez_vous.set_fonction(1, self.__supprimer_rendez_vous)
      #----------------------------------------------------------------------- 
      self.__manipule_page_agenda.set_fonction(0, self.__importer_agenda_medecin)
      self.__manipule_page_agenda.set_fonction(1, self.__quitter_agenda_vers_patient)
      
#les fonction dans de bouton et echange
    def __importer_agenda_medecin(self):
      self.__manipule_page_agenda.set_tab_in(self.__manipule_base.recuper_agenda(self.__medecin_courant.get_code()))

    def __quitter_agenda_vers_patient(self):
      tab_elt= self.__manipule_page_agenda.get_ligne_select()
      if(tab_elt == None):
             showerror("Absence de données", "Veuillez d'abord selectionner une ligne")
      else:
        mes= askquestion("Autoriser action", "Voulez vous effectuer des traitements sur la ligne selectionnée ?")
        if(mes == "yes"):
              if(self.__tab_trace_evolution_id[1]== self.__id_page_patient_unique):
                self.__recule_dans_trace_page()
              else:
                 self.__changer_page(self.__id_page_patient_unique) 
              self.__manipule_page_patient.presenter_rendez_vous()    
              self.__importer_info_patient_dans_page_patient(self.__manipule_base.recuper_donner_table_selon_condition("Patient", [["Code_patient", tab_elt[2] ]] )[0]) 

    def __nouveau_patient_pris_dans_base(self):
      self.__manipule_page_resultat_rech_patient.set_fonction_bouton(2, self.__importer_info_patient_dans_operation_sur_patient)
      self.__changer_page(self.__id_page_result_recherche_patient)  

    def __importer_info_patient_dans_operation_sur_patient(self):
        tab_elt= self.__manipule_page_resultat_rech_patient.get_ligne_select()
        if(tab_elt == None):
           showerror("Absence de données", "Veuillez d'abord selectionner une ligne")
        else:
          mes= askquestion("Autoriser action", "Voulez vous effectuer des traitements sur le patient selectionnée ?")
          if(mes == "yes"):
             self.__recule_dans_trace_page() 
             self.__importer_info_patient_dans_page_patient(tab_elt)

    def __signaler_medecin_courant_dans_tableau(self, tab_elt, nom_medecin):
          nb= len(tab_elt)
          if(nb> 0):
            nb_2= len(tab_elt[0])
            nom_indexer= nom_medecin+  self.__identifie_medecin
            for i in range(nb):
              if(tab_elt[i][0] == nom_medecin):
                nov_tuple= (nom_indexer,)
                for j in range(1, nb_2):
                   nov_tuple += (tab_elt[i][j], )
                tab_elt[i]= nov_tuple   
          return tab_elt     
    
    def __importer_info_patient_dans_page_patient(self, tab_elt):
            self.__manipule_page_patient.set_tab_info_patient(tab_elt)
            if(len(tab_elt) > 0):
              nom_medecin= self.__medecin_courant.get_nom()
              code_patient= self.__manipule_page_patient.get_code_patient()
              self.__page_examination.set_tab_in(self.__signaler_medecin_courant_dans_tableau(self.__manipule_base.recuper_examination(code_patient), nom_medecin))  
              self.__page_rendez_vous.set_tab_in(self.__signaler_medecin_courant_dans_tableau(self.__manipule_base.recuper_rendez_vous(code_patient), nom_medecin))    
            else:
              self.__page_examination.set_tab_in([])  
              self.__page_rendez_vous.set_tab_in([])   
                     
    def ___ajouter_examination(self):
      code_patient= self.__manipule_page_patient.get_code_patient()
      if(code_patient != None):
        larg_petite_fen= 650
        haut_petite_fen= 400
        x, y= self.__fenetre_appli.get_coord_centre_fen(larg_petite_fen, haut_petite_fen)
        page_centre, tab_bout= self.__contructeur_fen_info.creation_fen(larg_petite_fen, haut_petite_fen, x, y, "Ajout d'une examination", ["Valider", "Annuler"], self.__police_4, self.__couleur_1, self.__couleur_bordure)
        tab_en, tab_text = remplie_page_petit_fen.fabrique_page_recup_donnee_examination(page_centre, self.__police_4, self.__police_4, self.__police_6, self.__couleur_bordure)
        bout_valider: tk.Button= tab_bout[0]
        bout_annuler: tk.Button= tab_bout[1]
        bout_annuler.configure(command= self.__contructeur_fen_info.fermer)
        bout_valider.configure(command= lambda : self.__complete_ajout_examination(code_patient, self.__medecin_courant.get_code(), tab_en, tab_text, page_centre.get_feuile()))
        self.__contructeur_fen_info.fait__attendre()
      else:
         showerror("Absence de données", "Veuillez d'abord importer les informations d'un patient")  

    def __complete_ajout_examination(self, code_p, code_m,  tab_entry, tab_zone_texte, feuille: tk.Canvas):
      tab_requette= [code_p, code_m]
      en: tk.Entry
      text: tk.Text 
      remplie_page_petit_fen.effacer_tout_erreur(feuille)
      for en in tab_entry:
        tab_requette.append(en.get().strip().upper())
      for text in tab_zone_texte:
        tab_requette.append(text.get("1.0", "end").strip())  
      tab_indice_incorrecte, tab_requette = gestion_controle_entrer.controle_donnee_examination_rendez_vous(tab_requette)  
      if(len(tab_indice_incorrecte) != 0):
        remplie_page_petit_fen.signaler_erreur_avec_petit_ecris(tab_indice_incorrecte, feuille)
      else:  
        if(self.__manipule_base.ajouter_elt_dans_table("Examination", tab_requette)): 
            del tab_requette[0]
            tab_requette[0]= self.__medecin_courant.get_nom()+ self.__identifie_medecin
            self.__page_examination.ajout_ligne_in(tab_requette) #nous actualisons le tableau d'info
        self.__contructeur_fen_info.fermer()        

    def __supprimer_examination(self):
      tab_elt= self.__page_examination.get_ligne_select()       
      if(tab_elt != None):
        if(tab_elt[0]== self.__medecin_courant.get_nom()):
          mes= askquestion("Autoriser action", "Voulez vous supprimer l'examination selctionnée")
          if(mes == "yes"):
              code_patient= self.__manipule_page_patient.get_code_patient()
              self.__page_examination.enlever_ligne()
              self.__manipule_base.supprimer_donner_table_selon_condition("Examination", [["Code_patient", code_patient], ["Code_medecin", self.__medecin_courant.get_code()], ["Date", tab_elt[1]], ["Heure_debut", tab_elt[2]], ["Heure_fin", tab_elt[3]]])
        else:
           showerror("Autorisation", "Vous n'avez pas le droit de supprimer cette examination")      
      else:
        showerror("Absence de données", "Veuillez d'abord selectionner une ligne d'examination")    
              
    def __ajouter_rendez_vous(self):
      code_patient= self.__manipule_page_patient.get_code_patient()
      if(code_patient != None):
        larg_petite_fen= 650
        haut_petite_fen= 300
        x, y= self.__fenetre_appli.get_coord_centre_fen(larg_petite_fen, haut_petite_fen)
        page_centre, tab_bout= self.__contructeur_fen_info.creation_fen(larg_petite_fen, haut_petite_fen, x, y, "Ajout d'un rendez_vous", ["Valider", "Annuler"], self.__police_4, self.__couleur_1, self.__couleur_bordure)
        tab_entry =remplie_page_petit_fen.fabrique_page_recup_donnee_rendevous(page_centre, self.__police_4, self.__police_4, self.__police_6, self.__couleur_bordure)
        bout_valider: tk.Button= tab_bout[0]
        bout_annuler: tk.Button= tab_bout[1]
        bout_annuler.configure(command= self.__contructeur_fen_info.fermer)
        bout_valider.configure(command= lambda: self.__complete_ajout_rendez_vous(code_patient, self.__medecin_courant.get_code(),tab_entry, page_centre.get_feuile()))
        self.__contructeur_fen_info.fait__attendre()
      else:
         showerror("Absence de données", "Veuillez d'abord importer les informations d'un patient")  

    def __complete_ajout_rendez_vous(self, c_p, c_m, tab_entry, feuille):
      tab_requette= [c_p, c_m]
      en: tk.Entry
      remplie_page_petit_fen.effacer_tout_erreur(feuille)
      for en in tab_entry:
        tab_requette.append(en.get().strip().upper())
      tab_indice_incorrecte, tab_requette = gestion_controle_entrer.controle_donnee_examination_rendez_vous(tab_requette, False) 
      if(len(tab_indice_incorrecte) != 0):
        remplie_page_petit_fen.signaler_erreur_avec_petit_ecris(tab_indice_incorrecte, feuille)
      else: 
        if(self.__manipule_base.ajouter_elt_dans_table("Rendez_vous", tab_requette)):
            del tab_requette[0]
            tab_requette[0]= self.__medecin_courant.get_nom()+ self.__identifie_medecin
            self.__page_rendez_vous.ajout_ligne_in(tab_requette) #nous actualisons le tableau d'info      
        self.__contructeur_fen_info.fermer()                        

    def __supprimer_rendez_vous(self):
      tab_elt= self.__page_rendez_vous.get_ligne_select()       
      if(tab_elt != None):
        if(tab_elt[0]== self.__medecin_courant.get_nom()):
          mes= askquestion("Autoriser action", "Voulez vous supprimer l'examination selctionnée")
          if(mes == "yes"):
              code_patient= self.__manipule_page_patient.get_code_patient()
              self.__page_rendez_vous.enlever_ligne()
              self.__manipule_base.supprimer_donner_table_selon_condition("Rendez_vous", [["Code_patient", code_patient], ["Code_medecin", self.__medecin_courant.get_code()], ["Date", tab_elt[1]], ["Heure", tab_elt[2]]])
        else:
           showerror("Autorisation", "Vous n'avez pas le droit de supprimer ce rendez-vous")      
      else:
        showerror("Absence de données", "Veuillez d'abord selectionner une ligne d'examination")         

    def __nouveau_patient_pris_dans_agenda(self):
      self.__changer_page(self.__id_page_agenda) 

    def __changement_accueille_vers_autre(self):
      id_profil = self.__manipule_page_acceuille.get_id_profil_choisit()
      if(id_profil== self.__manipule_page_acceuille.get_id_assistant()):
        if(self.__manipule_base.recuperer_tab_donne_assistant_par_code(self.__manipule_page_acceuille.get_code())!= None):
          self.__changer_page(self.__id_page_enregistrement)
          self.__manipule_page_acceuille.supprimer_code()
        else:
            mes= showerror("Erreur de code", "Code assistant non reconnu")
      else:
        tab_info_medecin= self.__manipule_base.recuperer_tab_donne_medecin_par_code(self.__manipule_page_acceuille.get_code())
        if(tab_info_medecin != None):
            self.__changer_page(self.__id_page_acceuille_2)
            self.__medecin_courant= Medecin([elt for elt in tab_info_medecin])#nous conservons les donnees du medecin qui est entraint d'utilisee
            self.__manipule_page_acceuille.supprimer_code()
            self.__importer_info_patient_dans_page_patient([])
            self.__manipule_page_agenda.set_tab_in([])
        else:
            mes= showerror("Erreur de code", "Code medecin non reconnu")

    def __changement__acceuille_medecin_vers_patient(self):
      self.__changer_page(self.__id_page_patient_unique)

    def __changement__acceuille_medecin_vers_agenda(self):
      self.__changer_page(self.__id_page_agenda)

    def __changement_enregistrement_vers_info_patient_pour_importer(self):
        self.__manipule_page_resultat_rech_patient.set_fonction_bouton(2, self.__importeur_patient_vers_enregistrement)
        self.__changer_page(self.__id_page_result_recherche_patient) 

    def __importeur_patient_vers_enregistrement(self):
        tab_elt= self.__manipule_page_resultat_rech_patient.get_ligne_select()
        if(tab_elt == None):
           showerror("Absence de données", "Veuillez d'abord selectionner une ligne")
        else:
          mes= askquestion("Autoriser action", "Voulez vous importer les données de la ligne selctionnée ?")
          if(mes == "yes"):
            self.__recule_dans_trace_page()
            self.__manipule_page_enregistrement.set_tab_info_patient(tab_elt)   

    def __changement_enregistrement_vers_info_patient_pour_supprimer(self):
        self.__manipule_page_resultat_rech_patient.set_fonction_bouton(2, self.__suppression_patient)
        self.__changer_page(self.__id_page_result_recherche_patient) 

    def __suppression_patient(self):
        tab_elt= self.__manipule_page_resultat_rech_patient.get_ligne_select()
        if(tab_elt == None):
           showerror("Absence de données", "Veuillez d'abord selectionner une ligne")
        else:
          mes= askquestion("Autoriser action", "Voulez vous supprimer les données de la ligne selctionnée")
          if(mes == "yes"):
            self.__manipule_page_resultat_rech_patient.enlever_ligne()#cette ligne enleve la ligne dans la page mais nous restons en pocetion de celle-ci grace a tab_elt qui a pointer sur la liste plus tot
            self.__manipule_base.supprimer_donner_table_selon_condition("Patient", [ ["Code_patient", tab_elt[0]] ])

    def __enregistrement_patient(self):
       tab_indice_donnee_incorecte, tab_elt= gestion_controle_entrer.controle_donnee_patient(self.__manipule_page_enregistrement.get_tab_info_patient())
       if(len(tab_indice_donnee_incorecte) != 0):
         self.__manipule_page_enregistrement.afficher_petit_message_erreur(tab_indice_donnee_incorecte)
         mes= showerror("Erreur d'enregistrement des informations", "Veuillez vérifier vos informations puis reesayer")   
       else:
          if(self.__manipule_base.ajouter_elt_dans_table("Patient", tab_elt)):
              self.__manipule_page_enregistrement.supprimer_valeur_dans_entry()
          else:
              mes= askquestion("Autoriser action", f"Voulez vous modifier les informations du patient ayant le code {tab_elt[0]} ?")
              if(mes == "yes"):
                if(self.__manipule_base.modifier_patient(tab_elt)):
                  self.__manipule_page_enregistrement.supprimer_valeur_dans_entry()
                else:   
                    mes= showerror("Erreur de modification des informations", "Veuillez vérifier vos informations puis reesayer")   

    def __changement_resultat_vers_recherche_patient(self):
      self.__changer_page(self.__id_page_recherche_patient) 

    def __actualiser_page_resultat_recherche_patient(self):
      self.__manipule_page_resultat_rech_patient.set_info_utile(self.__manipule_base.recuper_donner_table_selon_condition("Patient", self.__manipule_page_resultat_rech_patient.get_tab_elt_de_requette()) )  

    def __afficher_info_tab_patient(self):
        larg_petite_fen= 600
        haut_petite_fen= 300
        x, y= self.__fenetre_appli.get_coord_centre_fen(larg_petite_fen, haut_petite_fen)
        x= int(x)
        y= int(y)
        tab_elt_requette= self.__manipule_page_resultat_rech_patient.get_tab_elt_de_requette()
        mot= "Notre tableau presente les données "
        if(len(tab_elt_requette)== 0):
          mot+= "\nde tous les patients de la base"
        else:
          mot += "\ndes patients respectant les caracteristiques suivantes :"
          for elt in tab_elt_requette:
            mot += f"\n-) {elt[0]}= {elt[1]}"
        page_centrale, tab_bout= self.__contructeur_fen_info.creation_fen(larg_petite_fen, haut_petite_fen, x, y, "Information sur le contenu du tableau de patient", ["Fermer"], self.__police_4, self.__couleur_1, self.__couleur_bordure)
        remplie_page_petit_fen.fabrique_ecris_info(page_centrale, mot, self.__police_4)
        bout_ferme: tk.Button= tab_bout[0]
        bout_ferme.configure(command= self.__contructeur_fen_info.fermer)
        self.__contructeur_fen_info.fait__attendre()

  
    def  __annuler_donnee_patient(self):
      self.__manipule_page_enregistrement.supprimer_valeur_dans_entry() 

    def __aficher_info_tous_les_patients(self):
      self.__recule_dans_trace_page()   
      self.__manipule_page_resultat_rech_patient.set_tab_elt_de_requette([])
      self.__manipule_page_resultat_rech_patient.set_info_utile(self.__manipule_base.recuper_donner_table_selon_condition("Patient"))  
      
    def __recupere_info_elet_choix(self):
      tab= self.__manipule_page_recherche.get_info_case_cochable()
      tab_indicateur= []
      tab_de_requette= []
      #on tri les informations choisit 
      for elt in tab:
        if(elt[2]):
          tab_indicateur.append(elt[0])
          tab_de_requette.append ([elt[1]]) 
      #------------------------------------------------------------------------------    
      larg_petite_fen= 600
      haut_petite_fen= 300
      x, y= self.__fenetre_appli.get_coord_centre_fen(larg_petite_fen, haut_petite_fen)
      page_centre, tab_bout= self.__contructeur_fen_info.creation_fen(larg_petite_fen, haut_petite_fen, x, y, "Récuperation des valeurs de recherche", ["Valider", "Annuler"], self.__police_4, self.__couleur_1, self.__couleur_bordure)
      bout_valider: tk.Button= tab_bout[0]
      bout_annuler: tk.Button= tab_bout[1]
      bout_annuler.configure(command= self.__contructeur_fen_info.fermer)
      #--------------------------------------------------------------------------------
      tab_en= remplie_page_petit_fen.fabrique_liste_entry(page_centre, tab_indicateur, self.__police_4, self.__couleur_bordure)
      bout_valider.configure(command= lambda : self.__execute_recherche_restrins_patient(tab_de_requette, tab_en))
      self.__contructeur_fen_info.fait__attendre()
       
    def __execute_recherche_restrins_patient(self, tab_requette: list, tab_entry):#les 2 table doivent avoir la meme taille 
      en:tk.Entry
      nb= len(tab_requette)
      for i in range(nb):
        en= tab_entry[i]
        tab_requette[i].append(en.get().strip().upper())
      self.__manipule_page_resultat_rech_patient.set_tab_elt_de_requette(tab_requette)
      self.__recule_dans_trace_page()
      self.__manipule_page_resultat_rech_patient.set_info_utile(self.__manipule_base.recuper_donner_table_selon_condition("Patient", tab_requette))
      self.__contructeur_fen_info.fermer()
         

#les fonctions utiliser globalement
    def __accomodation_page(self):
      larg= self.__fenetre_appli.get_largeur_fenetre()
      haut=  self.__fenetre_appli.get_hauteur_fenetre()
      self.__decor_permanant.accomodation(larg, haut)
      l= gestion_structuration_1.largeur_minimale_visibilite()
      h= gestion_structuration_1.hauteur_minimale_visiblilite()
      if(l> larg):
         self.__page_porteuseuse.change_larg_scroll_x(self.__largeur_scroll)
      else:
         self.__page_porteuseuse.change_larg_scroll_x(0)
      if(h> haut):
         self.__page_porteuseuse.change_larg_scroll_y(self.__largeur_scroll)
      else:
         self.__page_porteuseuse.change_larg_scroll_y(0)

    def __lancer_applie(self):#ceci doit etre la derniere partie a appeler est s'occupe des derniers detail et ouvre l'appli 
        self.__fenetre_appli.lancer_la_boucle_execution_de_la_fentre() 
        self.__manipule_base.fermer_base()
    
    def __changer_page(self, id_page):#ici nous devons gerer tous les parametres qu'il faut avant de passer a l'autre page
      if(self.__conteneur_page_appli.changer_page(id_page) ):
         self.__tab_trace_evolution_id.insert(0, id_page)
         if(id_page == self.__id_page_acceuille_2):
           self.__tab_trace_evolution_acceuil.insert(0, id_page)      

#gestion des boutons de navigation globales
    def __cree_bout_retour_et_acceuil(self):#ici on cree et initialise
       feuille= self.__page_porteuseuse.get_feuile()
       larg_bout= 100
       haut_bout= 30
       x= 2
       y= 50
       bout_accueil= fonction_creation_elt_page.cree_bouton(feuille, x, y, larg_bout, haut_bout, [], self.__couleur_bordure, "Accueil", self.__police_3, self.__couleur_1)
       bout_accueil.configure(command= self.__recule_dans_trace_page_acceuil)
       bout_retour= fonction_creation_elt_page.cree_bouton(feuille, x, y+ haut_bout+ 5, larg_bout, haut_bout, [], self.__couleur_bordure, "Retour", self.__police_3, self.__couleur_1)
       bout_retour.configure(command= self.__recule_dans_trace_page)

    def __recule_dans_trace_page(self):
       if(len(self.__tab_trace_evolution_id)> 1):
         self.__conteneur_page_appli.changer_page(self.__tab_trace_evolution_id[1])
         if(self.__tab_trace_evolution_acceuil.__contains__(self.__tab_trace_evolution_id[0])):
            del self.__tab_trace_evolution_acceuil[0]
         del self.__tab_trace_evolution_id[0]

    def  __recule_dans_trace_page_acceuil(self):
         self.__conteneur_page_appli.changer_page(self.__tab_trace_evolution_acceuil[0])
         self.__tab_trace_evolution_id= self.__tab_trace_evolution_acceuil.copy()     

