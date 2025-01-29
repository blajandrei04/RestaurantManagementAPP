from RestaurantManagementAPP.Restaurant.modelle.identifiable import Identifiable
class Gericht(Identifiable):
    def __init__(self, _id, portionGrosse, preiss):
        super().__init__(_id)
        self.__portionGrosse = portionGrosse
        self.__preiss = preiss
    def get_portiongrosse(self):
        return self.__portionGrosse

    def set_portionGrosse(self, new_portionGrosse):
        self.__portionGrosse = new_portionGrosse

    def get_preiss(self):
        return self.__preiss

    def set_preiss(self, new_preiss):
        self.__preiss = new_preiss