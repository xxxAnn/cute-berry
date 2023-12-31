from typing import Callable, TypeAlias

from lib.berry import User, Recipe
from lib.model.parser import BerryParser as BP
from lib.model.error import BerryError

Requester: TypeAlias = Callable[[str], str]
Bytifier: TypeAlias = Callable[[int, list[str]], bytes]

class BerryModel:

    GET_USER = 1
    GET_RECIPE = 3
    AVAILABLE_RECIPES = 4

    @staticmethod 
    def __generate_bytes(code: int, data: list[str]) -> bytes:
        data_str = '\r\n'.join(data)
        return f"{code}\r\n{data_str}\r\n".encode("UTF-8")
    
    @staticmethod
    def __call(data: list[str], code: int, rqster: Requester, converter, btfer: Bytifier=None):
        btfer = btfer or BerryModel.__generate_bytes
        res = rqster(btfer(code, data)).splitlines()
        if "err_" in res[0]: 
            raise BerryError(res[1])
        else:
            return converter(res)
    
    @staticmethod
    def get_user(f: Requester, *data):
        return BerryModel.__call(
            list(data),
            BerryModel.GET_USER,
            f,
            User
        )
    
    
    @staticmethod
    def available_recipes(f: Requester, *data):
        return BerryModel.__call(
            list(data),
            BerryModel.AVAILABLE_RECIPES,
            f,
            lambda res: [((x := BP.num_pair(ind))[0], x[1]) for ind in res[2:]]
        )
    
    @staticmethod
    def get_recipe(f: Requester, *data):
        return BerryModel.__call(
            list(data),
            BerryModel.GET_RECIPE,
            f,
            lambda res: Recipe(res[1])
        )