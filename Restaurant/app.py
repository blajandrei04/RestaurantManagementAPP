import jsonpickle

from RestaurantManagementAPP.Restaurant.ui.uI import UI
from RestaurantManagementAPP.Restaurant.tests.bestellung_test import BestellungTest
from RestaurantManagementAPP.Restaurant.repository.gekochterGerichtRepo import GekochterGerichtRepo
from RestaurantManagementAPP.Restaurant.modelle.gekochtergericht import GekochterGericht
from RestaurantManagementAPP.Restaurant.repository.gekochterGerichtRepo import GekochterGerichtRepo
from RestaurantManagementAPP.Restaurant.modelle.gericht import Gericht
from RestaurantManagementAPP.Restaurant.repository.kundenRepo import KundenRepo
from RestaurantManagementAPP.Restaurant.modelle.kunde import Kunde
from RestaurantManagementAPP.Restaurant.repository.bestellungRepo import BestellungRepo
from RestaurantManagementAPP.Restaurant.modelle.bestellung import Bestellung
import unittest
if __name__ == "__main__":
    unittest.main(exit=False)
    ui = UI()
    ui.print_menu()
    ui.menu(int(input("Option: ")))
