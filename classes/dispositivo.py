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

    @SistemaOperacional.setter
    def setSistemaOperacional(self, sistemaoperacional):
        self.__sistemaoperacional = sistemaoperacional;

    @Login.setter
    def setLogin(self, login):
        self.__login = login;

    @Maquina.setter
    def setMaquina(self, maquina):
        self.__maquina = maquina;

    def ConfereSO(self):
        Sistemas = BuscaSistemas(super().getLogin)
        QuantidadeAmostragemValida = 10;

        if len(Sistemas) > QuantidadeAmostragemValida:
            if self.getSistemaOperacional in Sistemas:
                return True;
            else:
                return False;

    def ConfereLogin(self):
        if len(self.getLogin > 0) and len(self.getLogin <= 24):
            return True;
        else:
            return False;

    def ConfereMaquina(self):
        Maquinas = BuscaMaquinas(super().getLogin)
        QuantidadeAmostragemValida = 10;

        if len(Maquinas) > QuantidadeAmostragemValida:
            if self.getMaquina in Maquinas:
                return True;
            else:
                return False;