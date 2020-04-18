class VariaveisLogin():

    def __init__(self, DatabaseObject):
        self.__dbobject = DatabaseObject;

    @property
    def getDbObject(self):
        return self.__dbobject;

    @getDbObject.setter
    def setDbObject(self, DatabaseObject):
        self.__dbobject = DatabaseObject;