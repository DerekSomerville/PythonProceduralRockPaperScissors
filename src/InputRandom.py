from random import randint
from src.WriteToFile import WriteToFile

class InputRandom:
    writeToFile = True
    inputWriteToFile = WriteToFile("computerInputLog.csv")

    def getInputString(self, request):
        return self.getInputInt()

    def getInputInt(self, request):
        rand = randint(0, 2)
        if self.writeToFile:
            self.inputWriteToFile.writeToFile(rand)
        return rand
