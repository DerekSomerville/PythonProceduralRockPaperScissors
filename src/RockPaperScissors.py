import src.InputConsole
import src.InputTest
import src.OutputConsole
import src.OutputTest
import src.ConfigFromFile
import src.ConfigFromStub
import src.InputRandom

testFile = False
testInput = False

def setTestFile(testing):
    global testFile
    testFile = testing

def setTestInput(testing):
    global testInput
    testInput = testing

def getConfig():
    result = None
    global testFile
    if testFile:
        result = src.ConfigFromStub.getConfig()
    else:
        result = src.ConfigFromFile.getConfig()

    return result

def printMessage(message):
    global testInput
    if testInput:
        src.OutputTest.printMessage(message)
    else:
        src.OutputConsole.printMessage(message)

def userInput(request):
    result = None
    global testInput
    if testInput:
        result = src.InputTest.getInputInt(request)
    else:
        result = src.InputConsole.getInputInt(request)
    return result

def computerInput(request):
    result = None
    global testInput
    if testInput:
        result = src.InputTest.getInputInt(request)
    else:
        result = src.InputRandom.getInputInt(request)
    return result

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
    player = userInput(request)
    if player in [0,1,2]:
        printMessage("You selected " + weapons[player])
    return player

def getComputerChoice( weapons):
    chosen = computerInput("")
    printMessage("Computer choose " + weapons[chosen])
    return chosen

def getListOfGames():
    property = getConfig()
    listOfGames = []
    for counter in range(1,len(property)):
        listOfGames.append(property[counter].split(":")[0])
    return listOfGames

def getWeaponLists():
    property = getConfig()
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
    userGame = userInput(request)
    weaponsLists = getWeaponLists()
    return weaponsLists[userGame]

def play():
    weapon = getGame()
    player = getUserChoice(weapon)
    while player in [0,1,2]:
        computer = getComputerChoice(weapon)
        result = determineWinner(player,computer)
        printMessage(result)
        player = getUserChoice(weapon)

def main():
    play()

if __name__ == "__main__":
    main()




