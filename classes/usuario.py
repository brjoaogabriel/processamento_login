from classes.VariaveisLogin import VariaveisLogin

class Usuario(VariaveisLogin):

    def __init__(self, login, senha, email, DatabaseObject):
        super().__init__(DatabaseObject);
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

    def ConfereLogin(self):
        if super().getDbObject.BuscaRegistro(f"'{self.getLogin}'", "'user_info'", "login", "Existencia", True) == True:
            return True;
        else:
            return False;

    def ConfereSenha(self):
        if super().getDbObject.BuscaRegistro(f"'{self.getSenha}'", "'user_info'", "senha", "Existencia", True) == True:
            return True;
        else:
            return False;

    def ConfereEmail(self):
        if super().getDbObject.BuscaRegistro(f"'{self.getEmail}'", "'user_info'", "email", "Existencia", True) == True:
            return True;
        else:
            return False;

    def ConfereEntrada(self):
        main.DatabaseObject.BuscaRegistro(f"'{self.getLogin}'", 'user_info', 'login', "Registros", True);
        SenhaCorreta = main.DatabaseObject.getCursor.fetchall()[0]['senha'];
        if len(SenhaCorreta) > 0:
            if self.getSenha == SenhaCorreta:
                return True;

            else:
                return False;

        else:
            print("Senha incorreta.");

    def __repr__(self):
        if (self.ConfereSenha() == True) and (self.ConfereEmail() == True) and (self.ConfereLogin() == True) and (self.ConfereEntrada() == True):
            return True;
        else:
            return False;
