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

    def __repr__(self):
        Parametro = {'nome':[], 'resultado':[]};

        Parametro['nome'].append('confere_sistema_operacional');
        Parametro['resultado'].append(self.ConfereSO());

        Parametro['nome'].append('confere_login');
        Parametro['resultado'].append(self.ConfereLogin());

        Parametro['nome'].append('confere_maquina');
        Parametro['resultado'].append(self.ConfereMaquina());

        for i in range(0, len(Parametro['nome']), 1):
            print(f"    - {Parametro['nome'][i]} - {Parametro['resultado'][i]}");

        if "False" in Parametro['resultado']:
            return "Dispositivo.        False\n";

        else:
            return "Dispositivo.        True\n";



