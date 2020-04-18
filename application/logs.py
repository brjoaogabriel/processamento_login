from classes.database import Database
import datetime

DatabaseObject = Database(3306, 'localhost', 'root', '', 'test');

DatabaseObject.ConectarBase();

DatabaseObject.ConectarCursor();

DatabaseObject.setCursor.execute("insert into teste (id_teste, desc_teste) values (1, 'a');");

DatabaseObject.DesconectarCursor();

DatabaseObject.DesconectarBase();

DatabaseObject = None;