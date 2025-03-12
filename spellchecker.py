import datetime

import multiDictionary as md

multiD = md.MultiDictionary()

class SpellChecker:

    def __init__(self):
        self.paroleErrate = []
        self.time = 0

    def handleSentence(self, txtIn, language):
        """
        Prende la frase in input e verifica che le parole che la compongono sianno corrette, se sono
        errate le appende alla lista
        :param txtIn: str input
        :param language: str
        :return:
        """
        testo = self.replaceChars(txtIn.lower()).split()
        tic = datetime.datetime.now()
        for parole in testo:
            verificaParole = multiD.searchWord(parole, language)
            if verificaParole == None:
                self.paroleErrate.append(parole)
        toc = datetime.datetime.now()
        self.time = toc - tic

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


    def replaceChars(self, text):
        chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
        for c in chars:
            if text.contains(c):
                text = text.replace(c, "")
        return text

    def __str__(self):
        return (f"______________________________\n"+"Using contains\n"+"\n".join(self.paroleErrate)+"Time elapsed"+
                {self.time}+"______________________________\n")