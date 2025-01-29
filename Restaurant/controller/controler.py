from RestaurantManagementAPP.Restaurant.modelle.identifiable import Identifiable
from RestaurantManagementAPP.Restaurant.modelle.bestellung import Bestellung
from RestaurantManagementAPP.Restaurant.modelle.kunde import Kunde
from RestaurantManagementAPP.Restaurant.modelle.getranke import Getranke
from RestaurantManagementAPP.Restaurant.modelle.gekochtergericht import GekochterGericht
from RestaurantManagementAPP.Restaurant.modelle.gericht import Gericht
from RestaurantManagementAPP.Restaurant.repository.dataRepo import DataRepo
from RestaurantManagementAPP.Restaurant.repository.bestellungRepo import BestellungRepo
from RestaurantManagementAPP.Restaurant.repository.kundenRepo import KundenRepo
from RestaurantManagementAPP.Restaurant.repository.getrankeRepo import GetrankeRepo
from RestaurantManagementAPP.Restaurant.repository.gekochterGerichtRepo import GekochterGerichtRepo

class Controller:
    def __init__(self, kundenRepo, getrankeRepo, gekochterGerichtRepo, bestellungRepo):
        self.kundenRepo = KundenRepo(kundenRepo)
        self.getrankeRepo = GetrankeRepo(getrankeRepo)
        self.gekochterGerichtRepo = GekochterGerichtRepo(gekochterGerichtRepo)
        self.bestellungRepo = BestellungRepo(bestellungRepo)
    def add_to_repo(self, obj):
        # if isinstance(obj, Kunde):
        #     self.kundenRepo.save_data(obj)
        # elif isinstance(obj, Getranke):
        #     self.getrankeRepo.save_data(obj)
        # elif isinstance(obj, GekochterGericht):
        #     self.gekochterGerichtRepo.save_data(obj)
        # elif isinstance(obj, Bestellung):
        #     self.bestellungRepo.json.save_data(obj)
        self.gekochterGerichtRepo.save_data(obj)
    def search_kunde_by_name(self, name):
        return self.kundenRepo.search_kunde_by_name(name)
    def search_kunde_by_adresse(self, adresse):
        return self.kundenRepo.search_kunde_by_adresse(adresse)
    def update_kunde_name(self, _id, name):
        self.kundenRepo.update_kunde(_id, name)

    def convert_to_string_rechnung(self, _id):
        return self.bestellungRepo.convert_to_string(_id)
    def save_bestellung(self, bestellung):
        self.bestellungRepo.save_data(bestellung)
    def read_bestellung_data(self):
        return self.bestellungRepo.read_data()
    def create_gericht(self, _id, portionGrosse, preiss):
        gericht = Gericht(_id, portionGrosse, preiss)
        return gericht
    def create_bestellung(self, _id, kunden_id=None, gerichte_ids=[], getranke_ids=[]):
        return Bestellung(_id, kunden_id, gerichte_ids, getranke_ids)