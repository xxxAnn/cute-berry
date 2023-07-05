from .base import Berry

class Recipe(Berry):
    
    def __init__(self, data: str):

        inpouts = data.split('->')

        self.inputs = self._parse_item(inpouts[0])
        self.outputs = self._parse_item(inpouts[1])

    def __str__(self) -> str:
        return self._repr(
            "Recipe",
            [
                ("Inputs", self.inputs),
                ("Outputs", self.outputs)
            ]
        )