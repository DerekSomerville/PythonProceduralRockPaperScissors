import src.WriteToFile

writeToFile = True
fileWritter = None

def printMessage(output):
    if writeToFile:
        global fileWritter
        if fileWritter == None:
            fileWritter = src.WriteToFile.getFileReader("userOutputLog.csv")
        src.WriteToFile.writeToFile(fileWritter, output)
    print(output)
