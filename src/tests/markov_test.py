import unittest
from unittest.mock import patch
from markov import luo_lause, luo_lause_trie
from tiedostonkasittely import load_data_dict, load_data_trie

class TestMarkov(unittest.TestCase):
    def setUp(self):
        self.data_dict = load_data_dict()
        self.data_trie = load_data_trie()

    def test_yksi_sana_dict(self):
        try:
            sana = luo_lause(self.data_dict, "sana")
            self.assertEqual(isinstance(sana, str))
        except:
            self.assertFalse

    def test_yksi_sana_trie(self):
        try:
            sana = luo_lause_trie(self.data_trie, "sana")
            self.assertEqual(isinstance(sana, str))
        except:
            self.assertFalse

    def test_monta_sanaa_dict(self):
        try:
            sana = luo_lause(self.data_dict, "monen sanan lause")
            self.assertEqual(isinstance(sana, str))
        except:
            self.assertFalse

    def test_monta_sanaa_trie(self):
        try:
            sana = luo_lause_trie(self.data_trie, "sana")
            self.assertEqual(isinstance(sana, str))
        except:
            self.assertFalse
