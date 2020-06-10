import json
from MYloggingSystem import loggingSystem

class MYjson:
    def __init__(self, loggin_name="jsonManager", log_file="./jsonManager.log"):
        """
        classe para gerenciar arquivos json
        :param loggin_name: nome do log que foi definido para a classe,altere apenas em caso seja necessário criar multiplas insstancias da função
        :param log_file: nome do arquivo de log que foi definido para a classe,altere apenas em caso seja necessário criar multiplas insstancias da função
        """
        self.logging = loggingSystem(loggin_name, arquivo=log_file)

    def saveFile(self, arrayToSave, arquivo, advanced_debug=False):
        """
        função para salvar arquivos de tipo json
        :param arrayToSave: array de tipo dictionary para ser salvo no arquivo
        :param arquivo: nome do arquivo a ser acessadonome do arquivo onde será salvo
        :param advanced_debug: ativa o sistema de logging se definido para True
        :return:
        """
        with open(arquivo, 'w+') as file:
            if advanced_debug:
                self.logging.debug("salvo dado no arquivo:" + str(arquivo))
            for elemento in arrayToSave:
                file.write(json.dumps(elemento) + "\n")
            file.flush()
            file.close()

    def readFile(self, arquivo, advanced_debug=False):
        """
        :param arquivo: nome do arquivo a ser acessado
        :param advanced_debug: ativa o sistema de logging se definido para True
        :return: dictionary gerado a partir do arquivo lido
        """
        retorno = []
        with open(arquivo, 'r') as file:
            if advanced_debug:
                self.logging.debug("lido dado no arquivo:" + str(arquivo))
            linha = file.readline()
            while (linha != ""):
                retorno.append(json.loads(linha))
                linha = file.readline()
            file.close()
        return retorno

    def search(self,dictionary:dict,campo,valor):
        return next(item for item in dictionary if item[campo] == valor)