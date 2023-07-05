
class BerryModel:

    @staticmethod 
    def __generate_bytes(code: int, data: list[str]):
        data_str = '\r\n'.join(data)
        return f"{code}\r\n{data_str}\r\n".encode("UTF-8")
    
    @staticmethod
    def get_user(user_id):
        code = 1
        data = [
            user_id#// user id
        ]
        return BerryModel.__generate_bytes(code, data)
    
class Berry:
    pass

class User(Berry):

    def __init__(self, data: list[str]):
        self.id = int(data[0])
        self.balance = int(data[2])
        coords = data[3].split(',')
        self.coords = (coords[0], coords[1])
        self.energy = data[4]
        self.__generate_inventory(data[1])

    def __generate_inventory(self, data: str):

        self.inventory = {}

        for l in data.split(','):
            sp = l.split(':')

            self.inventory[int(sp[0])] = int(sp[1])

    def __repr__(self) -> str:
        return f"""User(
    ID: {self.id}
    Balance: {self.balance}
    Coords: {self.coords}
    Energy: {self.energy}
    Inventory: {self.inventory}
)
        """