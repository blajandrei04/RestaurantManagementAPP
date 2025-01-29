from json import JSONEncoder
import json
from collections import namedtuple
from RestaurantManagementAPP.Restaurant.modelle.kunde import Kunde
# class MyEncoder(JSONEncoder):
        # def default(self, o):
        #     return o.__dict__
class MyEncoder(JSONEncoder):
    def default(self, o):
        return {
            "_id" : o.get_id(),
            "_name" : o.get_name(),
            "_adresse" : o.get_adresse()
        }

def customDecoder(obj):
    # return Kunde(**jsonDict)
    # return Kunde(jsonDict["_id"], jsonDict["_name"], jsonDict["_adresse"])
    try:
        if "_id" in obj and "_name" in obj and "_adresse" in obj:
            return Kunde(obj["_id"], obj["_name"], obj["_adresse"])
    except KeyError:
        return obj