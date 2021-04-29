import unittest
from unittest.mock import MagicMock
import src.ConfigFromFile
import src.InputTest
import src.OutputTest
from src.ReadFileToList import *
from src.RockPaperScissors import *

class RockTest(unittest.TestCase):

    def test_determinWinnerRockRock(self):
        result = determineWinner(0,0)
        self.assertEqual("Draw", result)

    def test_GenerateGamesRequestStub(self):
        setTestFile(True)
        result = generateGamesListRequest();
        self.assertEqual("Please select 0 - Rock Paper Scissors 1 - Star Wars", result)

    def test_getListOfGamesMock(self):
        propertyData = []
        propertyData.append("Name,First,Second,Third")
        propertyData.append("Rock Paper Scissors:Rock,Scissors,Paper")
        propertyData.append("Star War:Darth Vadar,Emperor,Luke Skywalker")
        property = []
        setTestFile(False)
        src.ConfigFromFile.getConfig = MagicMock(return_value=propertyData)
        result = getListOfGames();
        self.assertEqual(['Rock Paper Scissors', 'Star War'], result)


    def testRockVersusRock(self):
        setTestFile(True)
        setTestInput(True)
        src.InputTest.inputList = [0,0,0,4]
        play()
        result = src.OutputTest.outputlist.pop(-1)
        self.assertEqual(result,"Draw")

    def testReplay(self):
        setTestFile(False)
        setTestInput(True)
        src.InputTest.inputList = getList("userInputLog.csv")
        fileOutput = getList("userOutputLog.csv")
        play()
        self.assertEqual(src.OutputTest.outputlist,fileOutput)

    def testPropertyMoreThanOne(self):
        setTestFile(False)
        propertyData = getConfig()
        self.assertTrue(len(propertyData) >= 1)

    def testAtLeastOneGame(self):
        self.assertTrue(len(getListOfGames()) >= 1)


def main():
    unittest.main()

if __name__ == "__main__":
    unittest.main()
