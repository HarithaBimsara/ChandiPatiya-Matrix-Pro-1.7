from napolita import Napolita


class HariMatrix:
    def __init__(self, *array):
        self.array = array
        if len(array) == 1 and type(array[0]) == list and type(array[0][0]) == list:
            self.createSuperIntMatrix()
            self.m = len(array[0])
            self.n = len(array[0][0])
        elif len(array) == 1 and type(array[0]) == list and array[0][0] * array[0][1] == len(array[0]) - 2:
            self.array = array[0]
            self.m = array[0][0]
            self.n = array[0][1]
            self.matrix = []
            self.createIntelligentMatrix()
        elif len(array) == 2:
            self.m = array[0]
            self.n = array[1]
            self.matrix = []
            self.createMatrix()
        elif len(array) < 2:
            self.changeCore(1, 1)
        elif len(array) > 2:
            self.m = array[0]
            self.n = array[1]
            self.createIntelligentMatrix()

    def __add__(self, other):
        global new
        if type(self) == HariMatrix and type(other) == HariMatrix:
            new = HariMatrix(self.getM(), self.getN())
            for i in range(self.getM()):
                for j in range(self.getN()):
                    new.enterElement(i, j, self.askElement(i, j) + other.askElement(i, j))
            return new
        elif type(self) == HariMatrix:
            new = HariMatrix(self.getM(), self.getN())
            other = new.getI() * other
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    new.enterElement(i, j, self.matrix[i][j]+other.askElement(i, j))
        return new

    def __sub__(self, other):
        global new
        if type(self) == HariMatrix and type(other) == HariMatrix:
            new = HariMatrix(self.getM(), self.getN())
            for i in range(self.getM()):
                for j in range(self.getN()):
                    new.enterElement(i, j, self.askElement(i, j) - other.askElement(i, j))
        elif type(self) == HariMatrix:
            new = HariMatrix(self.getM(), self.getN())
            other = new.getI() * other
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    new.enterElement(i, j, self.matrix[i][j] - other.askElement(i, j))
        return new

    def __mul__(self, other):
        global c
        if type(self) == HariMatrix and type(other) == HariMatrix:
            c = HariMatrix(self.getM(), other.getN())

            for i in range(self.getM()):

                holdx = self.getRow(i)

                for j in range(other.getN()):

                    count = Napolita('')
                    holdy = other.getColumn(j)
                    for k in range(len(holdy)):
                        count += holdx[k] * holdy[k]
                    c.enterElement(i, j, count)

        elif type(self) == HariMatrix:
            c = HariMatrix(self.getM(), self.getN())
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    c.enterElement(i, j, self.matrix[i][j]*other)
        return c

    def __eq__(self, other):
        if type(self) == HariMatrix and type(other) == HariMatrix and self.getM() == other.getM() and self.getN() == other.getN():
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    if self.askElement(i, j).get() != other.askElement(i, j).get():
                        return False
            return True


    #Administrative Stuffs

    def createIntelligentMatrix(self):
        c = 2
        self.matrix = []
        for v in range(self.m):
            semi = []
            for i in range(self.n):
                if type(self.array[c] == Napolita):
                    semi.append(self.array[c])
                else:
                    semi.append(Napolita(str(self.array[c])))
                c += 1
            self.matrix.append(semi)

    def createSuperIntMatrix(self):
        new = []
        for i in self.array[0]:
            pre = []
            for j in i:
                if type(j) == Napolita:
                    pre.append(j)
                else:
                    pre.append(Napolita(str(j)))
            new.append(pre)
        self.matrix = new

    def changeCore(self, m, n):
        self.m = m
        self.n = n
        self.createMatrix()

    def createMatrix(self):
        self.matrix = []
        for i in range(self.m):
            self.matrix.append([])
            for j in range(self.n):
                self.matrix[i].append(Napolita(''))

    ######################

    #Get and Enter

    def getClone(self):
        pre = []
        for i in self.matrix:
            temp = []
            for j in i:
                temp.append(j)
            pre.append(temp)
        new = HariMatrix(pre)
        return new

    def askElement(self, row, column):
        return self.matrix[row][column]

    def enterElement(self, row, column, data):
        if type(data) == Napolita:
            self.matrix[row][column] = data
        else:
            self.matrix[row][column] = Napolita(str(data))

    '''def getElement(self, row, column):
        return self.matrix[row - 1][column - 1].get()'''

    def enterWhole(self, x=0, y=0):
        if x == 0 or y == 0:
            for i in range(self.m):
                for j in range(self.n):
                    self.matrix[i][j] = Napolita(input(f"~Value for ({i + 1}, {j + 1})$ "))
        else:
            self.changeCore(x, y)
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    self.matrix[i][j] = Napolita(input(f"~Value for ({i + 1}, {j + 1})$ "))

    '''def get(self):
        return self.matrix'''

    def getOrder(self):
        return len(self.matrix) * len(self.matrix[0])

    def getM(self):
        return len(self.matrix)

    def getN(self):
        return len(self.matrix[0])

    def getString(self):
        out = '[\n'
        for i in range(len(self.matrix)):
            out += "\t["
            for j in range(len(self.matrix[0])):
                out += (self.matrix[i][j].get() + ', ')*(j != len(self.matrix[0])-1)
                out += (self.matrix[i][j].get()) * (j == len(self.matrix[0]) - 1)
            out += "],\n"*(i != len(self.matrix)-1)
            out += "]\n" * (i == len(self.matrix) - 1)

        out += ']'
        return out

    def getBeautyString(self):
        realOut = ''
        out = []
        for j in range(len(self.matrix[0])):
            pre = []
            largest = self.matrix[0][j].get()
            for i in range(len(self.matrix)):
                if len(self.matrix[i][j].get()) > len(largest):
                    largest = self.matrix[i][j].get()
            for i in range(len(self.matrix)):
                pre.append(' '*(len(largest)-len(self.matrix[i][j].get()))+self.matrix[i][j].get())
            out.append(pre)
        for i in range(len(out[0])):
            pre = ''
            for j in range(len(out)):
                pre += out[j][i] + '  '
            pre = pre.rstrip(' ')
            realOut += pre + '\n'
        realOut = realOut.strip('\n')
        return realOut

    def getBeautyStringPro(self):
        realOut = ''
        out = []
        for j in range(len(self.matrix[0])):
            pre = []
            largest = self.matrix[0][j].get()
            for i in range(len(self.matrix)):
                if len(self.matrix[i][j].get()) > len(largest):
                    largest = self.matrix[i][j].get()
            for i in range(len(self.matrix)):
                pre.append(' '*(len(largest)-len(self.matrix[i][j].get()))+self.matrix[i][j].get())
            out.append(pre)

        for i in range(len(out[0])):
            pre = '  | '
            for j in range(len(out)):
                pre += out[j][i] + '  '
            pre = pre.rstrip(' ')
            pre += ' |'
            realOut += pre + '\n'
        newRealOut = '  '+(len(realOut.split('\n')[0])-2)*'-'+'\n'
        newRealOut += realOut
        newRealOut += '  '+(len(realOut.split('\n')[0])-2)*'-'+'\n'
        return newRealOut.rstrip('\n')

    def getBeautyStringProFraction(self, accuracy="Null"):
        realOut = ''
        out = []
        for j in range(len(self.matrix[0])):
            pre = []
            largest = str(self.matrix[0][j].getFractionRound(accuracy))
            for i in range(len(self.matrix)):
                if len(str(self.matrix[i][j].getFractionRound(accuracy))) > len(str(largest)):
                    largest = self.matrix[i][j].getFractionRound(accuracy)
            for i in range(len(self.matrix)):
                pre.append(' '*(len(str(largest))-len(str(self.matrix[i][j].getFractionRound(accuracy))))+str(self.matrix[i][j].getFractionRound(accuracy)))
            out.append(pre)

        for i in range(len(out[0])):
            pre = '  | '
            for j in range(len(out)):
                pre += out[j][i] + '  '
            pre = pre.rstrip(' ')
            pre += ' |'
            realOut += pre + '\n'
        newRealOut = '  '+(len(realOut.split('\n')[0])-2)*'-'+'\n'
        newRealOut += realOut
        newRealOut += '  '+(len(realOut.split('\n')[0])-2)*'-'+'\n'
        return newRealOut.rstrip('\n')

    def getMatrixFloats(self, accuracy):
        out = []
        for i in range(len(self.matrix)):
            pre = []
            for j in range(len(self.matrix[0])):
                pre.append(self.matrix[i][j].getFractionRound(accuracy))

            out.append(pre)
        return out



    def getI(self):
        if self.getM() == self.getN():
            I = HariMatrix(self.getM(), self.getN())
            for i in range(self.getM()):
                for j in range(self.getN()):
                    if i == j:
                        I.enterElement(i, j, Napolita("1"))
                    else:
                        I.enterElement(i, j, Napolita(''))

            return I
        else:
            print("m != n")

    def enterOneElementToRow(self, row, element):
        if type(element) == Napolita:
            for i in range(len(self.matrix[row])):
                self.matrix[row][i] = element
        else:
            for i in range(len(self.matrix[row])):
                self.matrix[row][i] = Napolita(str(element))

    def enterOneElementToColumn(self, column, element):
        if type(element) == Napolita:
            for i in self.matrix:
                i[column] = Napolita(str(element))
        else:
            for i in self.matrix:
                i[column] = element

    def getRow(self, row):
        return self.matrix[row]

    def getColumn(self, column):
        out = []
        for i in self.matrix:
            out.append(i[column])
        return out

    def transpose(self):
        result = []
        for k in range(self.n):
            out = []
            for i in range(self.m):
                out.append(self.matrix[i][k])
            result.append(out)
        out = HariMatrix(result)
        return out

    def power(self, r):
        new = self.getI()
        for i in range(r):
            new = new * self
        return new

    #############################

    #Inside Changers

    def rowSpan(self, *data):
        if len(data) == self.getN() + 1:
            for k in range(data[0]):
                sem = []
                for i in range(self.getN()):
                    if type(data[i+1]) == Napolita:
                        sem.append(data[i + 1])
                    else:
                        sem.append(Napolita(str(data[i + 1])))
                self.matrix.append(sem)
        elif len(data) == 1:
            for i in range(data[0]):
                sem = []
                for i in range(self.getN()):
                    sem.append(Napolita(''))
                self.matrix.append(sem)
        elif len(data) == self.getN():
            sem = []
            for i in range(self.getN()):
                if type(data[i]) == Napolita:
                    sem.append(data[i])
                else:
                    sem.append(Napolita(str(data[i])))
            self.matrix.append(sem)
        else:
            return "Invalid Inputs"

    def colSpan(self, *data):
        if len(data) == self.getM() + 1:
            for k in range(data[0]):
                for i in range(self.getM()):
                    if type(data[i+1]) == Napolita:
                        self.matrix[i].append(data[i + 1])
                    else:
                        self.matrix[i].append(Napolita(str(data[i + 1])))
        elif len(data) == 1:
            for k in range(data[0]):
                for i in range(self.getM()):
                    self.matrix[i].append(Napolita(''))
        elif len(data) == self.getM():
            for i in range(self.getM()):
                if type(data[i]) == Napolita:
                    self.matrix[i].append(data[i])
                else:
                    self.matrix[i].append(Napolita(str(data[i])))
        else:
            return "Invalid Inputs"

    def clearRow(self, row):
        self.matrix.remove(self.matrix[row])

    def clearColumn(self, column):
        for i in range(self.getM()):
            self.matrix[i].remove(self.matrix[i][column])

    def rowExchange(self, a, b):
        temp = self.matrix[a]
        self.matrix[a] = self.matrix[b]
        self.matrix[b] = temp

    def colExchange(self, a, b):
        temp = []
        for i in self.matrix:
            temp.append(i[a])
        for i in range(len(self.matrix)):
            self.matrix[i][a] = self.matrix[i][b]
        for i in range(len(self.matrix)):
            self.matrix[i][b] = temp[i]

    ################

    #High Resource Users and Friends

    def itemAntiFamilyCreate(self, row, col):
        out = []
        for i in range(len(self.matrix)):
            semi = []
            for j in range(len(self.matrix[i])):
                if i != row - 1 and j != col - 1:
                    semi.append(self.matrix[i][j])
            out.append(semi)
        while [] in out:
            out.remove([])
        return out

    def det4(self, m):
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    def getDeterminant(self):
        def det4(m):
            return m[0][0] * m[1][1] - m[0][1] * m[1][0]

        def zeroCatcher(l):
            def nicoZeroCounter(array):
                zeros = 0
                for i in array:
                    if (i.isZero()):
                        zeros += 1
                return zeros

            def zeroXCatcher(l):
                zero_count = 0
                line = 0
                for i in range(len(l)):
                    if nicoZeroCounter(l[i]) >= zero_count:
                        zero_count = nicoZeroCounter(l[i])
                        line = i
                return line, zero_count

            def zeroYCatcher(l):
                zero_count = 0
                line = 0
                new_job = []
                for i in range(len(l)):
                    core = []
                    for j in range(len(l[0])):
                        core.append(l[j][i])
                    new_job.append(core)
                    if nicoZeroCounter(core)> zero_count:
                        zero_count = nicoZeroCounter(core)
                        line = i
                return line, zero_count, new_job

            x = zeroXCatcher(l)
            y = zeroYCatcher(l)
            if x[1] >= y[1]:
                return x[0], "x"
            else:
                return y[0], "y", y[2]

        if len(self.matrix) == len(self.matrix[0]):
            def itemAntiFamilyCreate(matrix, row, col):
                out = []
                for i in range(len(matrix)):
                    semi = []
                    for j in range(len(matrix[i])):
                        if i != row - 1 and j != col - 1:
                            semi.append(matrix[i][j])
                    out.append(semi)
                while [] in out:
                    out.remove([])
                return out

            def det(maxt):
                res = Napolita('')
                zero = zeroCatcher(maxt)
                if len(maxt) != 2:
                    if zero[1] == 'y':
                        maxt = zero[2]
                    line = zero[0]
                    for i in range(len(maxt[0])):
                        if (i + line) % 2 == 0:
                            if not (maxt[line][i].isZero()):
                                x = itemAntiFamilyCreate(maxt, line + 1, i + 1)
                                res += maxt[line][i] * det(x)
                        else:
                            if not (maxt[line][i].isZero()):
                                x = itemAntiFamilyCreate(maxt, line + 1, i + 1)
                                res -= maxt[line][i] * det(x)
                else:
                    res += det4(maxt)
                return res

            return det(self.matrix)
        else:
            return "No Output"

    def trace(self):
        if self.getM() == self.getN():
            tc = Napolita('')
            for i in range(len(self.matrix)):
                tc += self.matrix[i][i]
            return tc
        else:
            return "No Output"

    def adjoin(self):
        def itemAntiFamilyCreate(matrix, row, col):
            out = []
            for i in range(len(matrix)):
                semi = []
                for j in range(len(matrix[i])):
                    if i != row and j != col:
                        semi.append(matrix[i][j])
                out.append(semi)
            while [] in out:
                out.remove([])
            return out

        def getDeterminant(mat):
            def det4(m):
                return m[0][0] * m[1][1] - m[0][1] * m[1][0]

            def zeroCatcher(l):
                def nicoZeroCounter(array):
                    zeros = 0
                    for i in array:
                        if (i.isZero()):
                            zeros += 1
                    return zeros

                def zeroXCatcher(l):
                    zero_count = 0
                    line = 0
                    for i in range(len(l)):
                        if nicoZeroCounter(l[i]) >= zero_count:
                            zero_count = nicoZeroCounter(l[i])
                            line = i
                    return line, zero_count

                def zeroYCatcher(l):
                    zero_count = 0
                    line = 0
                    new_job = []
                    for i in range(len(l)):
                        core = []
                        for j in range(len(l[0])):
                            core.append(l[j][i])
                        new_job.append(core)
                        if nicoZeroCounter(core) > zero_count:
                            zero_count = nicoZeroCounter(core)
                            line = i
                    return line, zero_count, new_job

                x = zeroXCatcher(l)
                y = zeroYCatcher(l)
                if x[1] >= y[1]:
                    return x[0], "x"
                else:
                    return y[0], "y", y[2]

            if len(mat) == len(mat[0]):

                def itemAntiFamilyCreate(matrix, row, col):
                    out = []
                    for i in range(len(matrix)):
                        semi = []
                        for j in range(len(matrix[i])):
                            if i != row - 1 and j != col - 1:
                                semi.append(matrix[i][j])
                        out.append(semi)
                    while [] in out:
                        out.remove([])
                    return out

                def det(maxt):
                    res = Napolita('')
                    zero = zeroCatcher(maxt)
                    if len(maxt) != 2:
                        if zero[1] == 'y':
                            maxt = zero[2]
                        line = zero[0]
                        for i in range(len(maxt[0])):
                            if (i + line) % 2 == 0:
                                if not (maxt[line][i].isZero()):
                                    x = itemAntiFamilyCreate(maxt, line + 1, i + 1)
                                    res += maxt[line][i] * det(x)
                            else:
                                if not (maxt[line][i].isZero()):
                                    x = itemAntiFamilyCreate(maxt, line + 1, i + 1)
                                    res -= maxt[line][i] * det(x)
                    else:
                        res += det4(maxt)
                    return res

                return det(mat)
            else:
                return "No Output"

        if len(self.matrix) == len(self.matrix[0]):
            pop = []
            if len(self.matrix) > 2:

                for i in range(len(self.matrix)):
                    lop = []
                    for j in range(len(self.matrix[0])):
                        if (i + j) % 2 == 0:
                            lop.append(getDeterminant(itemAntiFamilyCreate(self.matrix, i, j)))
                        else:
                            lop.append(getDeterminant(itemAntiFamilyCreate(self.matrix, i, j)) * -1)
                    pop.append(lop)

            elif len(self.matrix) == 2:
                pop = [
                    [self.matrix[1][1], self.matrix[1][0] * -1],
                    [self.matrix[0][1] * -1, self.matrix[0][0]]
                ]
            sex = HariMatrix(pop)
            return sex.transpose()
        else:
            return "No Output"

    def inverse(self):
        if self.getM() == self.getN():
            adj = self.adjoin().matrix
            det = self.getDeterminant()
            ou = []
            if det != 0:
                for i in adj:
                    c = []
                    for j in i:
                        ans = j / det
                        c.append(ans)
                    ou.append(c)
                out = HariMatrix(ou)
                return out
            else:
                return "Not Inversible"
        else:
            return "No Output"

    #############################

    #True False Stuff

    def isSquare(self):
        if self.getM() == self.getN():
            return True
        else:
            return False

    def isSymmetric(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j].get() != self.matrix[j][i].get():
                    return False
        return True

    def isSkewSymmetric(self):
        if self.isSquare():
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    if i == j:
                        if self.matrix[i][j].get() != '0':
                            return False
                    else:
                        if self.matrix[i][j].get() != '-' + self.matrix[j][i].get() and self.matrix[j][i].get() != '-' + self.matrix[i][j].get():
                            return False
            else:
                return True
        else:
            return "Not Square"

    def isOrthogonal(self):
        a = self * self.transpose()
        for i in range(a.getM()):
            for j in range(len(a.getRow(i))):
                if a.askElement(i, j).get() != self.getI().askElement(i, j).get():
                    return False
        return True

    #############

    #Row Operation Stuff

    def rowMultiply(self, row, num):
        num = Napolita(str(num))
        for i in range(len(self.matrix[row])):
            self.matrix[row][i] = self.matrix[row][i]*num

    def colMultiply(self, col, num):
        num = Napolita(str(num))
        for i in range(self.getM()):
            self.matrix[i][col] = self.matrix[i][col] * num

    def rowAddOperation(self, me, you, yourNum):
        yourNum = Napolita(str(yourNum))
        for i in range(self.getN()):
            self.matrix[me][i] += self.matrix[you][i] * yourNum

    def getRowEchelon(self):
        b = self.getClone()
        for i in range(b.getM()):
            if b.matrix[i][i].get() != '0':
                b.rowMultiply(i, b.matrix[i][i].getRotated().get())
                for j in range(i+1, b.getM()):
                    b.rowAddOperation(j, i, ((b.matrix[j][i]/b.matrix[i][i])*-1).get())
            else:
                for k in range(i+1, b.getM()):
                    if b.matrix[k][i].get() != '0':
                        b.rowExchange(i, k)
                        b.rowMultiply(i, b.matrix[i][i].getRotated().get())
                        for j in range(i + 1, b.getM()):
                            b.rowAddOperation(j, i, ((b.matrix[j][i] / b.matrix[i][i]) * -1).get())
        return b

    def getReducedRowEchelon(self):
        rowEchelonMatrix = self.getRowEchelon()
        for i in range(rowEchelonMatrix.getM()-1, 0, -1):
            if rowEchelonMatrix.matrix[i][i].get() != '0':
                rowEchelonMatrix.rowMultiply(i, rowEchelonMatrix.matrix[i][i].getRotated().get())
                for j in range(i-1, -1, -1):
                    rowEchelonMatrix.rowAddOperation(j, i, ((rowEchelonMatrix.matrix[j][i] / rowEchelonMatrix.matrix[i][i]) * -1).get())
        return rowEchelonMatrix

    def getRankAB(self):
        rank = 0
        mat = self.getRowEchelon()
        for i in range(len(mat.matrix)):
            for j in range(len(mat.matrix[0])):
                if mat.matrix[i][j].get() != '0':
                    rank += 1
                    break
        return rank

    def getRankA(self):
        rank = 0
        mat = self.getClone()
        mat = mat.getRowEchelon()
        mat.clearColumn(self.getN()-1)
        for i in range(len(mat.matrix)):
            for j in range(len(mat.matrix[0])):
                if mat.matrix[i][j].get() != '0':
                    rank += 1
                    break
        return rank

    def rowOperatedInverse(self):
        I = self.getI().getClone()
        b = self.getClone()
        for i in range(b.getM()):
            if b.matrix[i][i].get() != '0':
                devider = b.matrix[i][i].getRotated().get()
                b.rowMultiply(i, devider)
                I.rowMultiply(i, devider)
                for j in range(i + 1, b.getM()):
                    num = ((b.matrix[j][i] / b.matrix[i][i]) * -1).get()
                    b.rowAddOperation(j, i, num)
                    I.rowAddOperation(j, i, num)
            else:
                for k in range(i + 1, b.getM()):
                    if b.matrix[k][i].get() != '0':
                        b.rowExchange(i, k)
                        I.rowExchange(i, k)
                        devider = b.matrix[i][i].getRotated().get()
                        b.rowMultiply(i, devider)
                        I.rowMultiply(i, devider)
                        for j in range(i + 1, b.getM()):
                            num = ((b.matrix[j][i] / b.matrix[i][i]) * -1).get()
                            b.rowAddOperation(j, i, num)
                            I.rowAddOperation(j, i, num)
        for i in range(b.getM() - 1, 0, -1):
            if b.matrix[i][i].get() != '0':
                devider = b.matrix[i][i].getRotated().get()
                b.rowMultiply(i, devider)
                I.rowMultiply(i, devider)
                for j in range(i - 1, -1, -1):
                    num = ((b.matrix[j][i] / b.matrix[i][i]) * -1).get()
                    b.rowAddOperation(j, i, num)
                    I.rowAddOperation(j, i, num)
        return I

    ########################


a = [['1', '2'], ['4', '6/7']]
a = HariMatrix(a)
print(a.getDeterminant().get())
print(a.getBeautyStringPro())
print(a.getBeautyStringProFraction(3))
print(a.getMatrixFloats(3))