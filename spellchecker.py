import time

import multiDictionary as md

multiD = md.MultiDictionary()

class SpellChecker:

    def __init__(self):
        self.paroleErrate = []
        self.paroleErrateLin = []
        self.parolaErrateDic = []
        self.time = 0
        self.timeLin = 0
        self.timeDic = 0

    def handleSentence(self, txtIn, language):
        """
        Prende la frase in input e verifica che le parole che la compongono sianno corrette, se sono
        errate le appende alla lista
        :param txtIn: str input
        :param language: str
        :return:
        """
        self.paroleErrate = []
        testo = self.replaceChars(txtIn.lower()).split()
        tic = time.time()
        for parole in testo:
            verificaParole = multiD.searchWord(parole, language)
            if verificaParole == False:
                self.paroleErrate.append(parole)
        toc = time.time()
        self.time = toc - tic

        self.paroleErrateLin = []
        ticLin = time.time()
        for parole in testo:
            verificaParoleLin = multiD.searchWordLinear(parole, language)
            if verificaParoleLin == False:
                self.paroleErrateLin.append(parole)
        tocLin = time.time()
        self.timeLin = tocLin - ticLin

        self.paroleErrateDic = []
        ticDic = time.time()
        for parole in testo:
            verificaParoleDic = multiD.searchWordDichotomic(parole, language)
            if verificaParoleDic == False:
                self.paroleErrateDic.append(parole)
        tocDic = time.time()
        self.timeDic = tocDic - ticDic

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
            if c in text:
                text = text.replace(c, "")
        return text

    def __str__(self):
        return ("______________________________\n"+"Using contains\n"+"\n".join(self.paroleErrate)+
                f"\nTime elapsed {self.time}"+"\n______________________________\nUsing Linear search\n"+
                "\n".join(self.paroleErrateLin)+f"\nTime elapsed {self.timeLin}"+"\n_____________________________\n"+
                "Using Dichotomic search\n"+"\n".join(self.paroleErrateDic)+f"\nTime elapsed {self.timeDic}"+
                "\n_____________________________\n")