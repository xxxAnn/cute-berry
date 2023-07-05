from .base import Berry

class User(Berry):

    def __init__(self, data: list[str]):
        self.id = int(data[0])
        self.balance = int(data[2])
        coords = data[3].split(',')
        self.coords = (int(coords[0]), int(coords[1]))
        self.energy = data[4]
        self.__generate_inventory(data[1])

    def __generate_inventory(self, data: str):

        self.inventory = self._parse_item(data)

    def __str__(self) -> str:
        return self._repr(
            "User",
            [
                ("ID", self.id),
                ("Balance", self.balance),
                ("Coords", self.coords),
                ("Energy", self.energy),
                ("Inventory", self.inventory)
            ]
        )