from src.WriteToFile import WriteToFile

writeToFile = True
userInputWriteToFile = WriteToFile("userInputLog.csv")

class InputConsole:
    def getInputString(self, request):
        userInput = input(request)
        if writeToFile:
            userInputWriteToFile.writeToFile(userInput)
        return userInput

    def getInputInt(self, request):
        response = self.getInputString(request)
        while not str(response).isnumeric():
            response = self.getInputString("Please enter an integer")
        return int(response)