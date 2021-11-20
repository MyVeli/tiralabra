import unittest
from trie import TrieNode

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.juuri = TrieNode("tämä on testi lause".split())

    def test_lisaa(self):
        self.assertEqual(True,"t" in self.juuri.seuraavat_kirjaimet)

    def test_anna_sana(self):
        self.assertEqual("lause",self.juuri.anna_sana("tämäontesti"))
