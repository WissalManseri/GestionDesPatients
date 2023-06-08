class gestion_controle_entrer :
    __tab_indice_date_patient= [4, 8]
    __tab_indice_numero_patient= [5]
    #prend une chaine de caractere et retourne un booleen et une autre chaine qui contient une cahaine de caractere contenant la date correctement former .si le booleen est vraie c'est que nous avons reusit a contruire grace a la chaine resu si non nous retournons false et une chaine null
    def __controle_date(mot :str):
        tab= mot.split("/")
        retour_default_1 = False
        retour_default_2 = ""
        if(len(tab) != 3):
            return retour_default_1, retour_default_2 
        try:
            jour= int(tab[0].strip())
            if((jour <= 0) or (jour >= 32)):
                return retour_default_1, retour_default_2
            mois= int(tab[1].strip())
            if((mois <= 0) or (mois >= 13)):
                return retour_default_1, retour_default_2
            anne= int(tab[2].strip())
            if(mois % 2 == 0):
               if(jour > 30):
                 return retour_default_1, retour_default_2
               if( mois == 2):
                    if((anne % 4 != 0) and (jour > 28)):
                        return retour_default_1, retour_default_2
            s_jour=  f"0{jour}" if(jour < 10) else str(jour)
            s_mois=  f"0{mois}" if(mois < 10) else str(mois)  
            return True, f"{s_jour}/{s_mois}/{anne}"       
        except:
            return retour_default_1, retour_default_2    

    def __controle_heure(mot : str):
        retour_default_1 = False
        retour_default_2 = ""
        try:
            heure= int(mot)
            if((heure < 0) or (heure > 23)):
                return retour_default_1, retour_default_2
            return  True, f"{heure}H" 
        except :   
            return retour_default_1, retour_default_2 

    def __controle_telephone(mot: str):
        try:
            s= ""
            for elt in mot:
                if(elt != " "):
                    s += f"{int(elt)}"
            return True, s        
        except:
            return False, ""             

    #prend les donnees du patient retouche ceux nescessaires et retourne deux tableaux un pour les indice des donnees errounees et l'autre pour les donnees retouchees
    def controle_donnee_patient(tab_donne):
        tab_indice_incorecte= []
        nb_donnee= len(tab_donne)
        for i in range(nb_donnee):
            valeur= tab_donne[i]
            if(valeur == ""):
                tab_indice_incorecte.append(i)
            else:
                if(gestion_controle_entrer.__tab_indice_date_patient.__contains__(i)) :
                    reponse, date_retorucher =gestion_controle_entrer.__controle_date(valeur)
                    if(reponse):
                        tab_donne[i]= date_retorucher  
                    else:
                        tab_indice_incorecte.append(i)  
                else: 
                    if(gestion_controle_entrer.__tab_indice_numero_patient.__contains__(i)):
                        reponse, num_retoucher= gestion_controle_entrer.__controle_telephone(valeur)
                        if(reponse):
                            tab_donne[i]= num_retoucher
                        else:
                            tab_indice_incorecte.append(i)
        return tab_indice_incorecte, tab_donne

    def controle_donnee_examination_rendez_vous(tab_donne, exam= True):
        borne= 3
        if(not exam):
           borne= 2
        dbut= 2
        tab_indice_incorecte= []
        reponce, date_retoucher= gestion_controle_entrer.__controle_date(tab_donne[dbut])
        if(reponce):
            tab_donne[dbut]= date_retoucher
        else:
            tab_indice_incorecte.append(0)
        for i in range(dbut+1, dbut+borne):
            reponce, heure_retoucher= gestion_controle_entrer.__controle_heure(tab_donne[i])
            if(reponce):
                tab_donne[i]= heure_retoucher 
            else: 
                tab_indice_incorecte.append(i - dbut)
        if(tab_donne[borne + dbut] == ""):
            tab_indice_incorecte.append(borne)
        return tab_indice_incorecte, tab_donne                                                       
        