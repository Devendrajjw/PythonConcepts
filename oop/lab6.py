class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return f'hello my name is {self.name}'

    def get_age(self):
        return f'hello my age is {self.age}'


obj1 = Student('baba', 1)
obj2 = Student('jai', 6)

for data in (obj1, obj2):
    print(data.get_name())
    print(data.get_age())
    print()
