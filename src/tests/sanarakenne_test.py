import unittest
import sys
sys.path.append('..')
from src.sanarakenne import SanaRakenne

class TestSanaRakenne(unittest.TestCase):
    def setUp(self):
        self.rakenne = SanaRakenne("sana")

    def test_hae_ainoa_sana(self):
        self.assertEqual(self.rakenne.anna_sana(),"sana")

    def test_lisaa_uusi(self):
        self.rakenne.lisaa_sana("toinen")
        self.assertEqual(self.rakenne.sanat["toinen"],1)

    def test_lisaa_olemassa_oleva(self):
        self.rakenne.lisaa_sana("sana")
        self.assertEqual(self.rakenne.sanat["sana"],2)

    def test_mahdollisuus(self):
        for i in range(9):
            self.rakenne.lisaa_sana("sana")
        for i in range(10):
            self.rakenne.lisaa_sana("toinen")
        sana = 0
        toinen = 0
        for i in range(100000):
            temp = self.rakenne.anna_sana()
            if temp == "sana":
                sana += 1
            elif temp == "toinen":
                toinen += 1
        suhde = abs(sana-toinen)/100000
        # Kohtalaisen lähellä on riittävä toiminnan varmistamiseen
        if suhde < 0.1:
            suhde = 0
        self.assertEqual(0, suhde)
