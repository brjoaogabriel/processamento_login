from classes.database import *;
from application.functions import *;
from application.logs import *;
from classes.ambiente import *;
from classes.dispositivo import *;
from classes.usuario import *;
from classes.habitualidade import *;

Login = str(input("Login:   "));
Senha = str(input("Senha:   "));
Email = str(input("Email:   "));
print();

thisDatabaseObject = Database(3306, 'localhost', 'root', '', 'test');

thisUsuario = Usuario(Login, Senha, Email, thisDatabaseObject);
print(thisUsuario);

thisDispositivo = Dispositivo(thisDatabaseObject, thisUsuario.getLogin);
print(thisDispositivo);

thisAmbiente = Ambiente(thisDatabaseObject, thisDispositivo.getMaquina);
print(thisAmbiente);

thisResposta = Habitualidade(thisUsuario, thisAmbiente, thisDispositivo);
print(thisResposta);

DatabaseObject = None;