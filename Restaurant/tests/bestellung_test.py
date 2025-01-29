import unittest
from RestaurantManagementAPP.Restaurant.modelle.bestellung import Bestellung
class BestellungTest(unittest.TestCase):
    def setUp(self):
        self.bestellung = Bestellung(1, 1, [1], [1])
    def test_get_id(self):
        self.assertEqual(self.bestellung.get_id(), 1)
    # def test_berechne_kosten(self):
    #     # self.bestellung.berechne_kosten()
    #     self.assertEqual(self.bestellung.gesamtkosten, 2)
    # def test_erzeuge_rechnung_string(self):
    #     self.assertEqual(self.bestellung._erzeuge_rechnung_string(), "1\n1")
    def test_zeige_rechnung(self):
        self.bestellung.zeige_rechnung()