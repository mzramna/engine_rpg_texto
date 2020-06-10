import logging

class loggingSystem:
    def __init__(self, name, arquivo='./arquivo.log', format='%(name)s - %(levelname)s - %(message)s',
                 level=logging.DEBUG):
        """
        :param name: nome do log a ser escrito no arquivo
        :param arquivo: nome do arquivo a ser utilizado
        :param format: formato do texto a ser inserido no output do log
        :param level: nivel de log padrão de saida
        """
        formatter = logging.Formatter(format)
        handler = logging.FileHandler(arquivo)
        handler.setFormatter(formatter)
        f = open(arquivo, "w+")
        f.write("")
        f.close()
        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler)
        self.debug = logger.debug
        self.warning = logger.warning
        self.error = logger.error
        self.info = logger.info
        self.log = logger.log
        self.critical = logger.critical
        self.setlevel = logger.setLevel
        self.fatal = logger.fatal
