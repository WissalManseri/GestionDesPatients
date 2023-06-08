from front_end.petite_fenetre.generateur_petite_fen import generateur_petite_fen
from front_end.livre_page.page import Page, tk
from front_end.gestionaire_graphisme.gestionaire_page.fonction_creation_elt_dans_feuille import fonction_creation_elt_page


class generateur_petite_fen_info (generateur_petite_fen):
      def __init__(self, fen) -> None:
            super().__init__(fen)

      def fermer(self):
            self._top.destroy()      

      def creation_fen(self, larg, haut, x, y, titre, tab_nom_bout, police_1, couleur, couleur_ligne):
         super()._cree_une_petite_fentre(x, y, larg, haut)
         self._page_globale.change_largeur_scroll(0)
         ecart_bas= 20
         haut -= ecart_bas
         haut_lab= 30
         ecart= 10
         haut_page= haut- 2*haut_lab- 2* ecart
         feuille= self._page_globale.get_feuile()
         x_decale_page= 20
         larg_page= larg- 2*x_decale_page
         #-----------------------------------
         lab_titre= tk.Label(feuille, width=larg, height= haut_lab, text= titre, font= police_1, background= "white")
         page_info= Page(feuille, larg_page, haut_page, couleur)
         x=0
         y=0
         #--------------------------------------
         id_cadre= feuille.create_window(x, y, width= larg, height= haut_lab, window= lab_titre, anchor="nw")
         y= feuille.bbox(id_cadre)[3]+ ecart
         x += x_decale_page
         id_cadre= feuille.create_window(x, y, width= larg_page, height= haut_page, window= page_info.get_support(), anchor="nw")
         page_info.change_largeur_scroll(7)
         page_info.get_support().configure(bd= 1, background= couleur_ligne)
         #------------------------------------------- 
         espace_entre_bout= 10
         nb_bout= len(tab_nom_bout)
         larg_bout= int(larg_page/nb_bout- espace_entre_bout)
         y= feuille.bbox(id_cadre)[3]+ ecart
         tab_bout= []
         for elt in tab_nom_bout:
            bout= fonction_creation_elt_page.cree_bouton(feuille, x, y, larg_bout, haut_lab, [elt], couleur_ligne, elt, police_1, couleur) 
            tab_bout.append(bout)
            x = feuille.bbox(elt)[2]+ espace_entre_bout
         return page_info, tab_bout     
         
