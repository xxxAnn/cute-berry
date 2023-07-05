import socket

from .model import BerryModel
from .berry import User, Recipe

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
        data = BerryModel.available_recipes(self.__request, str(userid))

        return [(int(ind.split(':')[0]), int(ind.split(':')[1])) for ind in data[2:]]
    
    #// 

    def close(self):
        self.close()

    