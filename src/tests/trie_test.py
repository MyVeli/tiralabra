import unittest
import string
from trie import TrieNode
import konfiguraatio

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.juuri = TrieNode("")
        rivi = "tämä on testi lause".lower()\
            .translate(str.maketrans('', '', string.punctuation)).split()
        for i in range(len(rivi)-(konfiguraatio.ASTE+1)):
            j = konfiguraatio.ASTE
            while j >= 0:
                temp = []
                temp.append(rivi[int(i):int(i)+j])
                temp.append(rivi[int(i)+j])
                self.juuri.lisaa(temp)
                j -= 1

    def test_lisaa(self):
        self.assertEqual(True,"tämä" in self.juuri.seuraavat_sanat)

    def test_anna_sana(self):
        self.assertEqual("testi",self.juuri.anna_sana("tämä on".split()))
