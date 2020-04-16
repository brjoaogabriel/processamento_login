class Ambiente:

    def __init__(self, horario=datetime.datetime.now().time(), quantidadetentativas=0):
        self.__horario = horario;
        self.__quantidadetentatvias = quantidadetentativas;

    @property
    def getHorario(self):
        return self.__horario;

    @property
    def getQuantidadeTentativas(self):
        return self.__quantidadetentatvias;

    @Horario.setter
    def setHorario(self, horario):
        self.__horario = horario;

    @QuantidadeTentativas.setter
    def setQuantidadeTentatvias(self, quantidadetentativas):
        self.__quantidadetentatvias = quantidadetentativas;

    def ConfereHorario(self, maquina):
        QuantidadeAmostragemValida = 10;
        Horarios = BuscarLogs(datetime.datetime.now().hour, datetime.datetime.now().minute, Dispositivo.getMaquina);
        if len(Horarios > QuantidadeAmostragemValida):
            if (self.getHorario >= min(Horarios)) and (self.getHorario <= max(Horarios)):
                return True;
            else:
                return False;

    def ConfereQuantidadeTentativas(self):


