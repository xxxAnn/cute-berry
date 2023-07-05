class BerryModel:

    @staticmethod 
    def __generate_bytes(code: int, data: list[str]):
        data_str = '\r\n'.join(data)
        return f"{code}\r\n{data_str}\r\n".encode("UTF-8")
    
    @staticmethod
    def get_user(user_id):
        code = 1
        data = [
            user_id#// user id
        ]
        return BerryModel.__generate_bytes(code, data)
    