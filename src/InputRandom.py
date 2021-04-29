from random import randint
import src.WriteToFile
import src.InputConsole

writeToFile = True

def getInputString( request):
    return getInputInt()

def getInputInt(request):
    rand = randint(0, 2)
    if writeToFile:
        fileWritter = src.InputConsole.fileWritter
        src.WriteToFile.writeToFile(fileWritter, rand)
    return rand
