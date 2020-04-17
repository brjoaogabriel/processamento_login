import pymysql
import pymysql.cursors

class Database(pymysql.cursors):

    def __init__(self, porta, host, user, password, database, enconding="utf8mb4"):
        self.__porta = porta;
        self.__host = host;
        self.__user = user;
        self.__password = password;
        self.__database = database;
        self.__enconding = enconding;
        self.__cursorclass = pymysql.cursors.DictCursor;
        self.__conexao = None;
        self.__cursor = None;

    @property
    def getPorta(self):
        return self.__porta;

    @property
    def getHost(self):
        return self.__host;

    @property
    def getUser(self):
        return self.__user;

    @property
    def getPassword(self):
        return self.__password;

    @property
    def getDatabase(self):
        return self.__database;

    @property
    def getEnconding(self):
        return self.__enconding;

    @property
    def getCursorClass(self):
        return self.__cursorclass;

    @property
    def getConexao(self):
        return self.__conexao;

    @property
    def getCursor(self):
        return self.__cursor;

    @setPorta.setter
    def setPorta(self, porta):
        self.__porta = porta;

    @setHost.setter
    def setHost(self, host):
        self.__host = host;

    @setUser.setter
    def setUser(self, user):
        self.__user = user;

    @setPassword.setter
    def setPassword(self, password):
        self.__password = password;

    @setDatabase.setter
    def setDatabase(self, database):
        self.__database = database;

    @setEnconding.setter
    def setEnconding(self, enconding):
        self.__enconding = enconding;

    @setConexao.setter
    def setConexao(self, conexao):
        self.__conexao = conexao;

    @setCursor.setter
    def setCursor(self, cursor):
        self.__cursor = cursor;

    #Todos esses podem ser iguais e sua funcionalidade pode ser dividida dentro do python
    def ExisteRegistro(self, NomeTabela, Campo, Parametro):

    def BuscaRegistro(self, NomeTabela, Campo, Parametro):

    def ContaRegistro(self, NomeTabela, Campo, Parametro):

    def ConectarBase(self):
        self.setConexao = pymysql.connect(
            port=self.getPorta,
            host=self.getHost,
            user=self.getUser,
            password=self.getPassword,
            db=self.getDatabase,
            charset=self.getEnconding,
            cursorclass=self.getCursorClass
        );

    def DesconectarBase(self):
        self.setConexao.close;
        self.setConexao = None;

    def ConectarCursor(self):
        self.setCursor = self.getConexao.cursor

    def DesconectarCursor(self):
        self.setCursor.close();
        self.setCursor = None;

    def ExisteRegistro(self, ParametroBusca, NomeTabela, NomeCampo, Exato=True):
        self.ConectarBase();
        self.ConectarCursor();

        if Exato == True:
            self.getCursor.execute(f"SELECT * FROM {NomeTabela} WHERE {NomeCampo} = {ParametroBusca}");
        else:
            self.getCursor.execute(f"SELECT * FROM {NomeTabela} WHERE {NomeCampo} LIKE '%{ParametroBusca}%'");



        self.DesconectarCursor();
        self.DesconectarBase()

    def BuscaRegistro(self, ParametroBusca, NomeTabela, NomeCampo, Retorna="Registros", Exato=True):
        self.ConectarBase();
        self.ConectarCursor();

        if Exato == True:
                self.getCursor.execute(f"SELECT * FROM {NomeTabela} WHERE {NomeCampo} = {ParametroBusca}");
            else:
                self.getCursor.execute(f"SELECT * FROM {NomeTabela} WHERE {NomeCampo} LIKE '%{ParametroBusca}%'");

        if Retorna == "Registros":
            return self.getCursor.fetchall();

        elif Retorna == "Existencia":
            if len(self.getCursor.fetchall()) > 0:
                return True;
            else:
                return False;

        elif Retorna == "Quantidade":
            return len(self.getCursor.fetchall());

        self.DesconectarCursor();
        self.DesconectarBase()