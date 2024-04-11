class Demo:
    def __init__(self):
        self.emp_name = ''
        self.location = 'from Demo class'

    def set_name(self):
        name = input(" enter name ")
        self.emp_name = name

    def get_name(self):
        return self.emp_name

    def common(self):
        print(" from demo")


class Demo1(Demo):
    def __init__(self):
        self.location = 'from demo1 child class'

    def common(self):
        # super(Demo1, self).common()
        print(" from demo1")
        super().common()


obj1 = Demo()
obj2 = Demo1()
# print(obj1.common())
print(obj2.common())
# obj1.set_name()
# print(obj1.get_name())
# print(obj1.common())
