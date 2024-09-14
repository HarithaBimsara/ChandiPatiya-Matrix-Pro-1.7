from alge import BongoX
from matrix import HariMatrix


def isPrimarySymbol(a):
    primarySymbols = ['+', '-']
    if a in primarySymbols:
        return True
    return False


def getInverse(item):
    if '-' in item:
        return item[1:]
    return '-' + item


def joiner(array):
    out = []
    if len(array) != 1:
        one = array[0]
        array.remove(array[0])
        for i in range(len(array)):
            if array[i].base == one.base:
                one = one + array[i]
                array[i] = BongoX('0')
        out.append(one)
        out.extend(joiner(array))
    else:
        out.append(array[0])

    return out


def bongoAnalyser(*args):
    out = []
    for i in args:
        pre = []
        temp = i[0]
        for j in range(1, len(i)):
            if temp == '=':
                pre.append(temp)
                temp = i[j]
            elif not isPrimarySymbol(i[j]) and i[j] != '=':
                temp += i[j]
            elif i[j] == '=':
                pre.append(temp)
                temp = i[j]
            elif temp:
                pre.append(temp)
                temp = i[j]
        if '=' in temp:
            pre.append('=')
            pre.append(temp.replace('=', ''))
        else:
            pre.append(temp)
        for i in range(len(pre)):
            pre[i] = pre[i].replace('+', '')
        for i in range(pre.index('=')+1, len(pre)):
            pre[i] = getInverse(pre[i])
        pre.remove('=')
        for i in range(len(pre)):
            pre[i] = BongoX(pre[i])
        pre = joiner(pre)
        for i in pre:
            if i.base == '':
                break
        else:
            pre.append(BongoX('0'))
        out.append(pre)

    MATURED = []
    for i in range(len(out)):
        for j in range(len(out[i])):
            if out[i][j].base not in MATURED:
                MATURED.append(out[i][j].base)
    MAIN = []
    while '' in MATURED:
        MATURED.remove('')
    MATURED.append('')
    for i in range(len(out)):
        preMAIN = []
        for j in range(len(MATURED)):
            for k in range(len(out[i])):
                if MATURED[j] == '' and out[i][k].base == '':
                    preMAIN.append(BongoX(getInverse(out[i][k].coefficient.get())).coefficient)
                    break
                elif out[i][k].base == MATURED[j]:
                    preMAIN.append(out[i][k].coefficient)
                    break
            else:
                preMAIN.append(BongoX('0').coefficient)
        MAIN.append(preMAIN)

    inputs = HariMatrix(MAIN)
    RRE = inputs.getReducedRowEchelon()
    ans = list(map(lambda x: x.get(), HariMatrix([RRE.getColumn(len(MATURED))]).getRow(1)))
    if RRE.getRankA() == RRE.getRankAB() == len(MATURED)-1:
        result = ''
        for i in range(len(ans)):
            result += f'{MATURED[i]}  =  {ans[i]}\n'
        result = result.rstrip('\n')
        return result
    elif RRE.getRankAB() == RRE.getRankA():
        return f'Answers with {len(MATURED)-1-RRE.getRankA()} parameter(s)\nStill being developed'

    elif RRE.getRankA() != RRE.getRankAB():
        return 'No Solutions'



'''equationList = ['d-2/8a+b=-a-3b+4', '-b+a=-2b+c', '2=a-d', 'a+d=6-d']
equationList = ['-a=a', '-2.5a-c=2', '-c-b=-3/2']
#equationList = ['a+b=3', 'a+b+c=4']
print(bongoAnalyser(*equationList))'''
