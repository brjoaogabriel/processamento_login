class Ambiente(Dispositivo):

    def __init__(self):
        super().__init__();
        self.__horario = {'hora': datetime.datetime.now().hour, 'minuto': datetime.datetime.now().minute};
        self.__quantidadetentatvias = ContaLogs(super().getMaquina);

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
            if EstaEntre(self.getHorario, min(Horarios), max(Horarios)) == True:
                return True;
            else:
                return False;

    def ConfereQuantidadeTentativas(self):
        try:
            if self.getQuantidadeTentativas < 5:
                return True;
            else:
                return False;
        except:
            print("Erro de execução");


