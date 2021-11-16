import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_on_oikein(self):
        kortti = Maksukortti(100)
        kortin_saldo = kortti.saldo 
        self.assertEqual(kortin_saldo, 100)

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        kortti = Maksukortti(100)
        kortti.lataa_rahaa(10)
        kortin_saldo = kortti.saldo
        self.assertEqual(kortin_saldo, 110)

    def test_rahan_ottaminen_toimii(self):
        kortti = Maksukortti(100)
        kortti.ota_rahaa(10)
        kortin_saldo = kortti.saldo
        self.assertEqual(kortin_saldo, 90)

        kortti2 = Maksukortti(100)
        kortti2.ota_rahaa(110)
        kortin_saldo = kortti2.saldo
        self.assertEqual(kortin_saldo, 100)
    
    def test_tulostus_toimii(self):
        kortti = Maksukortti(100)
        kortti.ota_rahaa(10)
        tulostus = str(kortti)
        self.assertEqual(tulostus, "saldo: 0.9")

    
