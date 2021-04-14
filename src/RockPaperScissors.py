from random import randint
from src.InputConsole import InputConsole
from src.OutputConsole import OutputConsole
from src.ConfigFromFile import ConfigFromFile
from src.InputRandom import InputRandom


userInput = InputConsole()
userOutput = OutputConsole()
computerInput = InputRandom()
configProvider = ConfigFromFile()
property = []

def setUserInput(NewUserInput):
    global userInput
    userInput = NewUserInput

def setComputerInput(newComputerInput):
    global computerInput
    computerInput = newComputerInput

def setUserOutput (newUserOutput):
    global userOutput
    userOutput = newUserOutput

def setConfig(newConfig):
    global configProvider
    configProvider = newConfig

def determineWinner(player,computer):
    if player == computer:
        result = "Draw"
    elif (player + 1)%3 == computer:
        result = "Player wins"
    elif (computer + 1)%3 == player:
        result = "Computer Wins"
    return result

def getUserChoiceRequest(weapons):
    request = "Select "
    for counter in range(len(weapons)):
        request += str(counter) + " for " + weapons[counter] + " "
    return request

def getUserChoice(weapons):
    request = getUserChoiceRequest(weapons)
    player = userInput.getInputInt(request)
    if player in [0,1,2]:
        userOutput.print("You selected " + weapons[player])
    return player

def getComputerChoice( weapons):
    chosen = computerInput.getInputInt("")
    userOutput.print("Computer choose " + weapons[chosen])
    return chosen

def getListOfGames():
    property = configProvider.getConfig()
    listOfGames = []
    for counter in range(1,len(property)):
        listOfGames.append(property[counter].split(":")[0])
    return listOfGames

def getWeaponLists():
    property = configProvider.getConfig()
    weaponLists = []
    for counter in range(1,len(property)):
        weaponLists.append(property[counter].split(":")[1].split(","))
    return weaponLists

def getGamesRequest(listOfGames):
    request = "Please select"
    for counter in range(len(listOfGames)):
        request += " " + str(counter) + " - " + listOfGames[counter]
    return request

def generateGamesListRequest():
    listOfGames = getListOfGames()
    request = getGamesRequest(listOfGames)
    return request

def getGame():
    request = generateGamesListRequest()
    userGame = userInput.getInputInt(request)
    weaponsLists = getWeaponLists()
    return weaponsLists[userGame]

def play():
    weapon = getGame()
    player = getUserChoice(weapon)
    while player in [0,1,2]:
        computer = getComputerChoice(weapon)
        result = determineWinner(player,computer)
        userOutput.print(result)
        player = getUserChoice(weapon)

def main():
    play()

if __name__ == "__main__":
    main()




