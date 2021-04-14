class ConfigFromFile:
    def getConfig(self):
        configPath = "resource/Config/properties.cfg"
        propertyFile = open(configPath,"r")
        propertyData = propertyFile.read().splitlines()
        propertyFile.close()
        return propertyData
