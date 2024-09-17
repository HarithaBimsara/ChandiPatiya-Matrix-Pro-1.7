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


def getDet(parent, output,accuracy="Null"):

    if not output:
        if accuracy=="Null":
            print(parent.getDeterminant().getBeautyStringPro())
        else:
            print(parent.getDeterminant().getBeautyStringProFraction(accuracy))
    else:
        return parent.getDeterminant()


def getInverse(parent, output,accuracy="Null"):
    if not output:
        if accuracy=="Null":
            print(parent.inverse().getBeautyStringPro())
        else:
            print(parent.inverse().getBeautyStringProFraction(accuracy))
    else:
        return parent.inverse()


def getAdjoin(parent, output,accuracy="Null"):
    if not output:
        if accuracy=="Null":
            print(parent.adjoin().getBeautyStringPro())
        else:
            print(parent.adjoin().getBeautyStringProFraction(accuracy))
    else:
        return parent.adjoin()



def getRe(parent, output,accuracy="Null"):
    if not output:
        if accuracy=="Null":
            print(parent.getRowEchelon().getBeautyStringPro())
        else:
            print(parent.getRowEchelon().getBeautyStringProFraction(accuracy))
    else:
        return parent.getRowEchelon()

def getRre(parent, output,accuracy="Null"):
    if not output:
        if accuracy == "Null":
            print(parent.getReducedRowEchelon().getBeautyStringPro())
        else:
            print(parent.getReducedRowEchelon().getBeautyStringProFraction(accuracy))
    else:
        return parent.getReducedRowEchelon()

def transpose(parent, output,accuracy="Null"):
    if not output:
        if accuracy=="Null":
            print(parent.transpose().getBeautyStringPro())
        else:
            print(parent.transpose().getBeautyStringProFraction(accuracy))
    else:
        return parent.transpose()

def clRow(parent, output,accuracy="Null"):
    for i in matrixGroup.keys():
        if matrixGroup[i]==parent:
            parent = i
            break
    print('~ Enter the Row No $ ', end='')
    row = int(input())
    matrixGroup[parent].clearRow(row-1)

def clColumn(parent, output,accuracy="Null"):
    for i in matrixGroup.keys():
        if matrixGroup[i]==parent:
            parent = i
            break
    print('~ Enter the Column No $ ', end='')
    col = int(input())
    matrixGroup[parent].clearColumn(col-1)

def addRow(parent, output,accuracy="Null"):
    for i in matrixGroup.keys():
        if matrixGroup[i]==parent:
            parent = i
            break
    print('~ Enter the ROW Elements $ ', end='')
    data = input().split()
    print('~ How many times $ ', end='')
    times = int(input())
    matrixGroup[parent].rowSpan(times, *data)

def addColumn(parent, output,accuracy="Null"):
    for i in matrixGroup.keys():
        if matrixGroup[i]==parent:
            parent = i
            break
    print('~ Enter the COLUMN Elements $ ', end='')
    data = input().split()
    print('~ How many times $ ', end='')
    times = int(input())
    matrixGroup[parent].colSpan(times, *data)

def rowExchange(parent, output,accuracy="Null"):
    for i in matrixGroup.keys():
        if matrixGroup[i]==parent:
            parent = i
            break
    print('~ Enter the Rows $ ', end='')
    rows = [int(x)-1 for x in input().split()]
    matrixGroup[parent].rowExchange(*rows)

def colExchange(parent, output,accuracy="Null"):
    for i in matrixGroup.keys():
        if matrixGroup[i]==parent:
            parent = i
            break
    print('~ Enter the Columns $ ', end='')
    cols = [int(x)-1 for x in input().split()]
    matrixGroup[parent].colExchange(*cols)


def getDH(parent,output, accuracy="Null", ):
    #print(parent, type(parent))
    if not output:
        if len(parent.matrix) == 1:
            dhRow = DHRow(*(parent.getMatrixFloats(accuracy)[0]))
            if accuracy=="Null":
                print(dhRow.getHomoMatrixHari().getBeautyStringPro())
            else:
                print(dhRow.getHomoMatrixHari().getBeautyStringProFraction(accuracy))
        else:
            out = (DHRow(*(parent.getMatrixFloats(accuracy)[0]))).getHomoMatrixHari()
            for i in range(1, len(parent.matrix)):
                #print(matrixGroup.get(parent).getMatrixFloats(2)[i])
                out = (out * (DHRow(*(parent.getMatrixFloats(accuracy)[i]))).getHomoMatrixHari())
            if accuracy=="Null":
                print(out.getBeautyStringPro())
            else:
                print(out.getBeautyStringProFraction(accuracy))
    else:
        if len(parent.matrix) == 1:
            dhRow = DHRow(*(parent.getMatrixFloats(accuracy)[0]))
            return dhRow.getHomoMatrixHari()
        else:
            out = (DHRow(*(parent.getMatrixFloats(accuracy)[0]))).getHomoMatrixHari()
            for i in range(1, len(parent.matrix)):
                # print(matrixGroup.get(parent).getMatrixFloats(2)[i])
                out = (out * (DHRow(*(parent.getMatrixFloats(accuracy)[i]))).getHomoMatrixHari())
            return out

def deleteItem(parent):
    for i in matrixGroup.keys():
        if matrixGroup[i]==parent:
            parent = i
            break
    if parent in matrixGroup:
        del matrixGroup[parent]


def getAll():
    for i in matrixGroup:
        print(f"{Fore.LIGHTMAGENTA_EX}{i}:\n{matrixGroup[i].getBeautyStringPro()}\n")


def editItem(parent, accuracy="Null"):
    for i in matrixGroup.keys():
        if matrixGroup[i]==parent:
            parent = i
            break
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
    Help Available at LinkdIn Post Images
    """
    printCyan(answer)


def about():
    answer = """
   Developed and Maintained by ChandiPatiya Software Solutions
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


def fullTrim(string):
    return string.replace(' ', '')


def generateOutputFromRight(rightSide, output=False):
    #print(rightSide)
    rights = rightSide.split('.')
    if not output:

        if len(rights) == 2:
            if rights[1] not in commandDictionary:
                print(matrixGroup.get(rights[0]).getBeautyStringProFraction(int(rights[1])))
            else:
                commandDictionary.get(rights[1])(matrixGroup.get(rights[0]), output)

        elif len(rights) == 3:
            commandDictionary.get(rights[1])(matrixGroup.get(rights[0]), output, int(rights[2]))
    else:
        return commandDictionary.get(rights[1])(matrixGroup.get(rights[0]), output)


commandDictionary = {
    #'=': equal,

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


'''def seperator(fullCommand):
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
            print(cin)
            equal(cin)

        else:
            command = [i for i in ('+', '-', '/', '*') if i in cin]
            print(commandDictionary.get(command[0])(cin, True))'''
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
        if '=' in cin:
            left, rights = cin.split('=')
            #print(left)
            #print(rights)
            matrixGroup[left] = generateOutputFromRight(rights, output=True)
        else:
            if '.' in cin:
                if 'new' in cin:
                    commandDictionary.get('new')(cin.split('.')[0])
                else:
                    '''print(cin)
                    print(matrixGroup.get(cin.split('.')[0]))
                    print(cin.split('.')[1])'''
                    #print(commandDictionary.get(cin.split('.')[1]))
                    #print(matrixGroup.get(cin.split('.')[0]))
                    generateOutputFromRight(cin)
            elif ('+' in cin) or ('-' in cin) or ('*' in cin):
                if '+' in cin:
                    print((matrixGroup.get(cin.split('+')[0])+matrixGroup.get(cin.split('+')[1])).getBeautyStringPro())
                elif '-' in cin:
                    print((matrixGroup.get(cin.split('-')[0])-matrixGroup.get(cin.split('-')[1])).getBeautyStringPro())
                elif '*' in cin:
                    print((matrixGroup.get(cin.split('*')[0])*matrixGroup.get(cin.split('*')[1])).getBeautyStringPro())


    #except:
        #printRed('~ Programme Temporarily Crashed Keep going')
        #continue
