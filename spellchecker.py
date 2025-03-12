import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        pass

    def handleSentence(self, txtIn, language):
        pass

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


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        if text.contains(c):
            text = text.replace(c, "")
    return text