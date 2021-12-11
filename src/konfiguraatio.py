"""Sisältää konfiguraatioarvot
"""

from enum import Enum

mode_enum = Enum('Mode', 'DICT TRIE TEST TEXT')
#Käytetään mainissa valitsemaan mitä tietorakennetta käytetään
MODE = mode_enum.TEXT
#Testihakujen määrä jos test mode valittuna
HAKUJA = 100000
#Ketjun aste. Vaikuttaa vain Trie rakenteeseen
ASTE = 2
#Muodostettavan lauseen maksimipituus
MAX_PITUUS = 100
