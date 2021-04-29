import src.WriteToFile

writeToFile = True
fileWritter = None

def getInputString( request):
    userInput = input(request)
    if writeToFile:
        global fileWritter
        if fileWritter == None:
            fileWritter = src.WriteToFile.getFileReader("userInputLog.csv")
        src.WriteToFile.writeToFile(fileWritter,userInput)
    return userInput

def getInputInt( request):
    response = getInputString(request)
    while not str(response).isnumeric():
        response = getInputString("Please enter an integer")
    return int(response)