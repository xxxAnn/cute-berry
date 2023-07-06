class BerryParser:

    @staticmethod
    def parse_inventory(s: str) -> dict:
        inv = {}

        for l in s.split(','):
            sp = BerryParser.num_pair(l)

            inv[sp[0]] = sp[1]

        return inv
    
    @staticmethod
    def num_pair(s: str) -> tuple[str, str]:
        data = s.split(':')

        return (int(data[0]), int(data[1]))