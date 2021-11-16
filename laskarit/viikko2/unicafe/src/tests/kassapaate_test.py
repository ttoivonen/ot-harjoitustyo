import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
        
    def setUp(self):
        print("Tässä on setuppi")

    def test_oikea_lounaiden_maara(self):
        kassa = Kassapaate()
        self.assertEqual(kassa.maukkaat, 0)
        self.assertEqual(kassa.edulliset, 0)
        self.assertEqual(kassa.kassassa_rahaa, 100000)
    
    def test_edulliset_kateisosto_toimii(self):
        kassa = Kassapaate()
        kassa.syo_edullisesti_kateisella(250)
        self.assertEqual(kassa.kassassa_rahaa, 100000+240)
        self.assertEqual(kassa.edulliset, 1)

    def test_edulliset_kateisosto_liian_vahan(self):
        kassa = Kassapaate()
        kassa.syo_edullisesti_kateisella(239)
        self.assertEqual(kassa.kassassa_rahaa, 100000)
        self.assertEqual(kassa.edulliset, 0)

    def test_maukkaat_kateisosto_toimii(self):
        kassa = Kassapaate()
        kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual(kassa.kassassa_rahaa, 100000+400)
        self.assertEqual(kassa.maukkaat, 1)

    def test_maukkaat_kateisosto_liian_vahan(self):
        kassa = Kassapaate()
        kassa.syo_maukkaasti_kateisella(399)
        self.assertEqual(kassa.kassassa_rahaa, 100000)
        self.assertEqual(kassa.maukkaat, 0)

 #korttiostot
    def test_edulliset_korttiosto_toimii(self):
        kortti = Maksukortti(1000)
        kassa = Kassapaate()
        kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kassa.edulliset, 1)

   
    def test_edulliset_korttiosto_liian_vahan(self):
        kortti = Maksukortti(239)
        kassa = Kassapaate()
        kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kassa.edulliset, 0)  

    def test_maukkaat_korttiosto_toimii(self):
        kortti = Maksukortti(1000)
        kassa = Kassapaate()
        kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kassa.maukkaat, 1)
   
    def test_maukkaat_korttiosto_liian_vahan(self):
        kortti = Maksukortti(399)
        kassa = Kassapaate()
        kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kassa.maukkaat, 0)  

# tuli keskiyö ja deadline :)