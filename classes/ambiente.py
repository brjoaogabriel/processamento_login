import datetime
import platfrom

class Ambiente():

    def __init__(self, DatabaseObject):
        self.__horario = {'hora': datetime.datetime.now().hour, 'minuto': datetime.datetime.now().minute};
        self.__quantidadetentativas = DatabaseObject.BuscaRegistro(f"'{maquina}'", 'log_tentativas', 'maquina', "Quantidade", True);

    @property
    def getHorario(self):
        return self.__horario;

    @property
    def getQuantidadeTentativas(self):
        return self.__quantidadetentativas;

    def ConfereHorario(self, maquina, DatabaseObject):
        QuantidadeAmostragemValida = 10;
        Horarios = DatabaseObject.BuscaRegistro(f"'{maquina}'", 'log_tentativas', 'maquina', "Registros", True);

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