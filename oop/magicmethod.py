class Fraction:
    def __init__(self, x, y):
        self.num = x
        self.den = y

    # def __str__(self):
    #     # print("hello") # TypeError: __str__ returned non-string (type NoneType) because this magic method only return value not print
    #     # return 'hello'
    #     return '{}/{}'.format(self.num, self.den)

    def __add__(self,other):
        # print('aaaddddddd')
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return '{}/{}'.format(new_num, new_den)

fr1 = Fraction(3, 4)
print(fr1)
fr2 = Fraction(1, 2)
print(fr2)
''' before implementing __add__ magic method '''
# print(fr1 + fr2) # TypeError: unsupported operand type(s) for +: 'Fraction' and 'Fraction'

''' 001 for example related to TypeError: unsupported operand type(s) for +: 'Fraction' and 'Fraction' '''
# s1 = {1, 2, 3}
# s2 = {3, 4, 5}
# print(s1 + s2) # TypeError: unsupported operand type(s) for +: 'set' and 'set'

''' after implementing __add__ magic method '''
# print(fr1 + fr2)    # aaaddddddd

print(fr1 + fr2)    # 10/8

