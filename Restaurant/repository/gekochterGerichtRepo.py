from RestaurantManagementAPP.Restaurant.repository.dataRepo import DataRepo
from abc import ABC, abstractmethod
from json import JSONEncoder
import json
from RestaurantManagementAPP.Restaurant.modelle.gekochtergericht import GekochterGericht
class GekochterGerichtRepo(DataRepo):
    def __init__(self, file):
        super().__init__(file)
    def search_gericht(self, _id):
        data = self.read_data()
        for gericht in data:
            if gericht.get_id() == _id:
                return gericht
    def save_data(self, data):
        # super().save_data(data)
        file = open("gekochterGerichtRepo.json", 'a')
        file.write(json.dumps(data, cls=customEncoder))
        file.close()

    def load_data(self):
        file = open("gekochterGerichtRepo.json", 'r')
        data = file.read()
        data = json.loads(data, object_hook=customDecoder)
        return data
    def read_data(self):
        # super().read_data()
        file = open("gekochterGerichtRepo.json", 'r')
        data = file.read()
        data = json.loads(data, object_hook=customDecoder)
        return data
    def write_data(self, data):
        # super().write_data(data)
        file = open("gekochterGerichtRepo.json", 'w')
        file.write(json.dumps(data, cls=customEncoder))
        file.close()

def customDecoder(obj):
    try:
        if "_id" in obj and "_portionGrosse" in obj and "_preiss" in obj and "_zubereitungszeit" in obj:
            return GekochterGericht(obj["_id"], obj["_name"], obj["_preis"])
    except KeyError:
        return obj
class customEncoder(JSONEncoder):
    def default(self, obj):
        return {
            "_id": obj.get_id(),
            "_portionGrosse": obj.get_portiongrosse(),
            "_preiss": obj.get_preiss(),
            # "_zubereitungszeit": obj.get_zubereitungszeit()
        }
