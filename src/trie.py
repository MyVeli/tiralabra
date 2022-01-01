"""Toteuttaa Trie rakenteen käyttämällä SanaRakenne-luokkaa yhteyksiä varten
"""
from random import randint
from sanarakenne import SanaRakenne

class TrieNode:
    """Yksittäinen node rakenteessa
    """
    def __init__(self, sanat=None, alkupera=None):
        self.seuraavat_sanat = {}
        self.yhteydet = {}
        self.yhteydet_koko = 0
        if sanat:
            self.lisaa(sanat, alkupera)

    def lisaa(self, sanat, alkupera = None):
        """Lisää uuden sanaryhmän rakenteeseen ja luo yhteydet sanojen väleille

        Args:
            sanat (stringejä sisältävä taulukko): sisältää peräkkäisiä sanoja taulukossa
        """
        if len(sanat[0]) == 0:
            self.__lisaa_yhteys(sanat[1], alkupera)
            return
        sana = sanat[0][0]
        sanat[0] = sanat[0][1:]
        if sana in self.seuraavat_sanat:
            self.seuraavat_sanat[sana].lisaa(sanat, alkupera)
        else:
            self.seuraavat_sanat[sana] = TrieNode(sanat, alkupera)

    def __lisaa_yhteys(self, lisattava, alkupera):
        """lisää yhteyden sanojen välille käytämällä SanaRakenne-luokan toiminnallisuutta

        Args:
            lisattava (string): lisättävä sana
        """
        self.yhteydet_koko += 1
        if alkupera not in self.yhteydet:
            self.yhteydet[alkupera] = SanaRakenne(lisattava)
        else:
            self.yhteydet[alkupera].lisaa_sana(lisattava)

    def anna_sana(self, haku, alkupera='Any'):
        """Etsii parametrina annetulle sanalle tai lauseelle seuraavan sanan Trie-rakenteesta
        ja käyttämällä SanaRakenne-luokkaa seuraavan sanan valitsemiseen

        Args:
            haku (string): sana, tai lause, josta seuraava sana etsitään

        Returns:
            string: seuraava sana
        """
        if not haku:
            if alkupera == 'Any':
                satunnainen_tiedosto = randint(0, self.yhteydet_koko)
                for i in self.yhteydet.values():
                    satunnainen_tiedosto -= i.koko
                    if satunnainen_tiedosto <= 0:
                        return i.anna_sana()
            else:
                return self.yhteydet[alkupera].anna_sana()
        return self.seuraavat_sanat[haku[0]].anna_sana(haku[1:], alkupera)
