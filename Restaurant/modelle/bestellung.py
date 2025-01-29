from RestaurantManagementAPP.Restaurant.modelle.identifiable import Identifiable
from RestaurantManagementAPP.Restaurant.repository.gekochterGerichtRepo import GekochterGerichtRepo
from RestaurantManagementAPP.Restaurant.repository.getrankeRepo import GetrankeRepo
from json import JSONEncoder

class Bestellung(Identifiable):
    def __init__(self, _id, kunden_id, gerichte_ids, getranke_ids):
        super().__init__(_id)
        self.kunden_id = kunden_id
        self.gerichte_ids = gerichte_ids
        self.getranke_ids = getranke_ids
        self.gesamtkosten = 0

    def __repr__(self):
        return f"ID: {self.get_id()}\nKunden ID: {self.kunden_id}\nGerichte IDs: {self.gerichte_ids}\nGetranke IDs: {self.getranke_ids}\nGesamtkosten: {self.gesamtkosten} \n"

    def berechne_kosten(self):
        self.gesamtkosten = 0
        for gericht_id in self.gerichte_ids:
            gericht = GekochterGerichtRepo.search_gericht(gericht_id)
            self.gesamtkosten += gericht.get_preiss()
        for getranke_id in self.getranke_ids:
            getranke = GetrankeRepo.search_getranke(getranke_id)
            self.gesamtkosten += getranke.get_preiss()

    def _erzeuge_rechnung_string(self):
        gerichte_strings = map(lambda gerichte_id: str(GekochterGerichtRepo(gerichte_id)), self.gerichte_ids)
        getranke_strings = map(lambda getranke_id: str(GetrankeRepo(getranke_id)), self.getranke_ids)
        rechnung = '\n'.join(list(gerichte_strings) + list(getranke_strings))
        return rechnung

    def zeige_rechnung(self):
        rechnung = self._erzeuge_rechnung_string()
        print(rechnung)
