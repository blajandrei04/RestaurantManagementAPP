from RestaurantManagementAPP.Restaurant.repository.dataRepo import DataRepo
class GetrankeRepo(DataRepo):
    def __init__(self, file):
        super().__init__(file)
    def save_data(self, data):
        super().save_data(data)
    def load_data(self):
        super().load_data()
    def read_data(self):
        super().read_data()
    def write_data(self, data):
        super().write_data(data)