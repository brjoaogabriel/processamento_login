import datetime;
import platform;
from classes.VariaveisLogin import VariaveisLogin
from classes.dispositivo import Dispositivo

class Ambiente(VariaveisLogin):

    def __init__(self, DatabaseObject, maquina):
        super().__init__(DatabaseObject);
        self.__horario = datetime.datetime.now();
        self.__maquina = maquina;
        self.__quantidadetentativas = super().getDbObject.BuscaRegistro(f"{maquina}", 'log_tentativas', 'maquina', "Quantidade", True);

    @property
    def getHorario(self):
        return self.__horario;

    @property
    def getMaquina(self):
        return self.__maquina;

    @property
    def getQuantidadeTentativas(self):
        return self.__quantidadetentativas;

    def ConfereHorario(self):
        QuantidadeAmostragemValida = 10;
        super().getDbObject.BuscaRegistro(f'{self.getMaquina}', 'log_tentativas', 'maquina', "Registros", True);
        Horarios = super().getDbObject.getCursor.fetchall();

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
        Parametro = {'nome':[], 'resultado':[]};

        Parametro['nome'].append('confere_horario');
        Parametro['resultado'].append(self.ConfereHorario());

        Parametro['nome'].append('confere_quantidade_tentativas');
        Parametro['resultado'].append(self.ConfereQuantidadeTentativas());

        for i in range(0, len(Parametro['nome']), 1):
            print(f"    - {Parametro['nome'][i]} - {Parametro['resultado'][i]}");

        if False in Parametro['resultado']:
            return "Ambiente.           False\n";
        else:
            return "Ambiente.           True\n";