class InputTest:

    inputList = []

    def getInputString(self,request):
        return self.inputList.pop(0)

    def getInputInt(self, request):
        response = self.getInputString("Please enter an integer")
        return int(response)

    def setInputList(self,inputList):
        self.inputList = inputList
