import sys
from lib.client import CuteBerry

HOST = sys.argv[1]
PORT = 80
USERID = 331431342438875137
        

def main():
    cute_berry = CuteBerry(HOST, PORT)

    print(cute_berry.get_user(331431342438875137))