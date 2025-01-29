import unittest
from RestaurantManagementAPP.Restaurant.modelle.getranke import Getranke

class GetrankeTest(unittest.TestCase):
    def setUp(self):
        self.getranke = Getranke(1, 1, 1, 1)

    def test_get_id(self):
        self.assertEqual(self.getranke.get_id(), 1)

    def test_get_portionGrosse(self):
        self.assertEqual(self.getranke.get_portionGrosse(), 1)

    def test_get_preis(self):
        self.assertEqual(self.getranke.get_preiss(), 1)

    def test_get_alkoholgehalt(self):
        self.assertEqual(self.getranke.get_alkoholgehalt(), 1)