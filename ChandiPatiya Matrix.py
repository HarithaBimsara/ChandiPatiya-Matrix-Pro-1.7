# COLORAMA STUFF
import colorama
from colorama import Back, Fore, Style

colorama.init(autoreset=True)

from MatrixPro import HariMatrix

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
    return HariMatrix([[parent.getDeterminant()]])


def getInverse(parent, accuracy="Null"):
    if type(parent) == str:
        parent = matrixGroup.get(parent)
    return parent.inverse()


def getAdjoin(parent, accuracy="Null"):
    if type(parent) == str:
        parent = matrixGroup.get(parent)
    return parent.adjoin()


def getRe(parent, accuracy="Null"):
    if type(parent) == str:
        parent = matrixGroup.get(parent)
    return parent.getRowEchelon()


def getRre(parent, accuracy="Null"):
    if type(parent) == str:
        parent = matrixGroup.get(parent)
    return parent.getReducedRowEchelon()

def getTranspose(parent, accuracy="Null"):
    if type(parent) == str:
        parent = matrixGroup.get(parent)
    return parent.transpose()


def getDH(parent):
    if len(matrixGroup.get(parent).matrix) == 1:
        dhRow = DHRow(*(matrixGroup.get(parent).getMatrixFloats(2)[0]))
        return dhRow.getHomoMatrixHari()
    else:
        out = (DHRow(*(matrixGroup.get(parent).getMatrixFloats(2)[0]))).getHomoMatrixHari()
        for i in range(1, len(matrixGroup.get(parent).matrix)):
            #print(matrixGroup.get(parent).getMatrixFloats(2)[i])
            out = (out * (DHRow(*(matrixGroup.get(parent).getMatrixFloats(2)[i]))).getHomoMatrixHari())
        return out

#---------------------------------------------------------------


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
    Help not available Currently
    Check LinkdIn Account
    linkedin.com/in/haritha-herath-970180326
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



def fullTrim(string):
    return string.replace(' ', '')


def arithmaticOperationFound(cin):
    if ('+' in cin):
        rights = cin.split('+')
        return matrixGroup.get(rights[0]) + matrixGroup.get(rights[1])

    elif ('-' in cin):
        rights = cin.split('-')
        return matrixGroup.get(rights[0]) - matrixGroup.get(rights[1])

    elif ('*' in cin):
        rights = cin.split('*')
        return matrixGroup.get(rights[0]) * matrixGroup.get(rights[1])


commandDictionary = {
    'new': makeMatrix2,
    'det': getDet,
    'adj': getAdjoin,
    'inv': getInverse,
    're': getRe,
    'rre': getRre,
    'del': deleteItem,
    'edit': editItem,
    'tra' : getTranspose,
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
}

##########################################################


while running:
    try:
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
            if '.' in cin:
                if 'new' in cin:
                    commandDictionary.get(cin.split('.')[1])(cin.split('.')[0])
                elif '=' in cin:
                    newObjName = cin.split('=')[0]
                    rights = cin.split('=')[1].split('.')
                    matrixGroup[newObjName] = commandDictionary.get(rights[1])(rights[0])
                else:
                    rights = cin.split('.')
                    if rights[1] in commandDictionary:
                        if len(rights) == 3:
                            answer = commandDictionary.get(rights[1])(rights[0])
                            print(answer.getBeautyStringPro(int(rights[2])))
                        else:
                            answer = commandDictionary.get(rights[1])(rights[0])
                            if answer:
                                print(answer.getBeautyStringPro())
                    else:
                        print(matrixGroup.get(rights[0]).getBeautyStringPro(int(rights[1])))

            if ('+' in cin) or ('-' in cin) or ('*' in cin):
                if '=' in cin:
                    newObjName = cin.split('=')[0]
                    matrixGroup[newObjName]=arithmaticOperationFound(cin.split('=')[1])

                else:
                    print(arithmaticOperationFound(cin).getBeautyStringPro())




    except:
        printRed('~ Programme Crashed By Input Error')
        continue
