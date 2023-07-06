class BerryError(Exception):

    def __init__(self, txt):
        self.text = txt
        super().__init__(self.text)