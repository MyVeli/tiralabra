"""Sisältää konfiguraatioarvot
"""

from enum import Enum

mode_enum = Enum('Mode', 'DICT TRIE TEST')
#Käytetään mainissa valitsemaan mitä tietorakennetta käytetään
MODE = mode_enum.TRIE
#Testihakujen määrä jos test mode valittuna
HAKUJA = 100000
#Ketjun aste. Vaikuttaa vain Trie rakenteeseen
ASTE = 3
#Muodostettavan lauseen maksimipituus
MAX_PITUUS = 30
