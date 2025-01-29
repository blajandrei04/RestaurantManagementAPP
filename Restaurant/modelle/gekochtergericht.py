from RestaurantManagementAPP.Restaurant.modelle.gericht import Gericht
class GekochterGericht(Gericht):
    def __init__(self, _id, portionGrosse, preiss, zubereitungsZeit):
        super().__init__(_id, portionGrosse, preiss)
        self.__zubereitungszeit = zubereitungsZeit

    def get_zubereitungsZeit(self):
        return self.__zubereitungszeit
    def set_zubereitungsZeit(self, new_zubereitungszeit):
        self.__zubereitungszeit = new_zubereitungszeit