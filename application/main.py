from classes.database import *;
from application.functions import *;
from application.logs import *;
from classes.ambiente import *;
from classes.dispositivo import *;
from classes.usuario import *;
from classes.habitualidade import *;

thisDatabaseObject = Database(3306, 'localhost', 'root', '', 'test');

thisDispositivo = Dispositivo(thisDatabaseObject);
thisUsuario = Usuario('joaogabriel', 'itau', 'contato_joaogabriel@outlook.com', thisDatabaseObject);
thisAmbiente = Ambiente(thisDatabaseObject, thisDispositivo.getMaquina);

DatabaseObject = None;