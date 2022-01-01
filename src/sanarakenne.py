"""Sisältää sanarakenne-luokan, jota käytetään sanayhteyksien ja esiintymismäärien tallentamiseen.
"""

from random import randint

class SanaRakenne:
    """Luokka, johon tallennetaan sanaa tai sanaparia seuraavat sanat, sekä niiden esiintymismäärät
    dictionarya käytettäessä.
    """
    def __init__(self, sana):
        self.sanat = {}
        self.sanat[sana] = 1
        self.koko = 1

    def lisaa_sana(self, sana):
        """Lisää sanan tai päivittää esiintymismäärää

        Args:
            sana (string): lisättävä sana
        """
        if sana in self.sanat:
            self.sanat[sana] += 1
        else:
            self.sanat[sana] = 1
        self.koko += 1

    def anna_sana(self):
        """Palauttaa satunnaisen seuraavan sanan ottaen esiintymismäärät huomioon"""
        luku = randint(0, self.koko)
        # Tyhjää rakennetta on mahdoton luoda, joten sana löytyy aina.
        for sana, maara in self.sanat.items():
            luku -= maara
            if luku <= 0:
                return sana
