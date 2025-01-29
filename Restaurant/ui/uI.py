from RestaurantManagementAPP.Restaurant.controller.controler import Controller
class UI():
    def __init__(self):
        self.controler = Controller("kundenRepo.json", "getrankeRepo.json", "gekochterGerichtRepo.json", "bestellungRepo.json.json")
    def print_menu(self):
        print("1. Create Gericht")
        print("2. Search Kunde by Name")
        print("3. Search Kunde by Adresse")
        print("4. Update Kunde Name")
        print("5. Convert to String Rechnung")
        print("6. Add Bestellung")
        print("7. Convert to String Bestellung")
        print("0. Exit")
    def menu(self, option):
        while option != 0:
            self.print_menu()
            if option == 1:
                gericht_id = int(input("ID: "))
                portionGrosse = int(input("PortionGrosse: "))
                preiss = int(input("Preiss: "))
                gericht = self.controler.create_gericht(gericht_id, portionGrosse, preiss)
                self.controler.add_to_repo(gericht)

            elif option == 2:
                name = input("Partial Name: ")
                customer = self.controler.search_kunde_by_name( name)
                print(customer)

            elif option == 3:
                address = input("Partial Address: ")
                customer = self.controler.search_kunde_by_adresse( address)
                print(customer)
            elif option == 4:
                _id = input("ID: ")
                new_name = input("New Name: ")
                self.controler.update_kunde_name(_id, new_name)
            elif option == 5:
                _id = int(input("ID: "))
                print(self.controler.convert_to_string_rechnung(_id))
            elif option == 6:
                _id = int(input("ID: "))
                kunden_id = int(input("Kunden ID: "))
                gerichte_ids = list(map(int, input("Gerichte IDs: ").split()))
                getranke_ids = list(map(int, input("Getranke IDs: ").split()))
                bestellung = self.controler.create_bestellung(kunden_id, gerichte_ids, getranke_ids)
                self.controler.save_bestellung(bestellung)
            elif option == 7:
                _id = int(input("ID: "))
                print(self.controler.convert_to_string_rechnung(_id))
            else:
                print("Invalid Option")
            option = int(input("Option: "))
