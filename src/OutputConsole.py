from src.WriteToFile import WriteToFile

class OutputConsole:
    writeToFile = True
    outputWriteToFile = WriteToFile("userOutputLog.csv")

    def print(self,output):
        if self.writeToFile:
            self.outputWriteToFile.writeToFile(output)
        print(output)
