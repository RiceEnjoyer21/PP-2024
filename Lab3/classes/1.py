class Sturingo:
    def __init__(self):
        self.a = ""

    def getString(self):
        self.a = input()

    def printString(self):
        print(self.a)
        print(self.a.upper())

bebriki = Sturingo()

bebriki.getString()
bebriki.printString()
