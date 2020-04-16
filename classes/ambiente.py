import datetime
import platfrom

class Ambiente():

    def __init__(self):
        self.__horario = {'hora': datetime.datetime.now().hour, 'minuto': datetime.datetime.now().minute};
        self.__quantidadetentativas = ContaLogs(platform.node);

    @property
    def getHorario(self):
        return self.__horario;

    @property
    def getQuantidadeTentativas(self):
        return self.__quantidadetentativas;

    @setHorario.setter
    def setHorario(self, horario):
        self.__horario = horario;

    @setQuantidadeTentativas.setter
    def setQuantidadeTentatvias(self, quantidadetentativas):
        self.__quantidadetentativas = quantidadetentativas;

    def ConfereHorario(self, maquina):
        QuantidadeAmostragemValida = 10;
        Horarios = BuscarLogs(datetime.datetime.now().hour, datetime.datetime.now().minute, maquina);

        if len(Horarios) > QuantidadeAmostragemValida:
            if EstaEntre(self.getHorario, min(Horarios), max(Horarios)) == True:
                return True;
            else:
                return False;
        else:
            return True;

    def ConfereQuantidadeTentativas(self):
        if self.getQuantidadeTentativas < 5:
            return True;
        else:
            return False;

    def __repr__(self):
        if (self.ConfereHorario() == True) and (self.ConfereQuantidadeTentativas() == True):
            return True;
        else:
            return False;