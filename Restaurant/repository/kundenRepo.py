import json
from RestaurantManagementAPP.Restaurant.repository.dataRepo import DataRepo
from RestaurantManagementAPP.Restaurant.repository.utils import *

class KundenRepo(DataRepo):
    def __init__(self, file):
        super().__init__(file)

    def __repr__(self):
        data = self.load_data()
        str = ""
        for kunde in data:
            str += f"{kunde.get_name()}, {kunde.get_adresse()}, {kunde.get_id()} \n"
        return str
        # return f"{data.get_name()}"
    def save_data(self, data):
        super().save_data(data)

    def load_data(self):
        # super().load_data()
        #
        file = open("kundenRepo.json", 'r')
        data = file.read()
        data = json.loads(data, object_hook=customDecoder)
        return data
    def read_data(self):
        # super().read_data()
        file = open("kundenRepo.json", 'r')
        data = file.read()
        data = json.loads(data, object_hook=customDecoder)
        return data
    def write_data(self, data):
        super().write_data(data)
    def search_kunde_by_name(self, name):
        data = self.load_data()
        if data is None:
            return None
        for kunde in data:
            # print(kunde)
            if name.lower() in kunde.get_name().lower():
                return kunde
                # return f'{kunde["_Identifiable__id"]}, {kunde["_Kunde__name"]}, {kunde["_Kunde__adresse"]}'

    def search_kunde_by_adresse(self, adresse):
        data = self.load_data()
        if data is None:
            return None
        for kunde in data:
            if adresse.lower() in kunde.get_adresse().lower():
                return kunde

    def update_kunde(self, _id, new_name):
        data = self.load_data()
        for kunde in data:
            if kunde.get_id() == _id:
                kunde.set_name(new_name)
        self.write_data(data)