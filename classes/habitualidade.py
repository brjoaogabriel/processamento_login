class Habitualidade:

    def __init__(self, usuario, ambiente, dispositivo):
        self.__usuario = usuario;
        self.__ambiente = ambiente;
        self.__dispositivo = dispositivo;
        self.__validado = False;

    @property
    def __getUsuario(self):
        return self.__usuario;

    @property
    def __getAmbiente(self):
        return self.__ambiente;

    @property
    def __getDispositivo(self):
        return self.__dispositivo;

    @property
    def __getValidado(self):
        return self.__validado;

    @__getValidado.setter
    def __setValidado(self, validacoes):
        self.__validado = validacoes;

    def __ConfereUsuario(self):
        return self.__getUsuario;

    def __ConfereAmbiente(self):
        return self.__getAmbiente;

    def __ConfereDispositivo(self):
        return self.__getDispositivo;

    def Validar_Parametro(self):
        Parametro = {'nome':[], 'resultado':[]};

        Parametro['nome'].append('confere_ambiente');
        Parametro['resultado'].append(self.__getAmbiente);

        Parametro['nome'].append('confere_usuario');
        Parametro['resultado'].append(self.__getUsuario);

        Parametro['nome'].append('confere_dispositivo');
        Parametro['resultado'].append(self.__getDispositivo);

        self.__setValidado = Parametro;

        Parametro = None;

        return False not in self.__getValidado['resultado'];

    def __repr__(self):
        self.Validar_Parametro();
        if False not in self.__getValidado['resultado']:
            return 'Aprovado\n';
        else:
            return 'Não aprovado\n';