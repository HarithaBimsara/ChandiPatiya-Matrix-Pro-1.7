class Napolita:
    def __init__(self, phrase):
        if type(phrase) == Napolita:
            self.up = phrase.getUp
            self.down = phrase.getDown
        else:
            phrase = phrase.replace(' ', '')
            if '/' in phrase and '.' not in phrase:
                self.up = int(phrase.split('/')[0])
                self.down = int(phrase.split('/')[1])
            elif phrase == '-':
                self.up = -1
                self.down = 1
            elif phrase == '+':
                self.up = 1
                self.down = 1
            elif len(phrase) != 0 and '.' not in phrase:
                self.up = int(phrase)
                self.down = 1
            elif len(phrase) == 0:
                self.up = 0
                self.down = 1
            elif '.' in phrase and '/' not in phrase:
                self.up = int(phrase.replace('.', ''))
                self.down = 10 ** (len(phrase)-phrase.index('.') - 1)
            elif '.' in phrase and '/' in phrase:
                a = Napolita(phrase.split('/')[0])
                b = Napolita(phrase.split('/')[1])
                c = a / b
                self.up = c.getUp()
                self.down = c.getDown()
        self.refresh()

    def getUp(self):
        return self.up

    def getDown(self):
        return self.down

    def isZero(self):
        if self.up == 0:
            return True
        return False

    def refresh(self):
        if self.down == 0:
            raise ZeroDivisionError
        '''for i in range(min(abs(self.up), abs(self.down)), 1, -1):
            if self.up % i == 0 and self.down % i == 0:
                self.up = self.up // i
                self.down = self.down // i'''
        GCD = self.gcd(self.up, self.down)
        if GCD:
            self.up = self.up // GCD
            self.down = self.down // GCD
        if self.up < 0 and self.down < 0:
            self.up = -1 * self.up
            self.down = -1 * self. down
        if self.up >= 0 and self.down < 0:
            self.up = self.up * -1
            self.down = self.down * -1
        if self.up == self.down:
            self.up = 1
            self.down = 1

    def get(self):
        self.refresh()
        if self.down == 1:
            return f'{self.up}'
        if self.up == 0:
            return '0'
        return f'{self.up}/{self.down}'

    def getRotated(self):
        new = Napolita('')
        new.up = self.down
        new.down = self.up
        return new

    def getFraction(self, noOfDecimals="Null"):
        fraction = self.up/self.down
        fraction = str(fraction)
        if noOfDecimals=="Null":
            return float(fraction)
        if noOfDecimals==0:
            return int(float(fraction))
        if len(fraction[fraction.index(".")+1:])>=noOfDecimals:
            return float(fraction[:fraction.index(".")+noOfDecimals+1])
        else:
            return float(fraction)

    def getFractionRound(self, noOfDecimals="Null"):
        fraction = self.up/self.down
        if noOfDecimals=="Null":
            return float(fraction)
        if noOfDecimals==0:
            return int(round(fraction, noOfDecimals))
        return round(fraction, noOfDecimals)


    @staticmethod
    def gcd(a, b):
        if 0 in (a, b):
            return 1
        a = abs(a)
        b = abs(b)
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        else:
            return a

    def __add__(self, other):
        if type(self) == Napolita and type(other) == Napolita:
            new = Napolita('')
            new.down = self.down * other.down
            new.up = self.up*other.down + other.up*self.down
            new.refresh()
            return new
        elif type(self) == Napolita:
            new = Napolita('')
            new.down = self.down
            new.up = self.up + other*self.down
            new.refresh()
            return new

    def __sub__(self, other):
        if type(self) == Napolita and type(other) == Napolita:
            new = Napolita('')
            new.down = self.down * other.down
            new.up = self.up*other.down - other.up*self.down
            new.refresh()
            return new
        elif type(self) == Napolita:
            new = Napolita('')
            new.down = self.down
            new.up = self.up + other*self.down
            new.refresh()
            return new

    def __mul__(self, other):
        if type(self) == Napolita and type(other) == Napolita:
            new = Napolita('')
            new.down = self.down * other.down
            new.up = self.up*other.up
            new.refresh()
            return new
        elif type(self) == Napolita:
            print(self.up, other)
            new = Napolita('')
            new.down = self.down
            new.up = self.up*other
            new.refresh()
            return new

    def __truediv__(self, other):
        if type(self) == Napolita and type(other) == Napolita:
            new = Napolita('')
            new.down = self.down * other.up
            new.up = self.up*other.down
            new.refresh()
            return new
        elif type(self) == Napolita:
            new = Napolita('')
            new.down = self.down*other
            new.up = self.up
            new.refresh()
            return new



