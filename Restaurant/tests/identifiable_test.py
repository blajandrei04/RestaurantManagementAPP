import unittest
from RestaurantManagementAPP.Restaurant.modelle.identifiable import Identifiable

class IdentifiableTest(unittest.TestCase):
    def setUp(self):
        self.identifiable = Identifiable(1)

    def test_get_id(self):
        self.assertEqual(self.identifiable.get_id(), 1)

    def test_set_id(self):
        self.identifiable.set_id(2)
        self.assertEqual(self.identifiable.get_id(), 2)