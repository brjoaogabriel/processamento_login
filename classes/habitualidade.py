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
        return self.__getUsuario;

    def __ConfereAmbiente(self):
        return self.__getAmbiente;

    def __ConfereDispositivo(self):
        return self.__getDispositivo;

    def __repr__(self):
        Parametro = {'nome':[], 'resultado':[]};

        Parametro['nome'].append('confere_ambiente');
        Parametro['resultado'].append(self.__ConfereAmbiente())

        Parametro['nome'].append('confere_usuario');
        Parametro['resultado'].append(self.__ConfereUsuario());

        Parametro['nome'].append('confere_dispositivo');
        Parametro['resultado'].append(self.__ConfereDispositivo())

        return "Aprovado";