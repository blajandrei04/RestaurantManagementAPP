from RestaurantManagementAPP.Restaurant.modelle.identifiable import Identifiable
import json
from collections import namedtuple
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Identifiable):
            return o.to_json()
        return super().default(o)

class Kunde(Identifiable):
    def __init__(self, _id, name, adresse):
        super().__init__(_id)
        self.__name = name
        self.__adresse = adresse

    def toJson(self):
        return json.dumps(self, indent = 3 , default=lambda o: o.__dict__,)


    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_adresse(self):
        return self.__adresse

    def set_adresse(self, new_adresse):
        self.__adresse = new_adresse

    def __str__(self):
        return f"ID: {self.get_id()}\nName: {self.get_name()}\nAdresse: {self.get_adresse()}"

    def __repr__(self):
        return f"ID: {self.get_id()}\nName: {self.get_name()}\nAdresse: {self.get_adresse()}"