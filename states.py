class Estados:
    
    def __init__(self, sigla, nome, flag):
        self.__sigla  = sigla
        self.__nome = nome
        self.__flag = flag

    def get_sigla(self):
        return self.__sigla
    
    def get_nome(self):
        return self.__nome

    def get_flag(self):
        return self.__flag

    def get_news_list(self):
        return self.__news_list
    
    def set_news_list(self, news_list):
        self.__news_list = news_list
