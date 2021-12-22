import unittest

import konfiguraatio
from tiedostonkasittely import load_data_dict, load_data_trie_telegram

class TestTiedostonKasittely(unittest.TestCase):

    def setUp(self):
        self.konf = konfiguraatio.Konfiguraatio()

    def test_avaaminen_dict(self):
        try:
            data = load_data_dict()
        except:
            self.assertFalse
        if not data:
            self.assertFalse

    def test_avaaminen_trie(self):
        try:
            juuri = load_data_trie_telegram(self.konf)
        except:
            self.assertFalse
        if not juuri:
            self.assertFalse
