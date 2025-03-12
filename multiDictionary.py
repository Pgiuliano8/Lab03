import dictionary as d
import richWord as rw
dizionari = d.Dictionary()


class MultiDictionary:

    def __init__(self):
        self.dizIta = dizionari.loadDictionary("Italian.txt")
        self.dizEng = dizionari.loadDictionary("English.txt")
        self.dizEsp = dizionari.loadDictionary("Spanish.txt")

    def printDic(self, language):
        pass

    def searchWord(self, words, language):
        """
        La funzione verifica che la parola sia presente nel dizionario della sua lingua
        :param words: str
        :param language: str
        :return: True se la parola è presente nel dizionario, None altrimenti
        """
        parola = rw.RichWord(words)
        if language == "english":
            diz = self.dizEng
        if language == "spanish":
            diz = self.dizEsp
        if language == "italian":
            diz = self.dizIta

        if diz.__contains__(parola):
            parola.corretta(True)

        return parola.corretta()


