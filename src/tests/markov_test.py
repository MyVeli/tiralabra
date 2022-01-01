import unittest
import string
from unittest.mock import patch

import konfiguraatio
from trie import TrieNode
from markov import luo_lause_dict, luo_lause_trie
from tiedostonkasittely import load_data_dict, load_data_trie_telegram

class TestMarkov(unittest.TestCase):
    def setUp(self):
        """Valmistellaan data setupissa testejä varten"""
        self.konf = konfiguraatio.Konfiguraatio()
        self.konf.aste = 1
        self.data_trie = TrieNode("")
        self.rivi = "tämä on testi lause. myös, monen sanan testi".lower()\
            .translate(str.maketrans('', '', string.punctuation)).split()
        for i in range(len(self.rivi)-(self.konf.aste+1)):
            j = self.konf.aste
            while j >= 0:
                temp = []
                temp.append(self.rivi[int(i):int(i)+j])
                temp.append(self.rivi[int(i)+j])
                self.data_trie.lisaa(temp, "tiedosto")
                j -= 1
        self.data_dict = load_data_dict()

    def test_yksi_sana_dict(self):
        """testaa, että luo_lause_dict palauttaa merkkijonon oikealla syötteellä
        """
        sana = luo_lause_dict(self.data_dict, "sana".split(), self.konf)
        self.assertTrue(isinstance(sana, str))

    def test_yksi_sana_trie(self):
        """testaa, että luo_lause_trie palauttaa merkkijonon oikealla syötteellä
        """
        sana = luo_lause_trie(self.data_trie, "sana".split(), self.konf)
        self.assertTrue(isinstance(sana, str))

    def test_monta_sanaa_dict(self):
        """testaa, että luo_lause_dict palauttaa merkkijonon oikealla syötteellä, jossa on monta sanaa
        """
        sana = luo_lause_dict(self.data_dict, "monen sanan lause".split(), self.konf)
        self.assertTrue(isinstance(sana, str))

    def test_monta_sanaa_trie(self):
        """testaa, että luo_lause_trie palauttaa merkkijonon oikealla syötteellä, jossa on monta sanaa
        """
        sana = luo_lause_trie(self.data_trie, "sana".split(), self.konf)
        self.assertTrue(isinstance(sana, str))

    def test_syotetta_ei_rakenteessa_dict(self):
        """testaa luo_lause_dict toiminnan tilanteessa, jossa sanaa ei ole rakenteessa
        """
        self.konf.max_pituus = 10
        sana = luo_lause_dict(self.data_dict, "notindata".split(), self.konf)
        self.assertEqual(sana, "notindata")

    def test_syotetta_ei_rakenteessa_trie(self):
        """testaa luo_lause_trie toiminnan tilanteessa, jossa sanaa ei ole rakenteessa
        """
        self.konf.max_pituus = 10
        sana = luo_lause_trie(self.data_trie, "notindata".split(), self.konf)
        self.assertEqual(sana, "notindata")

    def test_tyhja_syote_trie(self):
        """testaa luo_lause_trie toiminnan ilman aloittavaa sanaa
        """
        self.konf.max_pituus = 1
        sana = luo_lause_trie(self.data_trie, "".split(), self.konf)
        self.assertTrue(sana in self.rivi)

    def test_tyhja_syote_dict(self):
        """testaa luo_lause_dict toiminnan ilman aloittavaa sanaa
        """
        sana = luo_lause_dict(self.data_dict, "".split(), self.konf)
        self.assertTrue(" ", sana)

    def test_lause_tekstista_trie(self):
        """testaa luo_lause_trie toiminnan, kun aste on pienempi kuin max_pituus ja sanoja tulee useampia
        """
        self.konf.max_pituus = 2
        self.konf.aste = 1
        sanat = luo_lause_trie(self.data_trie, "".split(), self.konf).split()
        self.assertTrue(sanat[0] in self.rivi)
        self.assertTrue(sanat[1] in self.rivi)

    def test_yhdistelmat_oikeita(self):
        self.konf.max_pituus = 2
        self.konf.aste = 1
        for _ in range(10):
            sanat = luo_lause_trie(self.data_trie, "".split(), self.konf).split()   
            i = 0
            while i < len(self.rivi)-1:
                if self.rivi[i] == sanat[0]:
                    self.assertEqual(self.rivi[i+1],sanat[1])
                    break
                i += 1

    def test_vaara_rakenne_trie(self):
        """testaa trien toiminnan, kun parametrina annetaan vääränlainen data-rakenne
        """
        sana = luo_lause_trie(self.data_dict, "sana".split(), self.konf)
        self.assertEqual(sana, " ")

    def test_vaara_rakenne_dict(self):
        """testaa dictionaryn toiminnan, kun parametrina annetaan vääränlainen data-rakenne
        """
        sana = luo_lause_dict(self.data_trie, "sana".split(), self.konf)
        self.assertEqual(sana, " ")
