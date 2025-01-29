from RestaurantManagementAPP.Restaurant.repository.dataRepo import DataRepo
from RestaurantManagementAPP.Restaurant.modelle.bestellung import Bestellung
from json import JSONEncoder
import json
class customEncoder(JSONEncoder):
    def default(self, obj):
        return {
            "_id": obj.get_id(),
            "kunden_id": obj.kunden_id,
            "gerichte_ids": obj.gerichte_ids,
            "getranke_ids": obj.getranke_ids,
        }
def customDecoder(obj):
    try:
        if "_id" in obj and "kunden_id" in obj and "gerichte_ids" in obj and "getranke_ids" in obj:
            return Bestellung(int(obj["_id"]), [obj["kunden_id"]], [obj["gerichte_ids"]], [obj["getranke_ids"]])
    except KeyError:
        return obj

class BestellungRepo(DataRepo):
    def __init__(self, file):
        super().__init__(file)
    def save_data(self, data):
        # super().save_data(data)
        file = open("bestellungRepo.json", 'a')
        file.write(json.dumps(data, cls=customEncoder))
        file.close()

    def load_data(self):
        file = open("bestellungRepo.json", 'r')
        data = file.read()
        data = json.loads(data, object_hook=customDecoder)
        return data
    def read_data(self):
        # super().read_data()
        file = open("bestellungRepo.json", 'r')
        data = file.read()
        data = json.loads(data, object_hook=customDecoder)
        return data
    def write_data(self, data):
        # super().write_data(data)
        file = open("bestellungRepo.json", 'w')
        file.write(json.dumps(data, cls=customEncoder))
        file.close()

    def convert_to_string(self, _id):
        file = open("bestellungRepo.json", 'r')
        data = file.read()
        data = json.loads(data, object_hook=customDecoder)
        for bestellung in data:
            if bestellung.get_id() == _id:
                return bestellung