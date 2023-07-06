import socket

from src.model import BerryModel
from src.berry import User, Recipe

class CuteBerry:

    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__connect(host, port)

    def __connect(self, host, port):
        self.socket.connect((host, port))

    def __request(self, bts: str) -> str:
        self.socket.sendall(bts)
        data = self.socket.recv(1024)
        return str(data, "UTF-8")

    def _request(self, code: int, *data: list[str]) -> str:
        return self.__request(BerryModel.__generate_bytes(code, list(data)))
    #//
    
    def get_user(self, userid: int) -> User:
        return BerryModel.get_user(self.__request, str(userid))
    
    def available_recipes(self, userid: int) -> list[(int, int)]:
        return BerryModel.available_recipes(self.__request, str(userid))
    
    def get_recipe(self, recipeid: int) -> Recipe:
        return BerryModel.get_recipe(self.__request, str(recipeid))
    
    #// 

    def close(self):
        self.close()

    