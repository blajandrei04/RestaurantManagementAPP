from RestaurantManagementAPP.Restaurant.modelle.gericht import Gericht

class Getranke(Gericht):
    def __init__(self, _id, portionGrosse, preiss, alkoholgehalt):
        super().__init__(_id, portionGrosse, preiss)
        self.__alkoholgehalt = alkoholgehalt
    def get_alkoholgehalt(self):
        return self.__alkoholgehalt

    def set_alkoholgehalt(self, new_alkoholgehalt):
        self.__alkoholgehalt = new_alkoholgehalt