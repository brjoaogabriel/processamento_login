import platform
import os

class Dispositivo(Usuario):

    def __init__(self):
        super().__init__()
        self.__sistemaoperacional = platform.system();
        self.__login = os.getlogin();
        self.__maquina = platform.node();

    @property
    def getSistemaOperacional(self):
        return self.__sistemaoperacional;

    @property
    def getLogin(self):
        return self.__login;

    @property
    def getMaquina(self):
        return self.__maquina;

    def ConfereSO(self, login, DatabaseObject):
        return False;
        Sistemas = DatabaseObject.BuscaRegistro(f"'{login}", 'log_tentativas', 'login', "Registros", True);
        QuantidadeAmostragemValida = 10;

        if len(Sistemas) > QuantidadeAmostragemValida:
            for i in range(0, len(Sistemas), 1):
                if self.getSistemaOperacional in Sistemas[i]['sistema']:
                    return True;

    def ConfereLogin(self):
        if len(self.getLogin > 0) and len(self.getLogin <= 24):
            return True;
        else:
            return False;

    def ConfereMaquina(self, login, DatabaseObject):
        return False;
        Maquinas = DatabaseObject.BuscaRegistro(f"'{login}", 'log_tentativas', 'login', "Registros", True);
        QuantidadeAmostragemValida = 10;

        if len(Maquinas) > QuantidadeAmostragemValida:
            for i in range(0, len(Maquinas), 1):
                if self.getMaquina in Maquinas[i]['maquina']
                    return True;

    def __repr__(self):
        if (self.ConfereSO() == True) and (self.ConfereLogin() == True) and (self.ConfereMaquina() == True):
            return True;
        else:
            return False;