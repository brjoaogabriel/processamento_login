class Habitualidade:

    def __init__(self, usuario, ambiente, dispositivo):
        self.__usuario = usuario;
        self.__ambiente = ambiente;
        self.__dispositivo = dispositivo;

    @property
    def __getUsuario(self):
        return self.__usuario;

    @property
    def __getAmbiente(self):
        return self.__ambiente;

    @property
    def __getDispositivo(self):
        return self.__dispositivo;

    def __ConfereUsuario(self):
        return True;
        if self.__getUsuario == True:
            return True;

    def __ConfereAmbiente(self):
        if self.__getAmbiente == True:
            return True;

    def __ConfereDispositivo(self):
        if self.__getDispositivo == True:
            return True;

    def __repr__(self):
        if (self.__ConfereAmbiente() == True) and (self.__ConfereUsuario() == True) and (self.__ConfereDispositivo() == True):
            return True;
        else:
            return False;