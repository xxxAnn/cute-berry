from lib.client import CuteBerry

HOST = "127.0.0.1"
PORT = 8080  
USERID = 331431342438875137
        

def main():
    cute_berry = CuteBerry(HOST, PORT)

    print(cute_berry.get_user(331431342438875137))