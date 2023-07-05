class Berry:
    
    def _parse_item(self, data: str):
        inv = {}

        for l in data.split(','):
            sp = l.split(':')

            inv[int(sp[0])] = int(sp[1])

        return inv
    
    def _repr(self, name: str, data: list[tuple[str,str]]):
        sub = ', '.join([f"{a}: {b}" for (a, b) in data])
        return f"{name}({sub})"