
# Here will be the instance stored.

def getFileReader(fileName):
    fileWritter = open("resource/" + "log/" + fileName, "w")
    return fileWritter

def writeToFile(fileWritter,logItem):
   fileWritter.write(str(logItem) + "\n")
