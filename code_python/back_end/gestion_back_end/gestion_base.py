import sqlite3

class gestion_base:
    def __init__(self, nom_base) -> None:
         self.__la_base= sqlite3.connect(nom_base)
         self.__executeur= self.__la_base.cursor()
         
    def  fermer_base(self):
        self.__la_base.close()   

    def recuperer_tab_donne_medecin_par_code(self, code_medecin):
        self.__executeur.execute(f"SELECT * FROM Medecin WHERE Code_medecin= '{code_medecin}'")
        return self.__executeur.fetchone()
        
    def recuperer_tab_donne_assistant_par_code(self, code_assistant):
        self.__executeur.execute(f"SELECT * FROM Assistant WHERE Code_assistant= '{code_assistant}'")   
        return self.__executeur.fetchone() 

    def ajouter_elt_dans_table(self, nom_table, tab_info):
        nb = len(tab_info)
        if(nb != 0):
            try:
                liste_elt= (tab_info[0],)
                for i in range(1, nb):
                    liste_elt= liste_elt+ (tab_info[i],)
                la_requette= f"INSERT INTO {nom_table} VALUES {liste_elt}"
                self.__executeur.execute(la_requette)
                self.__la_base.commit()
                return True
            except:
                return False 
        return False        

    def recuper_examination(self, code_patient):
        la_requette= f"SELECT Nom, Date, Heure_debut, Heure_fin,  Type, Remarque, Resultat, Prescription FROM Medecin AS m INNER JOIN Examination as e ON m.Code_medecin = e.Code_medecin WHERE Code_patient= '{code_patient}'" 
        self.__executeur.execute(la_requette)       
        return self.__executeur.fetchall()                 

    def recuper_rendez_vous (self, code_patient):
        la_requette= f"SELECT Nom, Date, Heure, Raison FROM Medecin AS m INNER JOIN Rendez_vous as r ON m.Code_medecin = r.Code_medecin WHERE Code_patient= '{code_patient}'" 
        self.__executeur.execute(la_requette)       
        return self.__executeur.fetchall()                                  

    def recuper_agenda (self, code_medecin):
        la_requette= f"SELECT Date, Heure, p.Code_patient, Nom, Prenom FROM Patient AS p INNER JOIN Rendez_vous as r ON p.Code_patient = r.Code_patient WHERE Code_medecin= '{code_medecin}'" 
        self.__executeur.execute(la_requette)       
        return self.__executeur.fetchall()     

    def __str_elt_condition(self, tab_elt_valeur, nb_elt):
            elt= tab_elt_valeur[0]
            str_elt_egale_valeur= f"{elt[0]}= '{elt[1]}'"
            for i in range(1, nb_elt):
                elt= tab_elt_valeur[i]
                str_elt_egale_valeur+= " AND "+f"{elt[0]}= '{elt[1]}'" 
            return str_elt_egale_valeur   

    def __str_elt_changer(self, tab_elt_valeur, nb_elt):
            elt= tab_elt_valeur[0]
            str_elt_egale_valeur= f"{elt[0]}= '{elt[1]}'"
            for i in range(1, nb_elt):
                elt= tab_elt_valeur[i]
                str_elt_egale_valeur+= " , "+f"{elt[0]}= '{elt[1]}'" 
            return str_elt_egale_valeur                                         

    def recuper_donner_table_selon_condition(self, Nom_table, tab_elt_contrainte=[]) :#le tableau de contrainte est une liste de liste contenant 2 elt l'attribut et la valeur de condition
        la_requette= f"SELECT * FROM {Nom_table}"
        nb_elt= len(tab_elt_contrainte)
        if(nb_elt!= 0):
            la_requette += f" WHERE {self.__str_elt_condition(tab_elt_contrainte, nb_elt)} "
        self.__executeur.execute(la_requette)       
        return self.__executeur.fetchall()    

    def supprimer_donner_table_selon_condition(self,  Nom_table, tab_elt_contrainte=[]):
        try:
           la_requette= f"DELETE FROM {Nom_table}" 
           nb_elt= len(tab_elt_contrainte)
           if(nb_elt!= 0):
                la_requette += f" WHERE {self.__str_elt_condition(tab_elt_contrainte, nb_elt)}"
           self.__executeur.execute(la_requette)  
           self.__la_base.commit()      
        except:
            pass    

    def modification(self, Nom_table, tab_elt_changer, tab_elt_condition):
        nb_elt_changer= len(tab_elt_changer)
        if(nb_elt_changer == 0):
            return False    
        la_requette= f"UPDATE {Nom_table} SET {self.__str_elt_changer(tab_elt_changer, nb_elt_changer)}" 
        nb_elt_condition= len(tab_elt_condition)
        if(nb_elt_condition > 0):
            la_requette += f" WHERE {self.__str_elt_condition(tab_elt_condition, nb_elt_condition)}"   
            self.__executeur.execute(la_requette)  
            self.__la_base.commit()      
            return True
    
    def modifier_patient(self, tab_elt):
          tab =["Nom", "Prenom", "Sexe", "Date_naissance", "Telephone", "Adresse", "Proffession", "Date_inscription"]   
          tab_echange= []
          nb_echange= len(tab)
          for i in range(nb_echange):
            tab_echange.append([tab[i], tab_elt[i+1]]) 
          tab_condition= [["Code_patient", tab_elt[0]] ]
          return self.modification("Patient", tab_echange, tab_condition)
            