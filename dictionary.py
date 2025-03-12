class Dictionary:
    def __init__(self):
        self.dizionario = []

    def loadDictionary(self,file):
        """
        Carica il file di testo e aggiunge le parole alla lista dizionario
        :param file: file di testo da leggere
        :return: dizionario
        """
        with open(file, 'r', encoding='utf-8') as f:
            for riga in f:
                self.dizionario.append(riga.strip())
        return self.dizionario

    def printAll(self):
        pass


    @property
    def dict(self):
        return self._dict