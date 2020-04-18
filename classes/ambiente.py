import datetime;
import platform;
from classes.VariaveisLogin import VariaveisLogin
from classes.dispositivo import Dispositivo

class Ambiente(VariaveisLogin):

    def __init__(self, DatabaseObject, maquina):
        super().__init__(DatabaseObject);
        self.__horario = datetime.datetime.now();
        self.__quantidadetentativas = super().getDbObject.BuscaRegistro(f"'{maquina}'", 'log_tentativas', 'maquina', "Quantidade", True);

    @property
    def getHorario(self):
        return self.__horario;

    @property
    def getQuantidadeTentativas(self):
        return self.__quantidadetentativas;

    def ConfereHorario(self, maquina):
        QuantidadeAmostragemValida = 10;
        Horarios = super().getDbObject.BuscaRegistro(f"'{Dispositivo.getMaquina}'", 'log_tentativas', 'maquina', "Registros", True);

        if len(Horarios) > QuantidadeAmostragemValida:
            if EstaEntre(self.getHorario, Horarios) == True:
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