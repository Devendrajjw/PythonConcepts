class Demo:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        # print(self.a, self.b, 'demo')

    def addi(self):
        return self.a + self.b

class Demo1(Demo):
    def __init__(self, a, b):
        super().__init__(a, b)
        self.a = a * a
        # print(self.a, self.b, 'demo1')

d1 = Demo1(2, 3)
print(d1.addi())   # 7

