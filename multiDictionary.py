import dictionary as d
import richWord as rw

dizionari = d.Dictionary()
class MultiDictionary:

    def __init__(self):
        dizIta = dizionari.loadDictionary("Italian.txt")
        dizEng = dizionari.loadDictionary("English")
        dizEsp = dizionari.loadDictionary("Spanish")

    def printDic(self, language):
        pass

    def searchWord(self, words, language):
        pass


