from classes.database import *;
from application.functions import *;
from application.logs import *;
from classes.ambiente import *;
from classes.dispositivo import *;
from classes.usuario import *;
from classes.habitualidade import *;

def Validar_Usuario():
    Login = str(input("Login:   "));
    Senha = str(input("Senha:   "));
    Email = str(input("Email:   "));
    print();

    thisDatabaseObject = Database(3306, 'localhost', 'root', '', 'test');

    thisUsuario = Usuario(Login, Senha, Email, thisDatabaseObject);
    thisUsuario.getValidado;
    print(thisUsuario);

    thisDispositivo = Dispositivo(thisDatabaseObject, thisUsuario.getLogin);
    thisDispositivo.getValidado;
    print(thisDispositivo);

    thisAmbiente = Ambiente(thisDatabaseObject, thisDispositivo.getMaquina);
    thisAmbiente.getValidado;
    print(thisAmbiente);

    thisResposta = Habitualidade(thisUsuario.Validar_Parametro(), thisAmbiente.Validar_Parametro(), thisDispositivo.Validar_Parametro());
    Resultado = thisResposta.Validar_Parametro();
    print(thisResposta);

    if Resultado == True:
        thisDatabaseObject.Gerar_Log(Login, thisDispositivo.getSistemaOperacional, thisDispositivo.getMaquina, thisAmbiente.getHorario, 1);
    else:
        thisDatabaseObject.Gerar_Log(Login, thisDispositivo.getSistemaOperacional, thisDispositivo.getMaquina, thisAmbiente.getHorario, 0);

    thisDatabaseObject = None;

    print("Finalizando execução da validação do usuário...");

    return Resultado;

Validar_Usuario();