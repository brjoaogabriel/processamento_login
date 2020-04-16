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

    @setLogin.setter
    def setLogin(self, login):
        self.__login = login;

    @setSenha.setter
    def setSenha(self, senha):
        self.__senha = senha;

    @setEmail.setter
    def setEmail(self, email):
        self.__email = email;

    def ConfereLogin(self):
        if ExisteRegistro('user_info', 'login',self.getLogin) == True:
            return True;
        else:
            return False;

    def ConfereSenha(self):
        if ExisteRegistro('user_info', 'senha', self.getSenha) == True:
            return True;
        else:
            return False;

    def ConfereEmail(self):
        if ExisteRegistro('user_info', 'email', self.getEmail) == True:
            return True;
        else:
            return False;

    def __repr__(self):
        if (self.ConfereSenha() == True) and (self.ConfereEmail() == True) and (self.ConfereLogin() == True):
            return True;
        else:
            return False;
