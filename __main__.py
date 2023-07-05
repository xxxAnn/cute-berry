from src import CuteBerry

HOST = "127.0.0.1"
PORT = 7878  
USERID = 331431342438875137
        

def main():
    cute_berry = CuteBerry(HOST, PORT)

    print(cute_berry.available_recipes(USERID))

if __name__ == "__main__":
    main()
