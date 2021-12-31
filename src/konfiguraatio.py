"""Sisältää konfiguraatioarvot
"""

from enum import Enum

# luokan käyttämä tietotyyppi
mode_enum = Enum('Mode', 'DICT TELEGRAM TEXT MOLEMMAT')

class Konfiguraatio:
    """Konfiguraatio-luokka, joka sisältää ohjelman asetukset
    """
    def __init__(self):
        #Käytetään valitsemaan mitä tietorakennetta käytetään ja mitkä tiedostot ladataan
        self.mode = mode_enum.TELEGRAM
        #Testihakujen määrä jos test mode valittuna
        self.hakuja = 100000
        #Ketjun aste. Vaikuttaa vain Trie rakenteeseen
        self.aste = 3
        #Muodostettavan lauseen maksimipituus
        self.max_pituus = 10
