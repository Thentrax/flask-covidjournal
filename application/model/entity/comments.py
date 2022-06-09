from nanoid import generate

class Comments:

    def __init__(self, author, text):
        self.__id = generate('0123456789')
        self.__author = author
        self.__text = text

    def get_id(self):
        return self.__id
    
    def get_author(self):
        return self.__author
    
    def get_text(self):
        return self.__text