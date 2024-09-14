from napolita import Napolita


class BongoX:
    base = ''
    coefficient = Napolita('')

    def __init__(self, string):
        if type(string) == BongoX:
            self.base = string.base
            self.coefficient = string.coefficient

        elif BongoX.containsAlgebra(string):
            if len(string) == 1:
                self.base = string
                self.coefficient = Napolita('1')
            else:
                self.base = string[-1]
                self.coefficient = Napolita(string[:-1])
        else:
            self.base = ''
            self.coefficient = Napolita(string)

    #only for same base
    def __add__(self, other):
        new = BongoX('')
        new.base = self.base
        new.coefficient = self.coefficient + other.coefficient
        return new

    def __sub__(self, other):
        new = BongoX('')
        new.base = self.base
        new.coefficient = self.coefficient - other.coefficient
        return new

    def __mul__(self, other):
        new = BongoX('')
        new.base = self.base
        new.coefficient = self.coefficient * other.coefficient
        return new

    def get(self):
        return self.coefficient.get() + self.base

    @staticmethod
    def containsAlgebra(string):
        for i in string:
            if ord(i) not in range(48, 58) and i not in ('/', '-', '+', '.'):
                return True
        return False


'''a = BongoX('2')
b = BongoX('5')
print((a+b).get())'''
'''print(a.get())
print(a.coefficient.get())
print(a.base)'''





