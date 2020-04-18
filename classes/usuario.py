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
        if super().getDbObject.BuscaRegistro(f'{self.getLogin}', 'user_info', 'desc_login', "Existencia", True) == True:
            return True;
        else:
            return False;

    def ConfereSenha(self):
        if super().getDbObject.BuscaRegistro(f'{self.getSenha}', 'user_info', 'desc_senha', "Existencia", True) == True:
            return True;
        else:
            return False;

    def ConfereEmail(self):
        if super().getDbObject.BuscaRegistro(f'{self.getEmail}', 'user_info', 'desc_email', "Existencia", True) == True:
            return True;
        else:
            return False;

    def ConfereEntrada(self):
        super().getDbObject.getCursor.execute(f"select * from user_info where desc_login = '{self.getLogin}'")
        SenhaCorreta = super().getDbObject.getCursor.fetchall()[0]['desc_senha'];
        if len(SenhaCorreta) > 0:
            if self.getSenha == SenhaCorreta:
                return True;

            else:
                return False;

        else:
            print("Senha incorreta.");

    def __repr__(self):
        Parametro = {'nome':[], 'resultado':[]};

        Parametro['nome'].append('confere_senha');
        Parametro['resultado'].append(self.ConfereSenha());

        Parametro['nome'].append('confere_email');
        Parametro['resultado'].append(self.ConfereEmail());

        Parametro['nome'].append('confere_login');
        Parametro['resultado'].append(self.ConfereLogin());

        Parametro['nome'].append('confere_entrada');
        Parametro['resultado'].append(self.ConfereEntrada());

        for i in range(0, len(Parametro['nome']), 1):
            print(f"    - {Parametro['nome'][i]} - {Parametro['resultado'][i]}");

        if False in Parametro['resultado']:
            return "Usuario.            False\n";
        else:
            return "Usuario.            True\n";
