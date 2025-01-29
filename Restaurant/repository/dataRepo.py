from abc import ABC, abstractmethod
from RestaurantManagementAPP.Restaurant.repository.utils import MyEncoder
import json
import jsonpickle
from collections import namedtuple
from RestaurantManagementAPP.Restaurant.repository.utils import customDecoder

class DataRepo(ABC):
    def __init__(self, file):
        self.__file = file

    @abstractmethod
    def read_data(self):
        # file = open(self.__file, 'r')
        # jContent = file.read()
        # data = json.loads(jContent)
        # file.close()
        # print(data)
        # return data
        file = open(self.__file, 'r')
        data = file.read()
        data = json.loads(data, object_hook=customDecoder)
        return data

    @abstractmethod
    def write_data(self, data):
        file = open(self.__file, 'w')
        # jContent = json.dumps(data.toJson())
        file.write(json.dumps(data, cls=MyEncoder))

        # file.write(data.toJson())
        # file.write(jContent)
        file.close()

    @abstractmethod
    def save_data(self, data):
        file = open(self.__file, 'a')
        # jContent = json.dumps(data.toJson())
        # file.write(data.toJson())
        file.write(json.dumps(data, cls=MyEncoder))
        file.close()
    @abstractmethod
    def load_data(self):
        # file = open(self.__file, 'r')
        file = open(self.__file, 'r')
        data = file.read()
        data = json.loads(data, object_hook=customDecoder)
        return data
    def convert_to_string(self, data):
        return json.dumps(data)
