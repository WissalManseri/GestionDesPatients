class Medecin:
    def __init__(self, tab_info_texte) -> None:
        self.__tab_infon_texte= tab_info_texte

    def get_code(self):
        return self.__tab_infon_texte[0]
    
    def get_nom(self):
        return self.__tab_infon_texte[1]
