class News:

    def __init__(self, id, tittle, headline, text, image, state):
        self.__id = id
        self.__tittle = tittle
        self.__headline = headline
        self.__text = text
        self.__image = image
        self.__state = state
    
    def get_id(self):
        return self.__id
    
    def get_tittle(self):
        return self.__tittle
    
    def get_headline(self):
        return self.__headline

    def get_text(self):
        return self.__text
    
    def get_image(self):
        return self.__image

    def get_state(self):
        return self.__state

    
# News (0, "", "", '', '',''),
