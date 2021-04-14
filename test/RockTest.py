import unittest
from unittest.mock import MagicMock
from src.ConfigFromStub import ConfigFromStub
from src.ConfigFromFile import ConfigFromFile

from src.InputTest import InputTest
from src.OutputTest import OutputTest
from src.ReadFileToList import *
from src.RockPaperScissors import *

class RockTest(unittest.TestCase):

    def test_determinWinnerRockRock(self):
        result = determineWinner(0,0)
        self.assertEqual("Draw", result)

    def test_GenerateGamesRequestStub(self):
        setConfig(ConfigFromStub())
        result = generateGamesListRequest();
        self.assertEqual("Please select 0 - Rock Paper Scissors 1 - Star Wars", result)

    def test_getListOfGamesMock(self):
        propertyData = []
        propertyData.append("Name,First,Second,Third")
        propertyData.append("Rock Paper Scissors:Rock,Scissors,Paper")
        propertyData.append("Star War:Darth Vadar,Emperor,Luke Skywalker")
        property = []
        configProvider = ConfigFromFile()
        configProvider.getConfig = MagicMock(return_value=propertyData)
        setConfig(configProvider)
        result = getListOfGames();
        self.assertEqual(['Rock Paper Scissors', 'Star War'], result)

    def getUserInput(self,inputs):
        userInput = InputTest()
        userInput.inputList = inputs
        return userInput

    def testRockVersusRock(self):
        setConfig(ConfigFromStub())
        userOutput = OutputTest()
        setUserOutput(userOutput)
        setUserInput(self.getUserInput([0,0,4]))
        setComputerInput(self.getUserInput([0]))
        play()
        result = userOutput.outputlist.pop(-1)
        self.assertEqual(result,"Draw")

    def testReplay(self):
        setConfig(ConfigFromFile())
        setUserInput(self.getUserInput(getList("userInputLog.csv")))
        setComputerInput(self.getUserInput(getList("computerInputLog.csv")))
        fileOutput = getList("userOutputLog.csv")
        userOutput = OutputTest()
        setUserOutput(userOutput)
        play()
        self.assertEqual(userOutput.outputlist,fileOutput)

    def testPropertyMoreThanOne(self):
        config = ConfigFromFile()
        propertyData = config.getConfig()
        self.assertTrue(len(propertyData) >= 1)

    def testAtLeastOneGame(self):
        self.assertTrue(len(getListOfGames()) >= 1)


def main():
    unittest.main()

if __name__ == "__main__":
    unittest.main()
