"""[summary]

Returns:
    [type]: [description]
"""

from sanarakenne import SanaRakenne

class TrieNode:
    """Yksittäinen node rakenteessa
    """
    def __init__(self, sanat):
        self.seuraavat_kirjaimet = {}
        self.yhteydet = None
        if sanat:
            self.lisaa(sanat)

    def lisaa(self, sanat):
        if not sanat:
            return
        if len(sanat[0]) == 0 and len(sanat) == 1:
            #self.lisaa_yhteys(".")
            return
        elif len(sanat[0]) == 0:
            self.lisaa_yhteys(sanat[1])
            sanat = sanat[1:]
        kirjain = sanat[0][0]
        sanat[0] = sanat[0][1:]
        if kirjain in self.seuraavat_kirjaimet:
            self.seuraavat_kirjaimet[kirjain].lisaa(sanat)
        else:
            self.seuraavat_kirjaimet[kirjain] = TrieNode(sanat)

    def lisaa_yhteys(self, lisattava):
        if self.yhteydet == None:
            self.yhteydet = SanaRakenne(lisattava)
        else:
            self.yhteydet.lisaa_sana(lisattava)

    def anna_sana(self, haku):
        if not haku:
            return self.yhteydet.anna_sana()
        return self.seuraavat_kirjaimet[haku[0]].anna_sana(haku[1:])

if __name__ == "__main__":
    lause = "tämä on testi lause"
    sanat = lause.split()
    juuri = TrieNode(sanat)
    print(juuri.anna_sana("".join("tämä on testi".split())))
