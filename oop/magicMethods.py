# class Demo:
#     name = 'Rudram'
#
#
# d = Demo()
# print(d)    # <__main__.Demo object at 0x00000219F9644210>
# print(d.name)
#
#
#
# class Demo1:
#     name = 'Devendra'
#     def __str__(self):
#         return self.name
#
#
# d1 = Demo1()
# print(d1)   # Devendra
#
#
#
# class Demo2:
#     name = 'Teddy'
#     def __repr__(self):
#         return self.name
#
#
# d2 = Demo2()
# print(d2) # Teddy
#
#
#
# class Demo3:
#     city = 'Bangalore'
#
#     def __init__(self, state):
#         self.state = state
#
#     def display(self):
#         return self.state
#
#     def __str__(self):
#         return f'{self.state} {self.city}'
#
#     # def __repr__(self):
#     #     return f'{self.state} {self.city}'
#
#
# d3 = Demo3('Karnataka')
# print(d3.state)     # Karnataka
# print(d3.city)      # Bangalore
# print(d3)           # Karnataka Bangalore
#
#

class D4:
    def __init__(self, a, b=10):
        self.a = a
        self.b = b

    def __int__(self):
        return self.a + self.b
    


d4 = D4(20)
print(d4)

