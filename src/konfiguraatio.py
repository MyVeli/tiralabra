"""Sisältää konfiguraatioarvot
"""

from enum import Enum

mode_enum = Enum('Mode', 'DICT TRIE TEST TEXT MOLEMMAT')

class Konfiguraatio:
    def __init__(self):        
        #Käytetään mainissa valitsemaan mitä tietorakennetta käytetään
        self.mode = mode_enum.MOLEMMAT
        #Testihakujen määrä jos test mode valittuna
        self.hakuja = 100000
        #Ketjun aste. Vaikuttaa vain Trie rakenteeseen
        self.aste = 2
        #Muodostettavan lauseen maksimipituus
        self.max_pituus = 20
