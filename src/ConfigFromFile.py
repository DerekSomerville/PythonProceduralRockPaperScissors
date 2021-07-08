import os

def fixWorkingDirectory():
    currentWorkingDirectory = os.getcwd()
    while "test" in currentWorkingDirectory or "src" in currentWorkingDirectory:
        os.chdir("../")
        currentWorkingDirectory = os.getcwd()

def getConfig():
    fixWorkingDirectory()
    configPath = "resource/Config/properties.cfg"
    propertyFile = open(configPath,"r")
    propertyData = propertyFile.read().splitlines()
    propertyFile.close()
    return propertyData
