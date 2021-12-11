"""Toteuttaa Trie rakenteen käyttämällä SanaRakenne-luokkaa yhteyksiä varten
"""
from sanarakenne import SanaRakenne

class TrieNode:
    """Yksittäinen node rakenteessa
    """
    def __init__(self, sanat):
        self.seuraavat_sanat = {}
        self.yhteydet = None
        if sanat:
            self.lisaa(sanat)

    def lisaa(self, sanat):
        """Lisää uuden sanaryhmän rakenteeseen ja luo yhteydet sanojen väleille

        Args:
            sanat (stringejä sisältävä taulukko): sisältää peräkkäisiä sanoja taulukossa
        """
        if not sanat:
            return
        """if len(sanat[0]) == 0 and len(sanat) == 1:
            #self.lisaa_yhteys(".")
            return"""
        if len(sanat[0]) == 0:
            self.__lisaa_yhteys(sanat[1])
            return
        #sanat = sanat[1:]
        sana = sanat[0][0]
        sanat[0] = sanat[0][1:]
        if sana in self.seuraavat_sanat:
            self.seuraavat_sanat[sana].lisaa(sanat)
        else:
            self.seuraavat_sanat[sana] = TrieNode(sanat)

    def __lisaa_yhteys(self, lisattava):
        """lisää yhteyden sanojen välille käytämällä SanaRakenne-luokan toiminnallisuutta

        Args:
            lisattava (string): lisättävä sana
        """
        if self.yhteydet is None:
            self.yhteydet = SanaRakenne(lisattava)
        else:
            self.yhteydet.lisaa_sana(lisattava)

    def anna_sana(self, haku):
        """Etsii parametrina annetulle sanalle tai lauseelle seuraavan sanan Trie-rakenteesta
        ja käyttämällä SanaRakenne-luokkaa seuraavan sanan valitsemiseen

        Args:
            haku (string): sana, tai lause, josta seuraava sana etsitään

        Returns:
            string: seuraava sana
        """
        if not haku:
            return self.yhteydet.anna_sana()
        return self.seuraavat_sanat[haku[0]].anna_sana(haku[1:])
