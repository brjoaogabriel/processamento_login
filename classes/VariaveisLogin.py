class VariaveisLogin():

    def __init__(self, DatabaseObject):
        self.__dbobject = DatabaseObject;

    @property
    def getDbObject(self):
        return self.__dbobject;