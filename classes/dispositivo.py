import platform
import os
from classes.VariaveisLogin import VariaveisLogin

class Dispositivo(VariaveisLogin):

    def __init__(self, DatabaseObject, login):
        super().__init__(DatabaseObject)
        self.__sistemaoperacional = platform.system();
        self.__login = os.getlogin();
        self.__secondlogin = login;
        self.__maquina = platform.node();
        self.__validado = False;

    @property
    def getSistemaOperacional(self):
        return self.__sistemaoperacional;

    @property
    def getLogin(self):
        return self.__login;

    @property
    def getSecondLogin(self):
        return self.__secondlogin;

    @property
    def getMaquina(self):
        return self.__maquina;

    @property
    def getValidado(self):
        return self.__validado;

    @getValidado.setter
    def setValidado(self, validacoes):
        self.__validado = validacoes;

    def ConfereSO(self):
        super().getDbObject.BuscaRegistro(f"{self.getSecondLogin}", 'log_tentativas', 'login', "Registros", True);
        Sistemas = super().getDbObject.getCursor.fetchall();
        QuantidadeAmostragemValida = 10;

        if len(Sistemas) > QuantidadeAmostragemValida:
            return self.getSistemaOperacional in Sistemas['sistema_op'];

        else:
            return True;

    def ConfereLogin(self):
        if len(self.getLogin) > 0 and len(self.getLogin) <= 24:
            return True;
        else:
            return False;

    def ConfereMaquina(self):
        super().getDbObject.BuscaRegistro(f"{self.getSecondLogin}", 'log_tentativas', 'login', "Registros", True);
        Maquinas = super().getDbObject.getCursor.fetchall();
        QuantidadeAmostragemValida = 10;

        if len(Maquinas) > QuantidadeAmostragemValida:
            return self.GetMaquina in Maquinas;

        else:
            return True;

    def Validar_Parametro(self):
        Parametro = {'nome':[], 'resultado':[]};

        Parametro['nome'].append('confere_login');
        Parametro['resultado'].append(self.ConfereLogin());

        Parametro['nome'].append('confere_sistema_operacional');
        Parametro['resultado'].append(self.ConfereSO());

        Parametro['nome'].append('confere_maquina');
        Parametro['resultado'].append(self.ConfereMaquina());

        self.setValidado = Parametro;

        Parametro = None;

        return False not in self.getValidado['resultado'];

    def __repr__(self):
        self.Validar_Parametro();
        super().printar_log(self.getValidado);
        if False not in self.getValidado['resultado']:
            return 'Aprovado\n';
        else:
            return 'Não aprovado\n';



