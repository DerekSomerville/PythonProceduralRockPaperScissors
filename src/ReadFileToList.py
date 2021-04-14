filePath = "resource/log/"

def getFileRows(fileName):
    file = open(filePath + fileName, "r")
    fileRows = file.read().splitlines()
    file.close()
    return fileRows

def getList(fileName):
    fileRows = getFileRows(fileName)
    fileList = []
    for fileRow in fileRows:
        if len(fileRow) > 0:
            fileList.append(fileRow)
    return fileList
