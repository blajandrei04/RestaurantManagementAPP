class Identifiable:
    def __init__(self, _id):
        self.__id = _id

    def get_id(self):
        return self.__id
    def set_id(self, new_id):
        self.__id = new_id