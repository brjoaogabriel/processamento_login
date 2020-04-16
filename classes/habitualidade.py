class Habitualidade:

    def __init__(self, usuario, ambiente, dispositivo):
        self.__usuario = usuario;
        self.__ambiente = ambiente;
        self.__dispositivo = dispositivo;

    @property
    def getUsuario(self):
        return self.__usuario;

    @property
    def getAmbiente(self):
        return self.__ambiente;

    @property
    def getDispositivo(self):
        return self.__dispositivo;

    @Usuario.setter
    def setUsuario(self, usuario):
        self.__usuario = usuario;

    @Ambiente.setter
    def setAmbiente(self, ambiente):
        self.__ambiente = ambiente;

    @Dispositivo.setter
    def setDispositivo(self, dispositivo):
        self.__dispositivo = dispositivo;

    def ConfereUsuario(self):
        return True;
        for parametro in self.getUsuario:
            if parametro == False:
                return False;

    def ConfereAmbiente(self):
        return True;
        for parametro in self.getAmbiente:
            if parametro == False:
                return False;

    def ConfereDispositivo(self):
        return True;
        for parametro in self.getDispositivo:
            if parametro == False:
                return False;

    def __repr__(self):
        if (self.ConfereAmbiente() == True) and (self.ConfereUsuario() == True) and (self.ConfereDispositivo() == True):
            return True;
        else:
            return False;