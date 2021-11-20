import unittest
from tiedostonkasittely import load_data_dict, load_data_trie, avaa_tiedosto

class TestTiedostonKasittely(unittest.TestCase):
    def test_avaaminen_dict(self):
        try:
            data = load_data_dict()
        except:
            self.assertFalse
        if not data:
            self.assertFalse

    def test_avaaminen_trie(self):
        try:
            juuri = load_data_trie()
        except:
            self.assertFalse
        if not juuri:
            self.assertFalse

    def test_avaa_tiedosto(self):
        try:
            file = avaa_tiedosto()
        except:
            self.assertFalse
        if not file:
            self.assertFalse
