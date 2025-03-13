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
        La funzione verifica che la parola sia presente nel dizionario della sua lingua con il metodo contains
        :param words: str
        :param language: str
        :return: True se la parola è presente nel dizionario, False altrimenti
        """
        parola = rw.RichWord(words)
        if language == "english":
            diz = self.dizEng
        if language == "spanish":
            diz = self.dizEsp
        if language == "italian":
            diz = self.dizIta

        if diz.__contains__(words):
            parola.corretta = True
        return parola.corretta

    def searchWordLinear(self, words, language):
        """
        Il metodo scorre il dizionario fino a quando non trova la parola o, se non la trova, fino all'ultima parola
        :param words: str
        :param language: str
        :return: True se la parola è presente nel dizionario, False altrimenti
        """
        parola = rw.RichWord(words)
        if language == "english":
            diz = self.dizEng
        if language == "spanish":
            diz = self.dizEsp
        if language == "italian":
            diz = self.dizIta

        for word in diz:
            if word == words:
                parola.corretta = True
        return parola.corretta


    def searchWordDichotomic(self, words, language):
        """
        Il metodo fa una ricerca dicotomica sul dizionario
        :param words: str
        :param language: str
        :return: True se la parola è presente nel dizionario, False altrimenti
        """
        parola = rw.RichWord(words)
        if language == "english":
            diz = self.dizEng
        if language == "spanish":
            diz = self.dizEsp
        if language == "italian":
            diz = self.dizIta

        inizio = 0
        fine = len(diz)-1
        while inizio <= fine:
            mid = (inizio+fine)//2
            if diz[mid] == words:
                parola.corretta = True
                break
            elif diz[mid]<words:
                inizio = mid+1
            elif diz[mid]>words:
                fine = mid-1
        return parola.corretta



