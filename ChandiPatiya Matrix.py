# COLORAMA STUFF
import colorama
from colorama import Back, Fore, Style

colorama.init(autoreset=True)

from MatrixPro import HariMatrix
from napolita import Napolita
from lin2 import bongoAnalyser

from HomoMatrix import DHRow


running = True


def printColorfulBack(string, steady=False):
    colors = [Back.LIGHTCYAN_EX,Back.LIGHTCYAN_EX, Back.LIGHTMAGENTA_EX ,Back.LIGHTMAGENTA_EX, Back.LIGHTGREEN_EX, Back.LIGHTGREEN_EX, Back.LIGHTYELLOW_EX, Back.LIGHTYELLOW_EX, Back.LIGHTRED_EX, Back.LIGHTRED_EX]
    text = ''
    reduced = 0
    if not steady:
        for i in range(len(string)):
            if string[i] == ' ':
                reduced += 1
                text += Back.BLACK + ' '
                continue
            text += Style.BRIGHT + Fore.BLACK + colors[(i - reduced) % len(colors)] + string[i]

    else:
        for i in range(len(string)):
            text += Fore.BLACK + colors[(i - reduced) % len(colors)] + string[i]
    print(text)


def printColorful(string, steady=False):
    colors = [Fore.LIGHTCYAN_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTRED_EX]
    text = ''
    reduced = 0
    if not steady:
        for i in range(len(string)):
            if string[i] == ' ':
                reduced += 1
                text += ' '
                continue
            text += colors[(i - reduced) % len(colors)] + string[i]
    else:
        for i in range(len(string)):
            text += colors[(i - reduced) % len(colors)] + string[i]
    print(text)


printColorfulBack("ChandiPatiya Matrix Helper (Edition 1.7)", True)
printColorfulBack("  Type help for more information ENJOY   ", True)

cin = ''
matrixGroup = {}


def makeMatrix(newName):
    matrix = []
    print(f'{Fore.LIGHTBLUE_EX}~Rows$ ', end='')
    rows = int(input())
    print(f'{Fore.LIGHTBLUE_EX}~Cols$ ', end='')
    cols = int(input())
    for i in range(rows):
        singleArray = []
        for j in range(cols):
            print(f"{Fore.LIGHTYELLOW_EX}~Value for ({i + 1} {j + 1})$ ", end='')
            singleArray.append(input())
        matrix.append(singleArray)
    matrixGroup[newName] = HariMatrix(matrix)


def makeMatrix2(newName):
    printRose("~ No of Rows$ ", '')
    rows = int(input())
    matrix = []
    for i in range(rows):
        printYellow(f'~ Row {i+1} $ ', '')
        matrix.append(input().split())
    matrixGroup[newName] = HariMatrix(matrix)


def printCyan(string):
    print(f"{Fore.LIGHTCYAN_EX}{string}")


def printRed(string):
    print(f"{Fore.LIGHTRED_EX}{string}")


def printGreen(string):
    print(f"{Fore.LIGHTGREEN_EX}{string}")


def printRose(string, last='\n'):
    print(f"{Fore.LIGHTMAGENTA_EX}{string}", end=last)


def printYellow(string, last='\n'):
    print(f"{Fore.LIGHTYELLOW_EX}{string}", end=last)


def printGrey(string):
    print(f"{Fore.LIGHTBLACK_EX}{string}")


def getDet(parent):
    if type(parent) == str:
        parent = matrixGroup.get(parent)
    return parent.getDeterminant()


def getInverse(parent):
    if type(parent) == str:
        parent = matrixGroup.get(parent)
    return parent.inverse()


def getAdjoin(parent):
    if type(parent) == str:
        parent = matrixGroup.get(parent)
    return parent.adjoin()


def getRe(parent):
    if type(parent) == str:
        parent = matrixGroup.get(parent)
    return parent.getRowEchelon()


def getRre(parent):
    if type(parent) == str:
        parent = matrixGroup.get(parent)
    return parent.getReducedRowEchelon()

def transpose(parent):
    if type(parent) == str:
        parent = matrixGroup.get(parent)
    return parent.transpose()

def clRow(parent):
    print('~ Enter the Row No $ ', end='')
    row = int(input())
    matrixGroup[parent].clearRow(row-1)

def clColumn(parent):
    print('~ Enter the Column No $ ', end='')
    col = int(input())
    matrixGroup[parent].clearColumn(col-1)

def addRow(parent):
    print('~ Enter the ROW Elements $ ', end='')
    data = input().split()
    print('~ How many times $ ', end='')
    times = int(input())
    matrixGroup[parent].rowSpan(times, *data)

def addColumn(parent):
    print('~ Enter the COLUMN Elements $ ', end='')
    data = input().split()
    print('~ How many times $ ', end='')
    times = int(input())
    matrixGroup[parent].colSpan(times, *data)

def rowExchange(parent):
    print('~ Enter the Rows $ ', end='')
    rows = [int(x)-1 for x in input().split()]
    matrixGroup[parent].rowExchange(*rows)

def colExchange(parent):
    print('~ Enter the Columns $ ', end='')
    cols = [int(x)-1 for x in input().split()]
    matrixGroup[parent].colExchange(*cols)


def getDH(parent):
    if len(matrixGroup.get(parent).matrix) == 1:
        dhRow = DHRow(*(matrixGroup.get(parent).getMatrixFloats(2)[0]))
        print(dhRow.getHomoMatrix(3))
    else:
        out = DHRow(*(matrixGroup.get(parent).getMatrixFloats(2)[0]))
        for i in range(1, len(matrixGroup.get(parent).matrix)):
            print(matrixGroup.get(parent).getMatrixFloats(2)[i])
            out = out * DHRow(*(matrixGroup.get(parent).getMatrixFloats(2)[i]))
        print(out.getBeautyStringProFraction(3))


def deleteItem(parent):
    if parent in matrixGroup:
        del matrixGroup[parent]


def getAll():
    for i in matrixGroup:
        print(f"{Fore.LIGHTMAGENTA_EX}{i}:\n{matrixGroup[i].getBeautyStringPro()}\n")


def editItem(parent):
    if parent in matrixGroup:
        print(f"{Fore.LIGHTBLUE_EX}~Rows$ ", end='')
        rows = int(input())
        print(f"{Fore.LIGHTBLUE_EX}~Cols$ ", end='')
        cols = int(input())
        print(f"{Fore.LIGHTBLUE_EX}~Value$ ", end='')
        value = input()
        matrixGroup[parent].enterElement(rows - 1, cols - 1, value)


def help():
    answer = """
    Assign your Matrix into a Single Word
    Define your Matrix using the new keyword

    Function Introduction

    new : ~ matrix.new
          ~Rows$ 2
          ~Cols$ 2
          ~Value for (1 1)$ 3
          ~Value for (1 2)$ 4.2
          ~Value for (2 1)$ 5/2
          ~Value for (2 2)$ 6

    adjoin: ~ matrix.adjoin

    inverse : ~ matrix.inverse

    rowEchelon : ~ matrix.re

    reducedRowEchelon : ~ matrix.rre

    edit:  ~ matrix.edit

    -----------------------------------------------------

    You can get the stored matrices by using their name
    you assingned them with

    ~ matrix


    -----------------------------------------------------

    You can use add, sub and multiply functions
    for two matrices that fulfills the mathematical needs

    ~ new.firstMatrix
    ~ .........
    ~ .........
    ~ new.secondMatrix
    ~ .........
    ~ .........

    ~ firstMatrix + secondMatrix

    ----------------------------------------------------

    Instead of Taking the results to the Terminal
    You are allowed to assign them in a variable

    ~ matrix.new
    ~ ...........
    ~ inverseOfMatrix = matrix.inverse

    ~ result = matrix * inverseOfMatrix

    ---------------------------------------------------

    Chained Function calling Available

    ~ matrix.inverse.adjoin.inverse
    ~ secondMatrix = matrix.inverse.adjoin.inverse

    ---------------------------------------------------

    Other Features
    ~ matrix.del
    ~ help
    ~ exit
    ~ all
    ~ about
    """
    printCyan(answer)


def about():
    answer = """
   Developed and maintained by ChandiPatiya Software Solutions
   ChandiPatiya Matrix Helper (Edition 1.70)
   bimsara.hari@gmail.com
   Free Software
    """
    printRose(answer)


def exit():
    global running
    print(f"{Fore.LIGHTCYAN_EX}~Thank you for using me Press Enter to EXIT")
    input()
    running = False

def equation():
    printCyan("Enter Equations")
    linearEquationList = []
    line = ''
    while True:
        print('~ ', end='')
        line = input().replace(' ', '')
        linearEquationList.append(line)
        if line.replace(' ', '') == '':
            linearEquationList.remove(linearEquationList[-1])
            break
    printGreen(bongoAnalyser(*linearEquationList))
    print('~')
    print('~')


'''def editCommand():
    printRose('~ Curernt Command Name $ ', '')
    command = fullTrim(input())
    printRose('~ New Command Name     $ ')
    newCommand = fullTrim(input())
    if command in commandDictionary:
        commandDictionary[newCommand] = commandDictionary.get(command)
        del commandDictionary[command]
    elif command in singleCommandDictionary:
        singleCommandDictionary[newCommand] = singleCommandDictionary.get(command)
        del singleCommandDictionary[command]
'''

def equal(fullCommand):
    print("yoloo")
    if '+' not in fullCommand and '-' not in fullCommand and '*' not in fullCommand:
        matrixGroup[fullTrim((fullCommand.split('=')[0]))] = commandDictionary[
            fullCommand.split('=')[1].split()[0] + 'R'](fullCommand.split('=')[1])
    elif '+' in fullCommand:
        matrixGroup[fullTrim((fullCommand.split('=')[0]))] = add(fullTrim(fullCommand.split('=')[-1]))
    elif '-' in fullCommand:
        matrixGroup[fullTrim((fullCommand.split('=')[0]))] = sub(fullTrim(fullCommand.split('=')[-1]))
    elif '*' in fullCommand:
        matrixGroup[fullTrim((fullCommand.split('=')[0]))] = mul(fullTrim(fullCommand.split('=')[-1]))


def add(fullCommand, string=False):
    if string:
        return (matrixGroup[fullTrim(fullCommand.split('+')[0])] + matrixGroup[
            fullTrim(fullCommand.split('+')[-1])]).getBeautyStringPro()
    return matrixGroup[fullTrim(fullCommand.split('+')[0])] + matrixGroup[fullTrim(fullCommand.split('+')[-1])]


def sub(fullCommand, string=False):
    if string:
        return (matrixGroup[fullTrim(fullCommand.split('-')[0])] - matrixGroup[
            fullTrim(fullCommand.split('-')[-1])]).getBeautyStringPro()
    return matrixGroup[fullTrim(fullCommand.split('-')[0])] + matrixGroup[fullTrim(fullCommand.split('-')[-1])]


def mul(fullCommand, string=False):
    if string:
        return (matrixGroup[fullTrim(fullCommand.split('*')[0])] * matrixGroup[
            fullTrim(fullCommand.split('*')[-1])]).getBeautyStringPro()
    return matrixGroup[fullTrim(fullCommand.split('*')[0])] * matrixGroup[fullTrim(fullCommand.split('*')[-1])]


def fullTrim(string):
    return string.replace(' ', '')





commandDictionary = {
    '=': equal,
    '+': add,
    '-': sub,
    '*': mul,

    'new2': makeMatrix,
    'new': makeMatrix2,
    'det': getDet,
    'adj': getAdjoin,
    'inv': getInverse,
    're': getRe,
    'rre': getRre,
    'del': deleteItem,
    'edit': editItem,
    'tra' : transpose,
    'clr': clRow,
    'clc': clColumn,
    'addr': addRow,
    'addc': addColumn,
    'rex': rowExchange,
    'cex': colExchange,
    'dh': getDH
}

singleCommandDictionary = {
    'all': getAll,
    'help': help,
    'exit': exit,
    'about': about,
    'eq': equation
}


def seperator(fullCommand):
    halfCommand = fullCommand.split('=')[-1]
    if len([i for i in ('+', '-', '/', '*') if i in halfCommand]) == 0:
        seperatedCommand = [i for i in halfCommand.split('.') if i]
        result = seperatedCommand[0]
        for i in range(1, len(seperatedCommand)):
            if i == 1:
                result = commandDictionary.get(seperatedCommand[i].lower())(result)
            else:
                result = commandDictionary.get(seperatedCommand[i])(result)
        if '=' not in fullCommand:
            if result:
                if type(result) == HariMatrix:
                    printGreen(result.getBeautyStringPro())
                elif type(result) == Napolita:
                    printGreen(HariMatrix([[result.get()]]).getBeautyStringPro())
        elif '=' in fullCommand:
            matrixGroup[fullCommand.split('=')[0]] = result

    else:
        if '=' in cin:
            equal(cin)

        else:
            command = [i for i in ('+', '-', '/', '*') if i in cin]
            print(commandDictionary.get(command[0])(cin, True))
##########################################################


while running:
    #try:
    print(f"{Fore.LIGHTRED_EX}~ ", end='')
    cin = fullTrim(input())
    if not cin:
        continue

    elif cin in matrixGroup:
        print(f'{Fore.LIGHTBLACK_EX}{matrixGroup[cin].getBeautyStringPro()}')

    elif cin.lower() in singleCommandDictionary:

        temp = singleCommandDictionary.get(cin.lower())()
        if temp:
            print(temp)
    else:
        seperator(cin)

    #except:
        #printRed('~ Programme Temporarily Crashed Keep going')
        #continue
