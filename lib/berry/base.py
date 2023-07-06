from lib.model.parser import BerryParser

class Berry:
    
    def _parse_item(self, data: str):
        return BerryParser.parse_inventory(data)
    
    def _repr(self, name: str, data: list[tuple[str,str]]):
        sub = ', '.join([f"{a}: {b}" for (a, b) in data])
        return f"{name}({sub})"