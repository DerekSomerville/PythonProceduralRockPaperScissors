
inputList = []

def getInputString(request):
    return inputList.pop(0)

def getInputInt(request):
    response = getInputString("Please enter an integer")
    return int(response)

def setInputList(newInputList):
    global inputList
    inputList = newInputList
