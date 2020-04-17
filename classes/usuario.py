class Usuario:

    def __init__(self, login, senha, email):
        self.__login = login;
        self.__senha = senha;
        self.__email = email;

    @property
    def getLogin(self):
        return self.__login;

    @property
    def getSenha(self):
        return self.__senha;

    @property
    def getEmail(self):
        return self.__email;

    def ConfereLogin(self, DatabaseObject):
        if DatabaseObject.BuscaRegistro(f"'{self.getLogin}'", "'user_info'", "login", "Existencia", True) == True:
            return True;
        else:
            return False;

    def ConfereSenha(self, DatabaseObject):
        if DatabaseObject.BuscaRegistro(f"'{self.getSenha}'", "'user_info'", "senha", "Existencia", True) == True:
            return True;
        else:
            return False;

    def ConfereEmail(self, DatabaseObject):
        if DatabaseObject.BuscaRegistro(f"'{self.getEmail}'", "'user_info'", "email", "Existencia", True) == True:
            return True;
        else:
            return False;

    def __repr__(self):
        if (self.ConfereSenha() == True) and (self.ConfereEmail() == True) and (self.ConfereLogin() == True):
            return True;
        else:
            return False;
