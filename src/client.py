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
        bts = BerryModel.__generate_bytes(code, list(data))
        return self.__request(bts)
    
    #//
    
    def get_user(self, userid: int) -> User:
        return User(self.__request(BerryModel.get_user(str(userid))).splitlines())
    
    def available_recipes(self, userid: int) -> list[(int, int)]:
        data = self.__request(BerryModel.available_recipes(str(userid))).splitlines()

        if int(data[1]) == 0:
            return []
        else:
            return [(int(ind.split(':')[0]), int(ind.split(':')[1])) for ind in data[2:]]
    
    #// 

    def close(self):
        self.close()

    