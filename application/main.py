from classes.database import *;
from application.functions import *;
from application.logs import *;
from classes.ambiente import *;
from classes.dispositivo import *;
from classes.usuario import *;
from classes.habitualidade import *;

thisDatabaseObject = Database(3306, 'localhost', 'root', '', 'test');

thisUsuario = Usuario('joaogabriel', 'itau', 'contato_joaogabriel@outlook.com', thisDatabaseObject);
print(thisUsuario);

thisDispositivo = Dispositivo(thisDatabaseObject, thisUsuario.getLogin);
print(thisDispositivo);

thisAmbiente = Ambiente(thisDatabaseObject, thisDispositivo.getMaquina);
print(thisAmbiente);

thisResposta = Habitualidade(thisUsuario, thisAmbiente, thisDispositivo);
print(thisResposta);

DatabaseObject = None;