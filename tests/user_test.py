from src.berry.user import User

import unittest

class TestUser(unittest.TestCase):

    def test_create(self):
        self.assertEqual(
            User([
                "000",
                "1:100",
                "100",
                "3,4",
                "30"
            ])._pairs(), 
            [
                ("ID", 0),
                ("Balance", 100),
                ("Coords", (3, 4)),
                ("Energy", 30),
                ("Inventory", {1:100})
            ]
        )


if __name__ == '__main__':
    unittest.main()