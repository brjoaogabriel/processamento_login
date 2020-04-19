from classes.VariaveisLogin import VariaveisLogin

class Usuario(VariaveisLogin):

    def __init__(self, login, senha, email, DatabaseObject):
        super().__init__(DatabaseObject);
        self.__login = login;
        self.__senha = senha;
        self.__email = email;
        self.__validado = False;

    @property
    def getLogin(self):
        return self.__login;

    @property
    def getSenha(self):
        return self.__senha;

    @property
    def getEmail(self):
        return self.__email;

    @property
    def getValidado(self):
        return self.__validado;

    @getValidado.setter
    def setValidado(self, validacoes):
        self.__validado = validacoes;

    def ConfereLogin(self):
        return super().getDbObject.BuscaRegistro(f'{self.getLogin}', 'user_info', 'desc_login', "Existencia", True);

    def ConfereSenha(self):
        return super().getDbObject.BuscaRegistro(f'{self.getSenha}', 'user_info', 'desc_senha', "Existencia", True);

    def ConfereEmail(self):
        return super().getDbObject.BuscaRegistro(f'{self.getEmail}', 'user_info', 'desc_email', "Existencia", True);

    def ConfereEntrada(self):
        return super().getDbObject.Valida_Senha(self.getLogin, self.getSenha);

    def Validar_Parametro(self):
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

        self.setValidado = Parametro;

        Parametro = None;

        return False not in self.getValidado['resultado'];




    def __repr__(self):
        self.Validar_Parametro();
        if False not in self.getValidado['resultado']:
            return 'Aprovado\n';
        else:
            return 'Não aprovado\n';