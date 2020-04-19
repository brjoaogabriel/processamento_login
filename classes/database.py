import pymysql
import pymysql.cursors

class Database(pymysql.connections.Connection, pymysql.cursors.Cursor):

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

    @getPorta.setter
    def setPorta(self, porta):
        self.__porta = porta;

    @getHost.setter
    def setHost(self, host):
        self.__host = host;

    @getUser.setter
    def setUser(self, user):
        self.__user = user;

    @getPassword.setter
    def setPassword(self, password):
        self.__password = password;

    @getDatabase.setter
    def setDatabase(self, database):
        self.__database = database;

    @getEnconding.setter
    def setEnconding(self, enconding):
        self.__enconding = enconding;

    @getConexao.setter
    def setConexao(self, conexao):
        self.__conexao = conexao;

    @getCursor.setter
    def setCursor(self, cursor):
        self.__cursor = cursor;

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
        self.setCursor = self.getConexao.cursor()

    def DesconectarCursor(self):
        self.getCursor.close;
        self.setCursor = None;

    def BuscaRegistro(self, ParametroBusca, NomeTabela, NomeCampo, Retorna="Registros", Exato=True):
        self.ConectarBase();
        self.ConectarCursor();

        if Exato == True:
            sql = f"""SELECT * FROM {NomeTabela} WHERE {NomeCampo} = '{ParametroBusca}'""";
            self.getCursor.execute(sql);
            sql = None;
        else:
            sql = f"""SELECT * FROM {NomeTabela} WHERE {NomeCampo} LIKE '%{ParametroBusca}%'""";
            self.getCursor.execute(sql);
            sql = None;

        if Retorna == "Registros":
            return self.getCursor.fetchall();

        elif Retorna == "Existencia":
            if self.getCursor.rowcount > 0:
                return True;
            else:
                return False;

        elif Retorna == "Quantidade":
            return self.getCursor.rowcount;

        self.DesconectarCursor();
        self.DesconectarBase()

    def Valida_Senha(self, login, senha):
        Validado: bool;

        self.ConectarBase();
        self.ConectarCursor();

        sql = f"SELECT desc_login, desc_senha FROM user_info WHERE desc_login = '{login}' and desc_senha = '{senha}' LIMIT 1"
        self.getCursor.execute(sql);

        Validado = self.getCursor.rowcount > 0;

        self.DesconectarCursor()
        self.DesconectarBase()

        return Validado;




