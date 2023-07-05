from typing import Callable

from .berry import User

class BerryModel:

    GET_USER = 0
    AVAILABLE_RECIPES = 4

    @staticmethod 
    def __generate_bytes(code: int, data: list[str]):
        data_str = '\r\n'.join(data)
        return f"{code}\r\n{data_str}\r\n".encode("UTF-8")
    
    @staticmethod
    def get_user(f: Callable[[str], str], user_id):
        data = [
            user_id
        ]
        return User(f(BerryModel.__generate_bytes(BerryModel.GET_USER, data)).splitlines())
    
    @staticmethod
    def available_recipes(f: Callable[[str], str], user_id):
        data = [
            user_id
        ]
        data = f(BerryModel.__generate_bytes(BerryModel.AVAILABLE_RECIPES, data)).splitlines()

        return [(int(ind.split(':')[0]), int(ind.split(':')[1])) for ind in data[2:]]