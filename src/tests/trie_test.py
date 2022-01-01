import unittest
import string
from trie import TrieNode
import konfiguraatio

class TestTrie(unittest.TestCase):
    """TrieNoden perustestaus. Rakennetta testataan enemmän markov_test yhteydessä.
    """
    def setUp(self):
        self.konf = konfiguraatio.Konfiguraatio()
        self.konf.aste = 2
        self.juuri = TrieNode("")
        self.rivi = "tämä on testi lause".lower()\
            .translate(str.maketrans('', '', string.punctuation)).split()
        self.rivi2 = "tämä on toinen testilause".lower()\
            .translate(str.maketrans('', '', string.punctuation)).split()
        def lisaa(rivi, tiedosto):
            for i in range(len(self.rivi)-(self.konf.aste+1)):
                j = self.konf.aste
                while j >= 0:
                    temp = []
                    temp.append(self.rivi[int(i):int(i)+j])
                    temp.append(self.rivi[int(i)+j])
                    self.juuri.lisaa(temp, tiedosto)
                    j -= 1
        lisaa(self.rivi,"tiedosto1")
        lisaa(self.rivi2, "tiedosto2")

    def test_lisaa(self):
        """Testataan, tallentuvatko lauseet rakenteeseen
        """
        self.assertTrue("tämä" in self.juuri.seuraavat_sanat)

    def test_anna_sana(self):
        """testaa, antaako rakenne oikean sanan seuraavaksi
        """
        self.assertEqual("testi", self.juuri.anna_sana("tämä on".split()))

    def test_tyhja_syote(self):
        """testaa toiminnan tyhjällä syötteellä
        """
        sana = self.juuri.anna_sana("")
        self.assertTrue(sana in self.rivi or sana in self.rivi2)

    def test_yhdesta_tiedostosta(self):
        """testaa, että sanoja tulee vain yhdestä tiedostosta pyydettäessä
        """
        for _ in range(10):
            self.assertTrue(self.juuri.anna_sana("", "tiedosto2") in self.rivi2)

    def molemmista_tiedostoista(self):
        """testaa, että sanoja tulee tarvittaessa molemmista
        """
        tiedosto1 = 0
        tiedosto2 = 0
        for _ in range(1000):
            if self.juuri.anna_sana("") in self.rivi2:
                tiedosto2 += 1
            else:
                tiedosto1 += 1
        self.assertTrue(tiedosto2 != 0 and tiedosto1 != 0)
