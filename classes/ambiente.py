import datetime;
import platform;
from classes.VariaveisLogin import VariaveisLogin
from classes.dispositivo import Dispositivo

class Ambiente(VariaveisLogin):

    def __init__(self, DatabaseObject, maquina):
        super().__init__(DatabaseObject);
        self.__horario = datetime.datetime.now().time();
        self.__maquina = maquina;
        self.__quantidadetentativas = super().getDbObject.BuscaRegistro(f"{maquina}", 'log_tentativas', 'maquina', "Quantidade", True);
        self.__validado = False;

    @property
    def getHorario(self):
        return self.__horario;

    @property
    def getMaquina(self):
        return self.__maquina;

    @property
    def getQuantidadeTentativas(self):
        return self.__quantidadetentativas;

    @property
    def getValidado(self):
        return self.__validado;

    @getValidado.setter
    def setValidado(self, validacoes):
        self.__validado = validacoes;

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

    def Validar_Parametro(self):
        Parametro = {'nome':[], 'resultado':[]};

        Parametro['nome'].append('confere_horario');
        Parametro['resultado'].append(self.ConfereHorario());

        Parametro['nome'].append('confere_quantidade_tentativas');
        Parametro['resultado'].append(self.ConfereQuantidadeTentativas());

        self.setValidado = Parametro;

        Parametro = None;

        return False not in self.getValidado['resultado'];

    def __repr__(self):
        self.Validar_Parametro();
        super().printar_log(self.getValidado);
        if False not in self.getValidado['resultado']:
            return 'Aprovado\n';
        else:
            return 'Não aprovado\n';