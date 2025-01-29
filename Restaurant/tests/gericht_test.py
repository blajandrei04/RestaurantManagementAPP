import unittest
from RestaurantManagementAPP.Restaurant.modelle.gericht import Gericht

class GerichtTest(unittest.TestCase):
    def setUp(self):
        self.gericht = Gericht(1, 1, 1)

    def test_get_id(self):
        self.assertEqual(self.gericht.get_id(), 1)

    def test_get_portionGrosse(self):
        self.assertEqual(self.gericht.get_portionGrosse(), 1)

    def test_get_preis(self):
        self.assertEqual(self.gericht.get_preis(), 1)