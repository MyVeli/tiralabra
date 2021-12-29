"""Sisältää konfiguraatioarvot
"""

from enum import Enum

# luokan käyttämä tietotyyppi
mode_enum = Enum('Mode', 'DICT TRIE TEXT MOLEMMAT')

class Konfiguraatio:
    """Konfiguraatio-luokka, joka sisältää ohjelman asetukset
    """
    def __init__(self):
        #Käytetään mainissa valitsemaan mitä tietorakennetta käytetään
        self.mode = mode_enum.TRIE
        #Testihakujen määrä jos test mode valittuna
        self.hakuja = 100000
        #Ketjun aste. Vaikuttaa vain Trie rakenteeseen
        self.aste = 2
        #Muodostettavan lauseen maksimipituus
        self.max_pituus = 10
