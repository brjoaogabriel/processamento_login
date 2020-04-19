from application.terminal import *

class VariaveisLogin():

    def __init__(self, DatabaseObject):
        self.__dbobject = DatabaseObject;

    @property
    def getDbObject(self):
        return self.__dbobject;

    def printar_log(self, parametros):
        for i in range(0, len(parametros['nome']), 1):
            if parametros['nome'] == False:
                #print(f"- {RED}{parametros['resultado'][i]}{RESET} -       {parametros['nome'][i]}...");
                print("-" + RED + f"{parametros['resultado'][i]}" + RESET + f" - {parametros['nome'][i]}...");
            else:
                #print(f"- {BLUE}{parametros['resultado'][i]}{RESET}-       {parametros['nome'][i]}...");
                print("-" + GREEN + f"{parametros['resultado'][i]}" + RESET + f" - {parametros['nome'][i]}...");